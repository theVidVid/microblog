from app import app


@app.route('/')
@app.route('/index')
# Home page route.
def index():
    return "Hello, World!"
