from tkinter import *
from tkinter import ttk
root = Tk()
root.title("BMI Calculator - The Pycodes")
root.geometry("470x580")
root.resizable(False, False)
root.configure(bg="silver")
def calculate_bmi():
    height = float(height_var.get())
    weight = float(weight_var.get())
    meters_height = height / 100
    bmi = round(weight / (meters_height ** 2), 1)
    bmi_label.config(text=f"BMI: {bmi}")

    if bmi < 18.5:
        status_label.config(text="Underweight")
        advice_label.config(text="You have lower weight than normal \n body.")
    elif 18.5 <= bmi <= 25:
        status_label.config(text="Normal")
        advice_label.config(text="You are healthy.")
    elif 25 < bmi <= 30:
        status_label.config(text="Overweight")
        advice_label.config(text="You are slightly obese.")
    else:
        status_label.config(text="Obese")
        advice_label.config(text="Your health might be at risk if you \n don't lose weight.")
Label(root, width=72, height=5, bg="white").pack(side=TOP)
Label(root, text="BMI CALCULATOR", font="arial 17 bold", bg="orange").place(x=130, y=20)
Label(root, width=72, height=18, bg="pink").pack(side=BOTTOM)
Label(root, text="HEIGHT(cm)", font="arial 14 bold", bg="gold").place(x=80, y=100)
Label(root, text="W(kg)", font="arial 14 bold", bg="gold").place(x=300, y=100)
height_var = StringVar()
weight_var = StringVar()
Entry(root, textvariable=height_var, width=5, font="arial 50", bg="grey", bd=0, justify=CENTER).place(x=35, y=160)
Entry(root, textvariable=weight_var, width=5, font="arial 50", bg="grey", bd=0, justify=CENTER).place(x=255, y=160)
current_height_value = DoubleVar()
current_weight_value = DoubleVar()
def slider_changed_height(event):
    height_var.set('{:.2f}'.format(current_height_value.get()))

def slider_changed_weight(event):
    weight_var.set('{:.2f}'.format(current_weight_value.get()))


style = ttk.Style()
style.configure("TScale", background="silver")

slider_height = ttk.Scale(root, from_=0, to=220, orient=HORIZONTAL, style="TScale",
command=slider_changed_height, variable=current_height_value)
slider_height.place(x=80, y=250)
slider_weight = ttk.Scale(root, from_=0, to=200, orient=HORIZONTAL, style="TScale",
command=slider_changed_weight, variable=current_weight_value)
slider_weight.place(x=300, y=250)
height_var.set('{:.2f}'.format(current_height_value.get()))
weight_var.set('{:.2f}'.format(current_weight_value.get()))
Button(root, text="Calculate BMI", width=15, height=2, font="arial 10 bold", bg="green", fg="white",
command=calculate_bmi).place(x=170, y=340)

bmi_label = Label(root, font="arial 50 bold", bg="lightblue", fg="black")
bmi_label.place(x=85, y=305)
status_label = Label(root, font="arial 20 bold", bg="lightblue", fg="black")
status_label.place(x=185, y=430)
advice_label = Label(root, font="arial 10 bold", bg="lightblue", fg="black")
advice_label.place(x=125, y=500)
root.mainloop()
