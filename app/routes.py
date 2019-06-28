from app import app


@app.route('/')
@app.route('/index')
# Home page route.
def index():
    user = {'username': 'Ian'}
    return """
<html>
    <head>
        <title>Home Page - Microblog</title>
    <head>
    <body>
        <h1>Hello, """ + user['username'] + """!</h1>
    </body>
</html>"""
