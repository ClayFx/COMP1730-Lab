## COMP1730/6730 S2 2019 - Homework 5
# Submission is due 11:55pm, Monday the 30th of September, 2019.

## YOUR ANU ID: u6234544
## YOUR NAME: Xuan Feng

## Implement the function interpolate below.
## (The statement "pass" is just a placeholder that does nothing: you
## should replace it.)
## You can define other functions if it helps you decompose the problem
## and write a better organised and/or more readable solution.

def interpolate(x, y, x_test):
    """

    :param x:
    :param y:
    :param x_test:
    :return:
    """
    for index in range(len(x)):
        if x[index] == x_test:
            return y[index]
        elif x[index] < x_test and x[index+1] > x_test:
            x1 = x[index]
            x2 = x[index + 1]
            y1 = y[index]
            y2 = y[index + 1]
            res = (y2-y1)/(x2-x1)*(x_test-x1)+y1
            return res





def test_interpolate():
    '''
    This function runs a number of tests of the interpolate function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 2.0) == 5.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 4.0) == 17.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 1.25) == 2.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 2.5) == 7.0

    # test that we get the right answer when x_test is exactly one
    # of the sample points:
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 1) == 1.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 3) == 9.0
    assert interpolate([1.0, 3.0, 5.0], [1.0, 9.0, 25.0], 5) == 25.0

    # we should get the same answer also if only the two adjacent
    # sample points are given:
    assert interpolate([1.0, 3.0], [1.0, 9.0], 2.0) == 5.0
    assert interpolate([3.0, 5.0], [9.0, 25.0], 4.0) == 17.0

    print("all tests passed")
    
