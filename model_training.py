#Engineering 133 Personal Project - CNN on MNIST Dataset
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


#MNIST Dataset
dataset = tf.keras.datasets.mnist

#Split into training data with labels and testing data with labels
(x_train, y_train), (x_test, y_test) = dataset.load_data()

input_shape = (28, 28, 1)

#Reshape the data points
x_train=x_train.reshape(x_train.shape[0], x_train.shape[1], x_train.shape[2], 1)
x_train=x_train / 255.0
x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], x_test.shape[2], 1)
x_test=x_test/255.0

y_train = tf.one_hot(y_train.astype(np.int32), depth=10)
y_test = tf.one_hot(y_test.astype(np.int32), depth=10)

batch_size = 64
num_classes = 10
epochs = 2


#The following lines are copied from online, at this website: https://www.kaggle.com/code/amyjang/tensorflow-mnist-cnn-tutorial
#I do not know how to design model architecture myself, and this architecture worked really well
model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (5,5), padding='same', activation='relu', input_shape=input_shape),
    tf.keras.layers.Conv2D(32, (5,5), padding='same', activation='relu'),
    tf.keras.layers.MaxPool2D(),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    tf.keras.layers.Conv2D(64, (3,3), padding='same', activation='relu'),
    tf.keras.layers.MaxPool2D(strides=(2,2)),
    tf.keras.layers.Dropout(0.25),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(num_classes, activation='softmax')
])

model.compile(optimizer=tf.keras.optimizers.RMSprop(epsilon=1e-08), loss='categorical_crossentropy', metrics=['acc'])

#Train the model.
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    validation_split=0.1,)

#model.save('model.keras')
model.save_weights('model_weights_newly_trained.h5')


#Evaluate model on test data and evaluate results
test_loss, test_acc = model.evaluate(x_test, y_test)
print('\nTest accuracy:', test_acc)