from ci_flask_docker_test import app
from ci_flask_docker_test.db_interaction import get_items


@app.route('/', methods=['GET'])
def root():
    return '<h1>Root Hello World !?</h1>'


@app.route('/hello', methods=['GET'])
def hello():
    return '<h1>Hello World !?</h1>'


@app.route('/items', methods=['GET'])
def items():
    the_items = get_items()

    def make_presentable(item_dict):
        return '<li>{name} - {description} </li>\n'.format(**item_dict)

    return '<h2>The items</h2><ol>{}</ol>'.format(
        '\n'.join(
            map(make_presentable, the_items)
        )
    )
