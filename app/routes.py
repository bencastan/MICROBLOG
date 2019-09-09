from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/benc')
def benc():
    return "Hello Benc"