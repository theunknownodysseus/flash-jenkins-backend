import os
from flask import Flask, render_template

# Get the parent directory (flask-jenkins root) for templates
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)