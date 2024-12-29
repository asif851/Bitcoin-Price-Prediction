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
        Open = float(request.form['Open'])
        High = float(request.form['High'])
        Low = float(request.form['Low'])
        Volume = float(request.form['Volume'])
        Month = int(request.form['Month'])
        Day = int(request.form['Day'])
        Year = int(request.form['Year'])
        Daily_Return = float(request.form['Daily_Return'])
        MA_7 = float(request.form['MA_7'])
        MA_30 = float(request.form['MA_30'])
        Volatility_30 = float(request.form['Volatility_30'])

        data = np.array([[Open, High, Low, Volume, Month, Day, Year, Daily_Return, MA_7, MA_30, Volatility_30]])
        my_prediction = model.predict(data)

        return render_template('home.html', prediction=my_prediction)

if __name__ == '__main__':
    app.run()
