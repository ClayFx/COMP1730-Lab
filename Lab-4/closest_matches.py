def smallest_greater(seq, value):
    differece = max(seq)
    result = None
    for i in seq:
        if i >= value and (i - value) <= differece:
            result = i
            differece = i-value
    return result



def greatest_smaller(seq, value):
    differece = min(seq)
    result = None
    for i in seq:
        if i < value and (i - value) >= differece:
            result = i
            differece = i-value
    return result