from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


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
