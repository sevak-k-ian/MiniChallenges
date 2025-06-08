#################################
# Program must get from user a lower and upper bound
# Then generate a random whole number between this 2 bounds
#################################
# Get lower and upper bound
while True:
    try:
        user_input: str = input(
            "Enter a lower and upper bound, separated by whitespace :"
        )
        # Convert input string to two integers: lower and upper
        lower, upper = list(map(int, user_input.strip().split()))
        if lower < upper:
            break
        print("Lower bound must be smaller than upper bound")
    except ValueError:
        print("Please input int number!")

# Generate random number
from random import randrange

random_num: int = randrange(lower, upper + 1)

print(random_num)
