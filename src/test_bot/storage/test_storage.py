from io import BytesIO, StringIO

from bot.storage import store_object, get_bucket


def test_store_object():
    data = BytesIO("hello".encode("utf-8"))
    store_object(file_obj=data, file_name="world")
    result = BytesIO()
    get_bucket().download_fileobj("world", result)
    assert result.getvalue().decode("utf-8") == "hello"
