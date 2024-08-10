import random
import string


def random_string_generator(size=5, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

"""
chars=string.ascii_lowercase + string.digits:

This is another keyword argument that defines the pool of characters from which the random string will be generated.
string.ascii_lowercase includes all lowercase letters ('abcdefghijklmnopqrstuvwxyz').
string.digits includes all decimal digits ('0123456789').
The expression string.ascii_lowercase + string.digits concatenates these two strings, resulting in a pool of characters 
that includes all lowercase letters and digits ('abcdefghijklmnopqrstuvwxyz0123456789').
If no chars argument is provided when calling the function, the function will use this combined string as the pool of characters.

How It Works

Random Character Selection:

random.choice(chars) is used to randomly select a single character from the chars pool.

String Construction:

The function uses a list comprehension inside the ''.join() method to generate a string.
''.join() concatenates the randomly chosen characters into a single string.
The list comprehension iterates size times (for x in range(size)), selecting a random character each time and forming a list of these characters.
The ''.join() method then combines this list of characters into a single string.

"""