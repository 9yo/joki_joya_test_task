def count_change(target_qty: int, coin_denomination: list) -> set:
    result: set = set()

    def calculate_combinations(tq: int, cd: list, combination=None) -> None:
        for coin in cd:
            if combination is None:
                combination: str = ''
            if tq - coin > 0:
                calculate_combinations(tq - coin, cd, combination + str(coin))
            if tq - coin == 0:
                result.add('+'.join(sorted(combination + str(coin))))

    calculate_combinations(target_qty, coin_denomination)
    if not result:
        return 0
    return len(result), result


if __name__ == '__main__':
    print(count_change(4, [1, 2]))  # 3 (1+1+1+1, 1+1+2, 2+2)
    print(count_change(10, [5, 2, 3]))  # 4 (5+5, 2+3+2+3, 5+2+3, 2+2+2+2+2)
    print(count_change(11, [5, 7]))  # 0
