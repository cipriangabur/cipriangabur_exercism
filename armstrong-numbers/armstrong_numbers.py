def is_armstrong_number(number):
    str_num = str(number)
    digit_number = len(str_num)
    return number == sum([int(str(d))**digit_number for d in str_num])
