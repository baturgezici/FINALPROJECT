from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()

def CNN():
    modelCNN = Sequential()
    modelCNN.add(Conv2D(128, kernel_size=(5, 5), strides=1, input_shape=(32, 32, 1), padding='same', activation='relu'))
    modelCNN.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    modelCNN.add(Conv2D(128, kernel_size=(5, 5), strides=1, padding='same', activation='relu'))
    modelCNN.add(MaxPooling2D(pool_size=(2, 2), padding='same'))
    modelCNN.add(Flatten())
    modelCNN.add(Dense(2048, activation = 'relu'))
    modelCNN.add(Dense(1024*colors, activation = 'softmax'))
    modelCNN.summary()

    adamOptimizer = keras.optimizers.Adam(lr=0.001)
    modelCNN.compile(optimizer=adamOptimizer, loss='categorical_crossentropy', metrics=['accuracy'])
