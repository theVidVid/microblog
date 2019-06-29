from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
# Home page route.
def index():
    user = {'username': 'Ian'}
    return render_template('index.html', title='Home', user=user)
