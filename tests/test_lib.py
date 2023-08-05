from services_test4 import lib


def test_hello_world() -> None:
    input_msg = "hello world"
    actual = lib.hello_world(input_msg)
    expected = "HELLO WORLD"
    assert actual == expected
