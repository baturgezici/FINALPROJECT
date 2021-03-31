from flask import Flask, render_template, redirect, url_for, request, session
import pymongo

app = Flask(__name__)
app.secret_key="abdulhalukbaturgezici"

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["admin"]
mycol = mydb["User"]

@app.route('/')
def home():
    return "Hello, World!"  # return a string

@app.route('/userpage')
def userpage():
    return render_template('userpage.html')

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')  # render a template

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        myq = {"username":request.form['username'],"password":request.form['password']}
        if mycol.find(myq).count() > 0:
            return render_template('userpage.html', username = request.form['username'])
    return render_template('login.html', error=error)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        newuser = {"username": request.form['username'], "password": request.form['password'], "email": request.form['email']}
        x = mycol.insert_one(newuser)
        session["username"] = request.form['username']
        y = session["username"]
        return render_template('userpage.html', username=y)
    return render_template('signup.html')

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
