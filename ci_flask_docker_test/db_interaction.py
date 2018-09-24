import psycopg2


def get_cursor_to_database():
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="postgres"
    )

    return connection.cursor()


def _iter_get_items(cursor):
    cursor.execute('select * from items')

    res = cursor.fetchone()
    while res is not None:
        yield res
        res = cursor.fetchone()


def _item_to_dict(item):
    return {
        'id': item[0],
        'name': item[1],
        'count_freq': item[2],
        'description': item[3]
    }


def get_items():
    cursor = get_cursor_to_database()
    return (_item_to_dict(x) for x in _iter_get_items(cursor))


def get_number_items():
    cursor = get_cursor_to_database()
    cursor.execute("select count(1) from items")
    res = cursor.fetchone()
    return res[0]
