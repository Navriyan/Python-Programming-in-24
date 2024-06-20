guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif number == guess_me:
        print('found it!')
        break  # to exit loop
    else:
        print('oops')
        break  
    number += 1  
    