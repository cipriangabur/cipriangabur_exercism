def print_formatted(number):
    text = ''
    twos_length = len(bin(number)[2:])
    print(twos_length)
    for i in range(number):
        dec = str(i+1).rjust(twos_length)
        octal = oct(i+1)[2:].rjust(twos_length)
        hexa = hex(i+1)[2:].upper().rjust(twos_length)
        binar = bin(i+1)[2:].rjust(twos_length)
        text += " ".join(x.rjust(twos_length) for x in [dec, octal, hexa, binar]) + "\n"
    print(text)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)