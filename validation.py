import builtins
from typing import Callable


def input(
    prompt: str,
    type: type = str,
    validator: Callable[[str], bool] = lambda _: True,
    invalid_message: str = "Invalid input.",
):
    while True:
        i = builtins.input(prompt)
        if validator(i):
            return type(i)
        else:
            print(invalid_message)
