from flask import Flask, render_template

import os

app = Flask(__name__,
            template_folder='templates',
            static_folder='static',
            static_url_path='/')


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
