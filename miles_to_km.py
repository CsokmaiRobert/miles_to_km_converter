from tkinter import *

window = Tk()
window.title("Kilometers to miles calculator")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)


def button_click():
    input_number = int(input_km.get())
    input_number = float(input_number * 0.621371)
    input_number = round(input_number, 2)
    number_miles.config(text=input_number)


input_km = Entry(width=10)
input_km.grid(column=1, row=0)

text_km = Label(text="KM", font=("Arial", 15))
text_km.grid(column=2, row=0)

text = Label(text="is equal to", font=("Arial", 15))
text.grid(column=0, row=1)

number_miles = Label(text="", width=10, font=("Arial", 15))
number_miles.grid(column=1, row=1)

text_miles = Label(text="Miles", font=("Arial", 15))
text_miles.grid(column=2, row=1)

button = Button(text="Calculate", command=button_click)
button.grid(column=1, row=2)


window.mainloop()
