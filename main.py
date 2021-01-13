from tkinter import *

global miles_to_km_converter
miles_to_km_converter = True


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")

def km_to_miles():
    km = float(km_input.get())
    miles = km/1.609
    miles_result_label.config(text=f"{miles}")

def switch():
    global miles_to_km_converter
    #determin true or false
    if miles_to_km_converter == True:
        miles_to_km_converter = False
    else:
        miles_to_km_converter = True



# def switch_converter_True():
#     global miles_to_km_converter
#     miles_to_km_converter = True
#
#
# def switch_converter_False():
#     global miles_to_km_converter
#     miles_to_km_converter = False
window = Tk()




while miles_to_km_converter == True:
    window.title("Miles to Kilometers Converter")
    window.config(padx=26, pady=20)

    miles_input = Entry(width=7)
    miles_input.grid(column=1, row=0)

    miles_label = Label(text="Miles")
    miles_label.grid(column=2, row=0)

    is_equal_label = Label(text="is equal to")
    is_equal_label.grid(column=0, row=1)

    kilometer_result_label = Label(text="0")
    kilometer_result_label.grid(column=1, row=1)

    kilometer_label = Label(text="Km")
    kilometer_label.grid(column=2, row=1)

    calculate_button = Button(text="Calculate", command=miles_to_km)
    calculate_button.grid(column=1, row=2)

    switch_button = Button(text="Switch", command=switch)
    switch_button.grid(column=2, row=2)


while miles_to_km_converter == False:
    window.title("Kilometers to Miles Converter")
    window.config(padx=26, pady=20)

    km_input = Entry(width=7)
    km_input.grid(column=1, row=0)

    km_label = Label(text="Kilometers")
    km_label.grid(column=2, row=0)

    is_equal_label = Label(text="is equal to")
    is_equal_label.grid(column=0, row=1)

    miles_result_label = Label(text="0")
    miles_result_label.grid(column=1, row=1)

    miles_label = Label(text="Miles")
    miles_label.grid(column=2, row=1)

    calculate_button = Button(text="Calculate", command=km_to_miles)
    calculate_button.grid(column=1, row=2)

    switch_button = Button(text="Switch", command=switch)
    switch_button.grid(column=2, row=2)






window.mainloop()





