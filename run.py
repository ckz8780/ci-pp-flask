import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
                    'index.html',
                    page_heading="Home",
                    template_var="This (home) heading was generated with a template variable (see run.py)",
                    list_of_numbers=[1, 2, 3, 4,5]
                )
    
@app.route('/about')
def about():
    return render_template(
                    'about.html',
                    page_heading="About",
                    template_var="This (about) heading was generated with a template variable (see run.py)"
                )
    
@app.route('/contact')
def contact():
    return render_template(
                    'contact.html',
                    page_heading="Contact",
                    template_var="This (contact) heading was generated with a template variable (see run.py)"
                )
    
@app.route('/careers')
def careers():
    return render_template(
                    'careers.html',
                    page_heading="Careers",
                    template_var="This (careers) heading was generated with a template variable (see run.py)"
                )
    
if __name__ == '__main__':
    app.run(
        host = os.environ.get('IP'),
        port = int(os.environ.get('PORT')),
        debug = True
    )