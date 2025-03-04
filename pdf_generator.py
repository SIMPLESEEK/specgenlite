from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def generate_pdf():
    return render_template('index.html')
