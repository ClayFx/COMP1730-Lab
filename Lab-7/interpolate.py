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
    This function computes the linear interpolation of the unknown function f at a new point x_test, by considering
    the closest known points below and above x_test. We assume that x_test is a number, and it is between two values
    in the x sequence, or possibly equal to a value in the sequence.

    :param x: A sample sequence of real numbers. It contains the x_axis value.
    :param y: A sample sequence of real numbers. It contains the y_axis value.
    :param x_test: A new value of x_axis.
    :return: The predicted value of x_test, that is, f(x_test).
    """
    for index in range(len(x)):
        if x[index] == x_test: # x_test equal to the k-th element in sequence x, where k = index.
            return y[index] # The output should be the k-th element in sequence y, where k = index.
        elif x[index] < x_test and x[index+1] > x_test:
            # The following code is to rename the variables so that it is easy to read.
            x_below = x[index]
            y_below = y[index]
            x_above = x[index + 1]
            y_above = y[index + 1]
            # This is the arithmetical solution of y': draw a line between (x_below, y_below) and (x_above, y_above),
            # then take the value where this line is at x_test.
            res = (y_above - y_below) / (x_above - x_below) * (x_test - x_below) + y_below
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
    
