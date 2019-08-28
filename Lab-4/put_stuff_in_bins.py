def count_in_bin(values, lower, upper):
    counter = 0
    for ele in values:
        if lower < ele and ele <= upper :
            counter +=1
    return counter

def histogram(values, dividers):
    res = []
    new_dividers = [0]
    new_dividers.extend(dividers)
    new_dividers.append(float('inf'))
    for i in range(len(new_dividers)-1):
        lower = new_dividers[i]
        upper = new_dividers[i+1]
        res.append(count_in_bin(values, lower, upper))
    return res