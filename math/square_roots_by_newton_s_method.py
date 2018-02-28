def square_root(x):
    guess = 1.0
    next_guess = improve_guess(x, guess)
    while abs(x - guess * guess) > 0.1:
        guess = next_guess
        next_guess = improve_guess(x, guess)
    return guess


def improve_guess(x, guess):
    return (x / guess + guess) / 2.0


if __name__ == "__main__":
    print(square_root(5))
