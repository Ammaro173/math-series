from math_series.series import fibonacci, lucas, sum_series

#  can my test be a function ?!?! like my recusion vs you recursion?


# test for basic conditions
def test_fibonacci_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


# Test for Decimals Handling
def test_fibonacci_1():
    actual = fibonacci(1.5)
    expected = "wrong entry"
    assert actual == expected


# Test for Negative Number Handling():
def test_fibonacci_2():
    actual = fibonacci(-10)
    expected = "wrong entry"
    assert actual == expected


# Test For Huge Numbers , Usually for recusrsion  there is limit for the input up to 40 only {1<=n<=40} value take form https://www.quora.com/What-is-the-1000th-term-of-the-Fibonacci-sequence
def test_fibonacci_3():
    actual = fibonacci(1000)
    expected = 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875
    assert actual == expected

# _______________________________________________________________________________

# test for basic conditions


def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


# Test for Decimals Handling
def test_lucas_1():
    actual = lucas(7.5)
    expected = "wrong entry"
    assert actual == expected


# Test for Decimals Handling
def test_lucas_2():
    actual = lucas(-20)
    expected = "wrong entry"
    assert actual == expected


# Test For Huge Numbers , Usually!! for recusrsion  there is limit for the input up to 40 only {1<=n<=40} value taken from https://www.quora.com/What-is-the-1000th-term-of-the-Fibonacci-sequence
def test_lucas_3():
    actual = lucas(937)
    expected = 6628555764166198810401445673527978611217589224031851258090071914073578778192243304726549453695640982677889887422342222622343013298810018847230068744346015774236200571634037230479880928176469417521
    assert actual == expected

# _______________________________________________________________________________


# should return febo @ 0
def test_sum_series_0():
    actual = sum_series(0)
    expected = 0
    assert actual == expected


# should return febo @ 11
def test_sum_series_1():
    actual = sum_series(11)
    expected = 89
    assert actual == expected


# should return lucas @ 7
def test_sum_series_2():
    actual = sum_series(11, 2, 1)
    expected = 199
    assert actual == expected


# should return wrong entry for either decimal or negative for any series
def test_sum_series_3():
    actual = sum_series(-30, 9, 5)
    expected = "wrong entry"
    assert actual == expected
