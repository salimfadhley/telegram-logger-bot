from client.config import get_config


def test_config():
    c = get_config()
    assert(c)
