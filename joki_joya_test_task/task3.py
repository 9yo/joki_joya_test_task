def is_merge(s: str, part1: str, part2: str) -> bool:
    return sorted(s) == sorted(part1 + part2)


if __name__ == '__main__':
    assert is_merge('helloworld', 'hello', 'world') is True
    assert is_merge('helloworld', 'how', 'ellorld') is True
    assert is_merge('helloworld', 'hell', 'world') is False
    assert is_merge('helloworld', 'ehll', 'world') is False
