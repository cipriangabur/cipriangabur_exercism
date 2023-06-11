def response(hey_bob):
    if hey_bob.strip() == "":
        return "Fine. Be that way!"
    elif hey_bob.strip()[-1] == "?" and not hey_bob.isupper():
        return "Sure."
    elif hey_bob.isupper():
        if hey_bob.strip()[-1] == "?":
            return "Calm down, I know what I'm doing!"
        else:
            return "Whoa, chill out!"
    else:
        return "Whatever."
