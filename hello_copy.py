# New Comment for Github demo
# New Comment for bigfeature branch demo + second try
# New Comment for littlefeature demo
# The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep #in.

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if # we are in trouble.

def monkey_trouble(a_smile, b_smile):
    if (a_smile and b_smile) or (not a_smile and not b_smile):
        return True
    else:
        return False
    
#Given two int values, return their sum. Unless the two values are the same, then return double their sum

def addition_or_double(a, b):
    if a != b:
        return a + b
    else:
        return (a+b) * 2

def diff21(n):
    if n > 21:
        return (n - 21) * 2
    else:
        return 21 - n
    
def diff21(n):
    if n<=21:
        return 21 - n
    else:
        return (n-21) * 2