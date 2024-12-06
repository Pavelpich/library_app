from ..src.json_db_handler import JsonDBNode

def test_jsonbnode():
    new_json_db = JsonDBNode()

    new_json_db.load_books()

    new_json_db.add_record("abc")


if __name__ == "__main__":
    test_jsonbnode()