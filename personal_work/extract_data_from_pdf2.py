import datetime
import math
import pandas as pd
from pdfquery import PDFQuery
import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from datetime import datetime as dt
from tkinter import messagebox


def check_is_digit(string):
    return any(char.isdigit() for char in string)


def read_from_pdf_and_return_dict():
    pdf = PDFQuery(r"C:\Users\Ciprian\Downloads\GABUR.pdf")
    pdf.load()

    page_count = pdf.doc.catalog['Pages'].resolve()['Count']
    days_count = 0
    result_dict = {}
    for p in range(page_count):
        if p > 1:
            days_count += 1
            pdf.load(p)
            text_elements = pdf.pq('LTTextLineHorizontal')
            text = [t.text.rstrip() for t in text_elements if t.text != ''][:len(text_elements) - 7]
            result_dict[f"Ziua {days_count}"] = {}

            masa1 = text[text.index('MASA 1') + 1:text.index('GUSTARE')]
            gustare = text[text.index('GUSTARE') + 1:text.index('MASA 2')]
            masa2 = text[text.index('MASA 2') + 1:]

            for initial_text, text_to_add in [(masa1, "Masa 1"), (gustare, 'Gustare'), (masa2, 'Masa 2')]:
                text_formatted = [elem.strip().lower()
                                  .replace(" nepreparate", "")
                                  .replace(" nepreparat", "")
                                  .replace(" crude", "")
                                  .replace(" crud", "")
                                  .replace(" cantarite", "")
                                  .replace(" cantariti", "")
                                  .replace(" cantarit", "")
                                  .replace(" preparata", "")
                                  .replace(" preparat", "")
                                  .replace(" (facut cu lapte 1.5%)", "")
                                  .replace(" fierte", "")
                                  .replace("rosie", "rosii")
                                  .replace("2 oua", 'oua 2')
                                  .replace("3 oua", "oua 3")
                                  .replace("para", "pere")
                                  .replace("de pui", 'pui')
                                  .replace('omleta din ', '')
                                  .replace(" dupa gust", '')
                                  .replace(' la alegere', '')
                                  .replace("pulpa", "pulpe")
                                  .replace("cartofi la cuptor", "cartofi")
                                  .replace("piure de cartofi", 'cartofi')
                                  .replace("dulcii", 'dulci')
                                  .replace('mazarea(conserva)', 'mazare')
                                  .replace("salta", 'salata')
                                  for elem in " ".join(initial_text).split("*") if elem != '']
                result_dict[f"Ziua {days_count}"][text_to_add] = text_formatted
    return result_dict


def create_window():

    def write_to_textbox(textbox, text_to_write):
        textbox.insert(tk.END, text_to_write)

    def clear_text_box(textbox):
        textbox.delete("1.0", tk.END)

    def select_date():
        [clear_text_box(textbox) for textbox in [output_text_days, output_text_shopping_list]]

        result = read_from_pdf_and_return_dict()
        # print('\n' * 100)
        day_0 = dt.strptime("05-06-2023", "%d-%m-%Y")

        start_date = dt.strptime(cal1.get_date(), "%d-%m-%Y")
        ending_date = dt.strptime(cal2.get_date(), "%d-%m-%Y")

        days_from_start = start_date - day_0
        delta_time = ending_date - start_date

        if delta_time.days < 0:
            messagebox.showerror("Error", "Please select a date higher than starting date!")
        else:
            values_list = []
            for i in range(delta_time.days + 1):
                day_nr = ((i + days_from_start.days) % 14) + 1
                date = start_date + datetime.timedelta(days=i)
                write_to_textbox(output_text_days, f"Ziua {date.strftime('%d-%m-%Y')} {result[f'Ziua {day_nr}']}\n\n")
                for value in result[f'Ziua {day_nr}'].values():
                    values_list += value

            food_quantity = {}

            for value in values_list:
                unit = ''
                count = ''
                split_value = value.split()
                food_name = " ".join(split_value[:-1])
                if check_is_digit(split_value[-1]):
                    for char in split_value[-1]:
                        count, unit = (count + char, unit) if check_is_digit(char) else (count, unit + char)
                    if " ".join(split_value[:-1]) in food_quantity:
                        try:
                            food_quantity[food_name][0] += int(count) * 2
                        except TypeError:
                            print('hey')
                        finally:
                            pass
                    else:
                        food_quantity[food_name] = [int(count) * 2, unit if unit else 'buc']
                else:
                    if value not in food_quantity:
                        food_quantity[value] = ['', '']

            for key, value in food_quantity.items():
                write_to_textbox(output_text_shopping_list, f"{key} {' '.join(str(char) for char in value)}\n")

    root = tk.Tk()
    root.title(f"Diet/Day traceability")

    # Create a calendary for starting day
    cal1 = Calendar(root, selectmode="day", date_pattern="dd-mm-yyyy")
    cal1.grid(row=0, column=0)

    # Create a calendary for ending day
    cal2 = Calendar(root, selectmode="day", date_pattern="dd-mm-yyyy")
    cal2.grid(row=0, column=3)

    # Create a text box
    output_text_days = tk.Text(root, height=20, width=30)
    output_text_days.grid(row=2, column=0, padx=10, pady=10)

    # Create a text box
    output_text_shopping_list = tk.Text(root, height=20, width=30)
    output_text_shopping_list.grid(row=2, column=3, padx=10, pady=10)

    select_button = tk.Button(root, text="Select ending Date", command=select_date)
    select_button.grid(row=1, column=2)

    root.mainloop()


create_window()
