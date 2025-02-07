import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('pickle.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Open=float(request.form['Open'])
        High = float(request.form['High'])
        Low = float(request.form['Low'])
        Volume = float(request.form['Volume'])
        MA_7day = float(request.form['7-day-MA'])
       


        data = np.array([[ Open,High, Low, Volume, MA_7day]])
        my_prediction = model.predict(data)

        return render_template('home.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run(debug=True)
