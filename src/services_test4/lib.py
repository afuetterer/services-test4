"""The functions in this project library."""


def hello_world(msg: str) -> str:
    """Uppercases a message string.

    The given message string will be uppercased and then returned.

    Args:
        msg: A message.

    Returns:
        An uppercase version of the input message.

    """
    result = msg.upper()
    print(result)
    print(result)
    return result
