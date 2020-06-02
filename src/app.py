from flask import Flask, render_template

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')