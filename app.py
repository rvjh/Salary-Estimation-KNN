import numpy as np
from flask import Flask, jsonify, request, render_template
import pickle
import math

app = Flask(__name__)
model=pickle.load(open('pickle_model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    predictions = model.predict(final_features)
    output=round(predictions[0],2)
    return render_template('index.html' , prediction_text="Your annual salary would be : {}".format(math.floor(output)))


if __name__ == "__main__":
    app.run()

