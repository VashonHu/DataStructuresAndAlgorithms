def exponentaion(x, n):
    if n == 0:
        return 1

    if n % 2 == 0:
        return exponentaion(x * x, n / 2)
    else:
        return exponentaion(x * x, n / 2) * x

if __name__ == "__main__":
    print exponentaion(2, 3)