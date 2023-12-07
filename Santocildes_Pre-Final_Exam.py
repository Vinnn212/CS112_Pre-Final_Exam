def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    try:
        lower = int(input("Enter a starting digit: "))
        if lower < 0:
            print("You must enter a non-negative integer!")
            print()
            continue
        if lower == 0:
            print("Invalid. Please try again.")
            break
    except ValueError:
        print("Invalid! Enter a integer number!")
        continue

    while True:
        try:
            upper = int(input("Enter the ending digit: "))
            if upper <= lower:
                print("You must enter an integer greater than", lower)
                continue
        except ValueError:
            print("You must enter a Integer number!")
            continue
        break

    print("Prime numbers between", lower, "and", upper, "are:")

    for num in range(lower, upper + 1):
        if is_prime(num):
            print(num)
