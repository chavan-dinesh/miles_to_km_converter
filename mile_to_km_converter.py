from tkinter import *


#function
def miles_to_km():
    miles = input.get()
    km = round(float(miles) * 1.60934)
    result.config(text=f"{km}")


window = Tk()
window.minsize(height=100, width=300)
window.title("Miles to Km Converter")
window.config(padx=30, pady=30)
#input
input = Entry(width=10)
input.grid(column=1, row=0)


#Label 1
mile_label = Label(text="Miles")
mile_label.grid(column=2, row=0)

#Label 2
label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

#Result in KM
result = Label(text="0")
result.grid(column=1, row=1)

# Label 3
label3 = Label(text="Km")
label3.grid(column=2, row=1)

#Button
calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=2)

window.mainloop()