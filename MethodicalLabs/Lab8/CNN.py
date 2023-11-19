import tensorflow as tf
import matplotlib.pyplot as plt

(trainImages, trainLabels), (testImages, testLabels) = tf.keras.datasets.cifar10.load_data()

trainImages, testImages = trainImages / 255.0, testImages / 255.0

class_names = ['літак', 'автомобіль', 'птаха', 'кіт', 'олень',
               'собака', 'жаба', 'кінь', 'корабель', 'вантажівка']

plt.figure(figsize=(10,10))
for i in range(20):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(trainImages[i])
    plt.xlabel(class_names[trainLabels[i][0]])
plt.show()

model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.MaxPooling2D((2, 2)))
model.add(tf.keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(10))

model.summary()

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

history = model.fit(trainImages, trainLabels, epochs=10,
                    validation_data=(testImages, testLabels))

plt.plot(history.history['accuracy'], label='Точність')
plt.plot(history.history['val_accuracy'], label = 'Точність значень')
plt.xlabel('Епоха')
plt.ylabel('Точність')
plt.ylim([0.5, 1])
plt.legend(loc='lower right')

plt.show()

testLoss, testAcc = model.evaluate(testImages,  testLabels, verbose=2)

print(testAcc)