# initialize function
def find_max(numbers):
    # define max list with 0 value
    maximum = numbers[0]
    # resets value of max when compared with
    # larger number
    for number in numbers:
        if number > maximum:
            maximum = number
    return maximum
