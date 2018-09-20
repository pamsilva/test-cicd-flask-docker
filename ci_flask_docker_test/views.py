from ci_flask_docker_test import app


@app.route('/', methods=['GET'])
def root():
    return '<h1>Root Hello World !</h1>'


@app.route('/hello', methods=['GET'])
def hello():
    return '<h1>Hello World !</h1>'
