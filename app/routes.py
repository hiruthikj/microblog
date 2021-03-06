from . import app


@app.route("/")
@app.route("/index")
def index():
    user = {
        'username': '007',
    }
    return '''
    <!DOCTYPE html>
    <html>
        <head>
            <title>MicroBlog</title>
        </head>
        <body>
            <h1>Hello''' + user['username'] + '''!</h1>
        </body>
    </html>
    '''
