import tkinter
from tkinter import *
from tkinter import messagebox


val = ""
A = 0
operator = "+"

def button_1_isclicked():
    global val
    val = val + "1"
    data.set(val)

def button_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def button_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def button_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def button_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def button_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def button_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def button_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def button_9_isclicked():
    global val
    val = val + "9"
    data.set(val)

def button_0_isclicked():
    global val
    val = val + "0"
    data.set(val)

def button_plus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)

def button_minus_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)

def button_mul_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)

def button_div_isclicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def button_c_isclicked():
    global A
    global operator
    global val
    val = ""
    A = 0
    operator = ""
    data.set(val)

def result():
    global A
    global operator
    global val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        c = A + x
        data.set(c)
        val = str(c)
    elif operator == "-":
        x = int((val2.split("-")[1]))
        c = A - x
        data.set(c)
        val = str(c)
    elif operator == "*":
        x = int((val2.split("*")[1]))
        c = A * x
        data.set(c)
        val = str(c)
    elif operator == "/":
        x = int ((val2.split("/")[1]))
        if x ==0:
            messagebox.showerror("Error", "Division by 0 is not supported")
            A == ""
            val = ""
            data.set(val)
        else:
            c = int(A/x)
            data.set(c)
            val = str(c)




root = tkinter.Tk()
root.geometry("350x450+350+300")
root.resizable(0,0)
root.title("Galactico's Calculator")
root.iconbitmap(r"calculator1.ico")

data = StringVar()
lbl = Label(
    root,
    text = "screen",
    anchor=SE,
    font =("Yu Gothic UI Semibold", 20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand= True, fill ="both",)

buttonrow1 = Frame(root, bg="#000000")
buttonrow1.pack(expand = True, fill = "both",)

buttonrow2 = Frame(root)
buttonrow2.pack(expand= True, fill = "both")

buttonrow3 = Frame(root)
buttonrow3.pack(expand=True, fill = "both")

buttonrow4 = Frame(root)
buttonrow4.pack(expand=True, fill = "both")

button7 = Button(
    buttonrow1,
    text = "7",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command =  button_7_isclicked,
)
button7.pack(side = LEFT, expand = True, fill = "both")


button8 = Button(
    buttonrow1,
    text = "8",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_8_isclicked,
)
button8.pack(side = LEFT, expand = True, fill = "both")


button9 = Button(
    buttonrow1,
    text = "9",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_9_isclicked,
)
button9.pack(side = LEFT, expand = True, fill = "both")


buttonmul = Button(
    buttonrow1,
    text = "*",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_mul_isclicked,
)
buttonmul.pack(side = LEFT, expand = True, fill = "both")



button4 = Button(
    buttonrow2,
    text = "4",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_4_isclicked,
)
button4.pack(side = LEFT, expand = True, fill = "both")


button5 = Button(
    buttonrow2,
    text = "5",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_5_isclicked,
)
button5.pack(side = LEFT, expand = True, fill = "both")


button6 = Button(
    buttonrow2,
    text = "6",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_6_isclicked,
)
button6.pack(side = LEFT, expand = True, fill = "both")


buttonminus = Button(
    buttonrow2,
    text = "-",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_minus_isclicked,
)
buttonminus.pack(side = LEFT, expand = True, fill = "both")


button1 = Button(
    buttonrow3,
    text = "1",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_1_isclicked,
)
button1.pack(side = LEFT, expand = True, fill = "both")


button2 = Button(
    buttonrow3,
    text = "2",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_2_isclicked,
)
button2.pack(side = LEFT, expand = True, fill = "both")


button3 = Button(
    buttonrow3,
    text = "3",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_3_isclicked,
)
button3.pack(side = LEFT, expand = True, fill = "both")


buttonplus = Button(
    buttonrow3,
    text = "+",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_plus_isclicked,
)
buttonplus.pack(side = LEFT, expand = True, fill = "both")


buttonnc = Button(
    buttonrow4,
    text = "C",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_c_isclicked,
)
buttonnc.pack(side = LEFT, expand = True, fill = "both")


button0 = Button(
    buttonrow4,
    text = "0",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_0_isclicked,
)
button0.pack(side = LEFT, expand = True, fill = "both")


buttonequal = Button(
    buttonrow4,
    text = "=",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = result,
)
buttonequal.pack(side = LEFT, expand = True, fill = "both")


buttondiv = Button(
    buttonrow4,
    text = "/",
    font = ("Yu Gothic UI Semibold", 22),
    relief = GROOVE,
    border = 0,
    command = button_div_isclicked,
)
buttondiv.pack(side = LEFT, expand = True, fill = "both")






root.mainloop()
