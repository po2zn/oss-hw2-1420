def digit_sum(n):
    """n의 각 자리 숫자를 모두 더한다."""
    total = 0
    for ch in str(n):
        total += int(ch)
    return total


def lucky_number(n):
    """한 자리 수가 될 때까지 각 자리 숫자를 더한다."""
    while n >= 10:
        n = digit_sum(n)
    return n
