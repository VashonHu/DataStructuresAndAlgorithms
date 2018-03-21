def fib_iter(a, b, count, sum):
    sum += b
    if count == 0:
        print(sum)
    else:
        fib_iter(a + b, a, count - 1, sum)


def fib(n):
    fib_iter(1, 0, n, 0)


def fib2(n):
    a = 1
    b = 1
    sum = a + b
    for x in range(n - 2):
        next = a + b
        sum += next
        a = b
        b = next

    return sum


def fib3(n):
    a, b = 0, 1

    if n < 1:
        return a
    else:
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    print(fib(5))

    # print fib2(5)
    # i = 1
    # for i, j in enumerate(range(1, 10)):
    #     print i, j
