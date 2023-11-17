import matplotlib.pyplot as plt
import numpy
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow import keras

from ucimlrepo import fetch_ucirepo

wine_quality = fetch_ucirepo(id=186)

x = wine_quality.data.features
y = wine_quality.data.targets

trainFeatures = x.sample(frac=0.8, random_state=0)
trainLabels = y.sample(frac=0.8, random_state=0)

testFeatures = x.drop(trainFeatures.index)
testLabels = y.drop(trainLabels.index)

# # metadata
print(wine_quality.metadata)
#
# # variable information
print(testFeatures)
print(trainFeatures)

normalizer = tf.keras.layers.Normalization(axis=-1)
normalizer.adapt(np.array(trainFeatures))

first = np.array(trainFeatures[:1])

with np.printoptions(precision=2, suppress=True):
    print('Початкові дані:', first)
    print('Дані після нормалізації:', normalizer(first).numpy())

alcohol = np.array(trainFeatures['alcohol'])

alcoholNormalizer = keras.layers.Normalization(input_shape=[1,], axis=None)
alcoholNormalizer.adapt(alcohol)

alcoholModel = tf.keras.Sequential([
    alcoholNormalizer,
    keras.layers.Dense(units=1)
])

alcoholModel.summary()

print(alcoholModel.predict(alcohol[:10]))

alcoholModel.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='mean_absolute_error')

history = alcoholModel.fit(
    trainFeatures['alcohol'],
    trainLabels,
    epochs=50,
    validation_split=0.2)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

print(hist)

plt.plot(hist['loss'], label='loss')
plt.plot(hist['val_loss'], label='val_loss')
plt.ylim([0, 10])
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.legend()
plt.grid(True)
plt.show()

test_results = {}

test_results['alcoholModel'] = alcoholModel.evaluate(
    testFeatures['alcohol'],
    testLabels, verbose=0)

x = tf.linspace(0.0, 250, 251)
y = alcoholModel.predict(x)

print(y)

plt.scatter(trainFeatures['alcohol'], trainLabels, label='Data')
plt.plot(x, y, color='k', label='Predictions')
plt.xlabel('alcohol')
plt.ylabel('qual')
plt.legend()
plt.show()

linearModel = tf.keras.Sequential([
    normalizer,
    keras.layers.Dense(units=1)
])

linearModel.compile(
    optimizer=tf.keras.optimizers.Adam(),
    loss='mean_absolute_error'
)

history = linearModel.fit(
    trainFeatures,
    trainLabels,
    epochs=50,
    validation_split=0.2
)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

plt.plot(hist['loss'], label='loss')
plt.plot(hist['val_loss'], label='val_loss')
plt.ylim([0, 10])
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.legend()
plt.grid(True)
plt.show()

test_results['linear_model'] = linearModel.evaluate(
    testFeatures, testLabels, verbose=0)

deepModel = keras.Sequential([
    normalizer,
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(64, activation='relu'),
    keras.layers.Dense(1)
])

deepModel.compile(loss='mean_absolute_error',
            optimizer=tf.keras.optimizers.Adam(0.001))

history = deepModel.fit(
    trainFeatures,
    trainLabels,
    epochs=50,
    validation_split=0.2)

hist = pd.DataFrame(history.history)
hist['epoch'] = history.epoch
hist.tail()

plt.plot(hist['loss'], label='loss')
plt.plot(hist['val_loss'], label='val_loss')
plt.ylim([0, 10])
plt.xlabel('Epoch')
plt.ylabel('Error')
plt.legend()
plt.grid(True)
plt.show()

test_results['dnn_model'] = deepModel.evaluate(testFeatures, testLabels, verbose=0)

print(pd.DataFrame(test_results, index=['Середня абсолютна похибка']).T)

testPredictions = deepModel.predict(testFeatures).flatten()

print('Істинні значення')
print(np.array(testLabels['quality']))
print('Передбачення')
print(testPredictions)

a = plt.axes(aspect='equal')
plt.scatter(testLabels, testPredictions)
plt.xlabel('Істинні значення')
plt.ylabel('Передбачення')
lims = [0, 50]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)
plt.show()

# error = testPredictions - testLabels
# plt.hist(error, bins=25)
# plt.xlabel('Похибка передбачення')
# _ = plt.ylabel('Значення')