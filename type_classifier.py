from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense,Convolution2D,MaxPooling2D,Flatten,Conv2D,Dropout
from keras.preprocessing.image import ImageDataGenerator
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
from PIL import Image
import tensorflow as tf
import cv2

NUM_CLASSES = 17

IMAGE_SIZE = 120

DATASET_PATH = "data/pokemon_per_type"

def to_lab(image):
    image = np.array(image)
    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    return lab_image

if __name__ == "__main__":

    # Creating the model
    model=Sequential()
    model.add(Dense(4, input_shape = (IMAGE_SIZE, IMAGE_SIZE, 3), activation = 'relu'))

    model.add(Conv2D(64, (3, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Conv2D(128, (3, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Conv2D(256, (3, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))

    model.add(Conv2D(512, (3, 3), activation = 'relu'))
    model.add(MaxPooling2D(pool_size = (2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(1024, activation = 'relu'))

    model.add(Dense(NUM_CLASSES, activation = 'softmax'))

    model.compile(loss = 'categorical_crossentropy', optimizer = 'adam', metrics = ['accuracy'])




    train_datagen = ImageDataGenerator(rescale = 1./255, 
                                    shear_range = 0.2, 
                                    zoom_range = 0.2, 
                                    rotation_range = 20,
                                    horizontal_flip = True,
                                    preprocessing_function = to_lab)

    test_datagen = ImageDataGenerator(rescale = 1./255,
                                    preprocessing_function = to_lab)

    training_set = train_datagen.flow_from_directory(DATASET_PATH + '/train', 
                                                        target_size = (IMAGE_SIZE, IMAGE_SIZE), 
                                                        batch_size = 100)
    test_set = test_datagen.flow_from_directory(DATASET_PATH + '/val',
                                                    target_size = (IMAGE_SIZE, IMAGE_SIZE),
                                                    batch_size = 100)

    nb_epochs = 100
    fitted_model = model.fit(training_set,
                            epochs = nb_epochs,
                            validation_data = test_set)

    plt.figure()
    plt.plot([i for i in range(nb_epochs)],fitted_model.history['accuracy'], label = "Training Accuracy")
    plt.plot([i for i in range(nb_epochs)],fitted_model.history['val_accuracy'], label = "Validation Accuracy")
    plt.legend()

    plt.show()

    plt.figure()
    plt.plot([i for i in range(nb_epochs)],fitted_model.history['loss'], label = "Training Loss")
    plt.plot([i for i in range(nb_epochs)],fitted_model.history['val_loss'], label = "Validation Loss")
    plt.legend()
    plt.show()
