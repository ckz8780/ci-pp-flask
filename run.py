import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', page_heading="Home")
    
@app.route('/about')
def about():
    return render_template('about.html', page_heading="About")
    
@app.route('/contact')
def contact():
    return render_template('contact.html', page_heading="Contact")
    
@app.route('/careers')
def careers():
    return render_template('careers.html', page_heading="Careers")
    
if __name__ == '__main__':
    app.run(
        host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True
    )