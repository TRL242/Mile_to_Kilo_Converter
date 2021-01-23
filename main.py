from tkinter import *



#==========================Functions=================================#
def miles_to_km():
    miles = float(unit1_input.get())
    km = miles * 1.609
    unit2_result.config(text=f"{km}")

def km_to_miles():
    km = float(unit1_input.get())
    miles = km/1.609
    unit2_result.config(text=f"{miles}")

def switch_miles_to_km():
    global window_title
    window_title="Kilometers to Miles Converter"
    window.title(window_title)
    unit1_label.config(text="KM")
    unit1_input.delete(0, END)
    unit2_label.config(text="Miles")
    unit2_result.config(text="0")
    calculate_button.config(text="Calculate", command=km_to_miles)
    switch_button.config(text="Switch", command=switch_km_to_miles)



def switch_km_to_miles():
    global window_title
    window_title="Miles to Kilometers Converter"
    window.title(window_title)
    unit1_label.config(text="Miles")
    unit1_input.delete(0, END)
    unit2_label.config(text="KM")
    unit2_result.config(text="0")
    calculate_button.config(text="Calculate", command=miles_to_km)
    switch_button.config(text="Switch", command=switch_miles_to_km)


#==========================UX=================================#
window = Tk()
window_title = "Miles to Kilometers Converter"
window.title(window_title)
window.config(padx=46, pady=40)

unit1_input = Entry(width=7)
unit1_input.grid(column=1, row=0)
unit1_input.focus()

unit1_label = Label(text="Miles")
unit1_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

unit2_result = Label(text="0")
unit2_result.grid(column=1, row=1)

unit2_label = Label(text="KM")
unit2_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

switch_button = Button(text="Switch", command=switch_miles_to_km)
switch_button.grid(column=2, row=2)



window.mainloop()





