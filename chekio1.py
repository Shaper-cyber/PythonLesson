def nearest_value(values: set, one: int) -> int:
    b = sorted(values)
    a = [i - one for i in b]
    for k, i in enumerate(a):
        if i == 0:
            return b[k]
    for k, i in enumerate(a):
        if i >= -1 and i <= 1:
            return b[k]
    for k, i in enumerate(a):
        if i > 1:
            return b[k]
    reversed(a)
    for k, i in enumerate(a):
        if i < -1:
            return b[-(k + 1)]


if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    assert nearest_value({1, 2, 3, 4, 5, 6, 7}, 2) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
