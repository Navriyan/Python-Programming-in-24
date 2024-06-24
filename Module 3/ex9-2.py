def get_odds():
    for number in range(10):
        if number % 2 != 0:
            yield number

# Using the generator function and printing the third value
count = 0
for odd in get_odds():
    count += 1
    if count == 3:
        print(odd)  # This will print the third odd number
        break