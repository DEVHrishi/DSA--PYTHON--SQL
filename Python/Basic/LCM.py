def compute_LCM(x, y):
    if (x > y):
        greater = x
    else:
        greater = y
    while (True):
        if ((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm


print(compute_LCM(54, 24))

# another approach

# Python program to find the L.C.M. of two input number

# This function computes GCD


def compute_gcd(x, y):

    while (y):
        x, y = y, x % y
    return x

# This function computes LCM


def compute_lcm(x, y):
    lcm = (x*y)//compute_gcd(x, y)
    return lcm


num1 = 54
num2 = 24

print("The L.C.M. is", compute_lcm(num1, num2))
