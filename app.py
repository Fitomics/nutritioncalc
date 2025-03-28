from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='./')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory(os.path.dirname(os.path.abspath(__file__)), filename)

if __name__ == '__main__':
    app.run(debug=True)
