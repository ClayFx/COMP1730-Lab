def find_element(sequence, element):
    i = 0
    while sequence[i] != element:
        if i < len(sequence):
           i = i + 1
    i = i + 1
    return i
