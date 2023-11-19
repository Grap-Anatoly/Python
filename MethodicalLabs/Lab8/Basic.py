import os
import re
import shutil
import string

import tensorflow as tf
import matplotlib.pyplot as plt

# url = "https://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz"
#
# dataset = tf.keras.utils.get_file("aclImdb_v1", url, untar=True, cache_dir='.', cache_subdir='')
#
# datasetDir = os.path.join(os.path.dirname(dataset), 'aclImdb')
#
# print(os.listdir(datasetDir))

trainDir = os.path.join(r'C:\Users\User\Desktop\Univer Aspirantura\Methodical\Labs\Lab8\aclImdb', 'train')
print(os.listdir(trainDir))

sampleFile = os.path.join(trainDir, 'pos/1181_9.txt')
with open(sampleFile) as f:
    print(f.read())

remove_dir = os.path.join(trainDir, 'unsup')
shutil.rmtree(remove_dir)

batch_size = 32
seed = 42

rawTrainDs = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='training',
    seed=seed)

rawTestDs = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/test',
    batch_size=batch_size)

rawValDs = tf.keras.utils.text_dataset_from_directory(
    'aclImdb/train',
    batch_size=batch_size,
    validation_split=0.2,
    subset='validation',
    seed=seed)

def customStandardization(inputData):
    lowercase = tf.strings.lower(inputData)
    stripped_html = tf.strings.regex_replace(lowercase, '<br />', ' ')
    return tf.strings.regex_replace(stripped_html, '[%s]' % re.escape(string.punctuation), '')

max_features = 10000
sequence_length = 250

vectorizeLayer = tf.keras.layers.TextVectorization(
    standardize=customStandardization,
    max_tokens=max_features,
    output_mode='int',
    output_sequence_length=sequence_length)

trainText = rawTestDs.map(lambda x, y: x)
vectorizeLayer.adapt(trainText)

def vectorizeText(text, label):
    text = tf.expand_dims(text, -1)
    return vectorizeLayer(text), label

text_batch, label_batch = next(iter(rawTrainDs))
first_review, first_label = text_batch[0], label_batch[0]
print("Оглад", first_review)
print("Мітка", rawTrainDs.class_names[first_label])
print("Векторизований огляд", vectorizeText(first_review, first_label))

trainDs = rawTrainDs.map(vectorizeText)
valDs = rawValDs.map(vectorizeText)
testDs = rawTestDs.map(vectorizeText)

AUTOTUNE = tf.data.AUTOTUNE

trainDs = trainDs.cache().prefetch(buffer_size=AUTOTUNE)
valDs = valDs.cache().prefetch(buffer_size=AUTOTUNE)
testDs = testDs.cache().prefetch(buffer_size=AUTOTUNE)

embedding_dim = 16

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(max_features, embedding_dim),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.GlobalAveragePooling1D(),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(1)])

model.summary()

model.compile(loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              optimizer='adam',
              metrics=tf.metrics.BinaryAccuracy(threshold=0.0))

epochs = 10
history = model.fit(
    trainDs,
    validation_data=valDs,
    epochs=epochs)

loss, accuracy = model.evaluate(testDs)

print("Втрати: ", loss)
print("Точність: ", accuracy)

history_dict = history.history

acc = history_dict['binary_accuracy']
val_acc = history_dict['val_binary_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']

epochs = range(1, len(acc) + 1)

plt.plot(epochs, acc, 'bo', label='Точність тренування')
plt.plot(epochs, val_acc, 'b', label='Точність перевірки')
plt.title('Графік точності')
plt.xlabel('Епохи')
plt.ylabel('Точність')
plt.legend(loc='lower right')

plt.show()

exportModel = tf.keras.Sequential([
    vectorizeLayer,
    model,
    tf.keras.layers.Activation('sigmoid')
])

exportModel.compile(
    loss=tf.keras.losses.BinaryCrossentropy(from_logits=False), optimizer="adam", metrics=['accuracy']
)

loss, accuracy = exportModel.evaluate(rawTestDs)
print(accuracy)

examples = [
  "The movie was Amazing!",
  "The movie was okay.",
  "The movie was terrible...",
  "The movie was great!",
  "The movie was Bad!",
]

print(exportModel.predict(examples))