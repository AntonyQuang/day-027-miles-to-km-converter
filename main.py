from tkinter import *


def convert():
    miles = float(miles_input.get())
    km = round(miles/0.62137, 2)
    output_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

output_label = Label(text="0")
output_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=convert)
calculate_button.grid(column=1, row=2)

window.mainloop()