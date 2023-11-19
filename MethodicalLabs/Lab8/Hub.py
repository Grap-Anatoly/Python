import os
import numpy as np

import tensorflow as tf
import tensorflow_hub as hub
import tensorflow_datasets as tfds

trainData, validationData, testData = tfds.load(
    name="imdb_reviews",
    split=('train[:60%]', 'train[60%:]', 'test'),
    as_supervised=True)

trainExamplesBatch, trainLabelsBatch = next(iter(trainData.batch(10)))

embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
hubLayer = hub.KerasLayer(embedding, input_shape=[],
                           dtype=tf.string, trainable=True)

print(hubLayer(trainExamplesBatch[:3]))

model = tf.keras.Sequential()
model.add(hubLayer)
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(1))

model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(trainData.shuffle(10000).batch(512),
                    epochs=10,
                    validation_data=validationData.batch(512),
                    verbose=1)

results = model.evaluate(testData.batch(512), verbose=2)

for name, value in zip(model.metrics_names, results):
    print("%s: %.3f" % (name, value))