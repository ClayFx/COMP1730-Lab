def sum_odd_digits(number):
    if number <= 0:
        raise Exception("Inout Error")
    sum = 0
    for i in str(number):
        if int(i) % 2 == 1:
            sum += int(i)
    print(sum)



def sum_even_digits(number):
    if number <= 0:
        raise Exception("Inout Error")
    sum = 0
    for i in str(number):
        if int(i) % 2 == 0:
            sum += int(i)
    print(sum)



def sum_all_digits(number):
    if number <= 0:
        raise Exception("Inout Error")
    sum = 0
    for i in str(number):
        sum += int(i)
    print(sum)