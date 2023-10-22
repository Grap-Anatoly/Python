import tensorflow as tf
from tensorflow import keras

import tensorflow_model_optimization as tfmot

import numpy as np
import tempfile
import zipfile
import os

mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images / 255.0
test_images  = test_images / 255.0

model = keras.Sequential([
    keras.layers.InputLayer(input_shape=(28, 28)),
    keras.layers.Reshape(target_shape=(28, 28, 1)),
    keras.layers.Conv2D(filters=12, kernel_size=(3, 3), activation=tf.nn.relu),
    keras.layers.MaxPooling2D(pool_size=(2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(10)
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
              metrics=['accuracy'])

model.fit(
    train_images,
    train_labels,
    validation_split=0.1,
    epochs=10
)

baseline_model_accuracy = model.evaluate(
    test_images, test_labels, verbose=0)

print('Початкова точність:', baseline_model_accuracy)

cluster_weights = tfmot.clustering.keras.cluster_weights
CentroidInitialization = tfmot.clustering.keras.CentroidInitialization

clustering_params = {
  'number_of_clusters': 16,
  'cluster_centroids_init': CentroidInitialization.LINEAR
}

clustered_model = cluster_weights(model, **clustering_params)

opt = tf.keras.optimizers.Adam(learning_rate=1e-5)

clustered_model.compile(
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
    optimizer=opt,
    metrics=['accuracy'])

clustered_model.summary()

clustered_model.fit(
    train_images,
    train_labels,
    batch_size=500,
    epochs=1,
    validation_split=0.1)

clustered_model_accuracy = clustered_model.evaluate(test_images, test_labels, verbose=0)

print('Точність моделі без кластеризації:', baseline_model_accuracy)
print('Точність моделі з кластеризацією:', clustered_model_accuracy)

final_model = tfmot.clustering.keras.strip_clustering(clustered_model)

clustered_tflite_file = '/tmp/clustered.tflite'
converter = tf.lite.TFLiteConverter.from_keras_model(final_model)
tflite_clustered_model = converter.convert()

with open(clustered_tflite_file, 'wb') as f:
    f.write(tflite_clustered_model)
print('Кластеризовану модель збережено до:', clustered_tflite_file)
