from ci_flask_docker_test.db_interaction import get_cursor_to_database, get_number_items


def test_db_interaction():
    assert get_cursor_to_database()


def test_default_items_table():
    assert get_number_items() == 3
