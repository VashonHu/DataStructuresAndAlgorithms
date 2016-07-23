def nextPrimary(n):
    if  n % 2 == 0:
        n += 1
    while True:
        noPrimary = 0
        for i in range(3, n / 2 + 1, 2):
            if n % i == 0:
                noPrimary = 1
                break
        if not noPrimary:
            return n
        else:
            n += 2

if __name__ == "__main__":
    pass