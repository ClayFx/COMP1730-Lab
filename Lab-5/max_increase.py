# COMP1730/6730 S2 2019 - Homework 4
# Submission is due 11:55pm, Monday the 23rd of September, 2019.

# YOUR ANU ID: u6234544
# YOUR NAME: Xuan Feng

# Implement the function max_increase below.
# (The statement "pass" is just a placeholder that does nothing: you
# should replace it.)
# You can define other functions if it helps you decompose the problem
# and write a better organised and/or more readable solution.

def max_increase(seq):
    index = 0 # The index of the starting element in the increasing sequence
    highest_increase = 0 # The max increase value
    for i in range(1, len(seq)):
        this_increase = seq[i] - seq[index] # To calculate the increase value so far
        if this_increase > 0:
            if this_increase > highest_increase:
                highest_increase = this_increase # To record the max increase value
        else:
            index = i # Once the sequence starts to
    return highest_increase



def test_max_increase():
    '''
    This function runs a number of tests of the max_increase function.
    If it works ok, you will just see the output ("all tests passed") at
    the end when you call this function; if some test fails, there will
    be an error message.
    '''

    assert max_increase([]) == 0.0, "empty list has no pair";
    assert max_increase([1]) == 0.0, "size-1 list has no pair";
    assert max_increase((1,2,3,2)) == 2.0;
    assert max_increase([1.0,3.0,1.0,2.0]) == 2.0;
    assert max_increase([3,-1,2,1]) == 3.0;
    assert max_increase([3,2,1,1]) == 0.0, "no increasing pair";
    assert max_increase([226, 264, 337, 364, 485, 529, 482]) == 303.0;

    btc_data = [ 6729.44, 6690.88, 6526.36, 6359.98, 6475.89, 6258.74,
                 6485.10, 6396.64, 6579.00, 6313.51, 6270.20, 6195.01,
                 6253.67, 6313.90, 6233.10, 6139.99, 6546.45, 6282.50,
                 6718.22, 6941.20, 7030.01, 7017.61, 7414.08, 7533.92,
                 7603.99, 7725.43, 8170.01, 8216.74, 8235.70, 8188.00,
                 7939.00, 8174.06 ]
    btc_data.reverse()
    assert abs(max_increase(tuple(btc_data))-589.45) < 1e-6;

    print("all tests passed")
