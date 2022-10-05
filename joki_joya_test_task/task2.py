from typing import Callable


def make_looper(s: str) -> Callable:
    index: int = -1

    def get_letter() -> str:
        nonlocal index
        index += 1
        return s[index % len(s)]

    return get_letter


if __name__ == '__main__':
    abc = make_looper('abc')
    assert abc() == 'a'
    assert abc() == 'b'
    assert abc() == 'c'
    assert abc() == 'a'
