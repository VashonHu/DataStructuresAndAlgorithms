def fast_expt(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return fast_expt(b * b, n / 2)
    else:
        return b * fast_expt(b * b, n / 2)

def square(a):
    return a * a

def fast_expt2(b, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        return square(fast_expt2(b, n / 2))
    else:
        return b * fast_expt(b, n - 1)

if __name__ == "__main__":
    print fast_expt2(10, 3)