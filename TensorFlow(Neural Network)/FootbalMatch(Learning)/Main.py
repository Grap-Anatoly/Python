import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer

def first_model(n_classes):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(2000, activation='relu'),
        tf.keras.layers.BatchNormalization(),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(45, activation='relu'),
        tf.keras.layers.BatchNormalization(),
         tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(n_classes, activation='softmax')
    ])
    model.compile(optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy'])

    return model


def fit_print (X_train, X_test, y_train, y_test, n_classes):
    t = Tokenizer(num_words=200)
    t.fit_on_texts(X_train)

    X_train = t.texts_to_matrix(X_train, mode='count')
    X_test = t.texts_to_matrix(X_test, mode='count')

    print (X_train.shape)
    model=first_model(n_classes)
    model.fit(X_train, y_train, epochs=5)
    results = model.evaluate(X_test, y_test, verbose=1)

    print ('test loss: {0}, test acc: {1}'.format(results[0],results[1]))
    y_pred = np.argmax(model.predict(X_test), axis=-1)
    con_mat = tf.math.confusion_matrix(labels=y_test, predictions=y_pred)

    print(con_mat.numpy())

# X_train_zab = 'Перемога','Поразка','Перемога','Поразка','Поразка',\
#               'Перемога', 'Перемога','Поразка','Перемога','Перемога',\
#               'Поразка', 'Перемога', 'Перемога', 'Перемога', 'Поразка',\
#               'Поразка', 'Перемога', 'Поразка', 'Поразка', 'Поразка',\
#               'Перемога', 'Поразка', 'Перемога', 'Поразка', 'Перемога',\
#               'Перемога', 'Перемога', 'Поразка', 'Перемога', 'Поразка'
# X_train_zab = '10.01.12','11.02.12','17.02.12','22.03.12','29.03.12','15.04.12', '27.04.12','29.05.12','03.07.12','20.07.12','29.07.12'
# Гра: наша команди - команда супротивника (30 записів)
X_train_zab = 'Карпати','Шахтар','Дніпро','Арсенал','Металіст',\
              'Металіст', 'Карпати','Олександрія','Тернопіль','Ворскла',\
              'Шахтар', 'Дніпро', 'Ворскла', 'Тернопіль', 'Шахтар',\
              'Арсенал', 'Карпати', 'Металіст', 'Карпати', 'Тернопіль',\
              'Ворскла', 'Дніпро', 'Олександрія', 'Миколаїв', 'Ворскла',\
              'Шахтар', 'Карпати', 'Металіст', 'Шахтар', 'Арсенал'
# 1 - Перемога, 0 - Поразка
y_train_zab = [1,0,1,0,0,
               1,1,0,1,1,
               0,1,1,1,0,
               0,1,0,0,0,
               1,0,1,0,1,
               1,1,0,1,0]

# Тестова вибірка(60 записів)
X_test_zab = 'Шахтар','Тернопіль','Арсенал','Металіст','Дніпро',\
              'Ворскла', 'Дніпро','Маріуполь','Карпати','Шахтар',\
              'Тернопіль', 'Карпати', 'Таврія', 'Тернопіль', 'Маріуполь',\
              'Карпати', 'Таврія', 'Дніпро', 'Ворскла', 'Карпати',\
              'Арсенал', 'Ворскла', 'Шахтар', 'Металіст', 'Тернопіль',\
              'Дніпро', 'Карпати', 'Арсенал', 'Маріуполь', 'Ворскла',\
              'Тернопіль','Шахтар','Дніпро','Таврія','Карпати',\
              'Металіст', 'Ворскла','Ворскла','Карпати','Таврія',\
              'Дніпро', 'Карпати', 'Маріуполь', 'Металіст', 'Шахтар',\
              'Ворскла', 'Ворскла', 'Арсенал', 'Ворскла', 'Карпати',\
              'Металіст', 'Карпати', 'Дніпро', 'Арсенал', 'Арсенал',\
              'Ворскла', 'Шахтар', 'Ворскла', 'Таврія', 'Металіст'
y_test_zab = [0,0,1,1,0,
              0,0,1,1,0,
              1,1,0,0,1,
              0,1,1,0,1,
              1,1,0,0,0,
              0,1,1,1,0,
              1,1,1,0,0,
              1,0,0,1,0,
              0,0,1,1,0,
              1,1,1,1,0,
              1,0,1,1,1,
              0,0,0,1,0]

n_classes = 200

fit_print (X_train_zab, X_test_zab,np.array(y_train_zab), np.array(y_test_zab), n_classes)

