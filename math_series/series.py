

def fibonacci(n: int):
    """
    # as recursive :

    other basic solution without dictionary
    if n == 0 or n == 1:
        return n
    return

    return (fibonacci(n-1)+fibonacci(n-2))"""

    # As Iteration :
    # ->this one is better cuz its alot faster than recalling + you can save on dictionary multiple runs; idea taken from https://www.youtube.com/watch?v=lnF_9hXD05k

    try:
        base_condition = {0: 0, 1: 1}
        for i in range(2, n+1):
            base_condition[i] = base_condition[i-1]+base_condition[i-2]
        return (base_condition[n])
    except:
        return ("wrong entry")

# _______________________________________________________________________________


def lucas(n: int):
    try:
        base_condition = {0: 2, 1: 1}

        for i in range(2, n+1):
            base_condition[i] = base_condition[i-1]+base_condition[i-2]

        return (base_condition[n])
    except:
        return "wrong entry"

# _______________________________________________________________________________

# Notice this function since its recursive it only takes from 0<=n<=100
# anything above 35 nth will take more than 40 sec and exponentially increases with the nth number increase ex: @40nth take 1 minute, @ 50 nth takes 4 minutes!


def sum_series(n: int, condition_1=0, condition_2=1):
    try:
        if type(n) is not int or n < 0:
            raise TypeError("That is not an integer number!")
        if n == 0:
            return condition_1
        elif n == 1:
            return condition_2
        else:
            return sum_series(n-1, condition_1, condition_2) + sum_series(n-2, condition_1, condition_2)
    except TypeError:
        return "wrong entry"


# print(fibonacci(11))
# print("#")
# print(lucas(937))
# print("#")
# print(sum_series(-40, 7, 4))
