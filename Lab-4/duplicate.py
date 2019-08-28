def count_duplicates(seq):
    counter = 0
    for i in range(0, len(seq)):
        if seq[i] in seq[i+1:]:
            counter += 1
    return counter

