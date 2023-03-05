if __name__ == '__main__':
    s = input()
    for action in ["isalnum", "isalpha", "isdigit", "islower", "isupper"]:
        print(eval(f"\"{s}\".{action}()"))
