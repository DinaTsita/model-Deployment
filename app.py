from flask import Flask, render_template, request
from predict import predict_url
from url_processor import process_url
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    url_input = request.form['user_input']
    features = process_url(url_input)
    prediction = predict_url(features)
    return prediction 

    #return render_template('index.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)