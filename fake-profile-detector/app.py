from flask import Flask, render_template, request
from transformers import pipeline
from PIL import Image
import os

app = Flask(__name__)

# Load pre-trained model
text_analyzer = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    bio = request.form['bio']
    image = request.files['image']

    # Basic image validation
    try:
        img = Image.open(image)
        img.verify()
    except Exception as e:
        return render_template('result.html', verdict="Invalid image")

    # Text analysis
    result = text_analyzer(bio)[0]
    verdict = "FAKE" if result['label'] == 'NEGATIVE' else "REAL"

    return render_template('result.html', verdict=verdict)

if __name__ == '__main__':
    app.run(debug=True)