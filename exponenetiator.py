def exponentiate(x,y):
    """Returns arg1 raised to arg2."""

    return (x ** y)
print(exponentiate.__doc__)

def raise_to_fourth(num1):
    return exponentiate(num1,4)
print(raise_to_fourth(4))

def exponentiator(exponent):
    def raise_x(x):
        return x ** exponent
    return raise_x


square = exponentiator(2)
print(square(2))
cube = exponentiator(3)
print(cube(2))
raise_to_fourth_power = exponentiator(4)
print(raise_to_fourth_power(2))






