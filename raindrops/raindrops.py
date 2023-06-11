def convert(number):
    text_added = [text for div_number, text in [(3, "Pling"), (5, "Plang"), (7, "Plong")]
                  if number % div_number == 0]
    return "".join(text_added) if len(text_added) else str(number)

