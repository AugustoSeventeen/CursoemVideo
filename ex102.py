# Factorial


def factorial(n, show=False):
    """
    -> To calculate a Factorial
    :param n: The number to be calculated as factorial
    :param show: (Optional) Show or not the account
    :return: The factorial value of  n number
    """
    account = 1
    for value in range(n, 0, -1):
        account *= value
        if show:
            print(f'{value}', end='')
            if value > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
    return f'{account}'


print(factorial(5, show=True))
