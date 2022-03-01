from tkinter import *

mansLogs=Tk()
mansLogs.title("Kalkulators")
mansLogs.iconbitmap("C:/Users/Skolnieks/Desktop/Ance 11.a/lietotne/kal.ico")

btn0=Button(mansLogs, text="0", padx="40", pady="20", command=lambda:klik(0))
btn1=Button(mansLogs, text="1", padx="40", pady="20", command=lambda:klik(1))
btn2=Button(mansLogs, text="2", padx="40", pady="20", command=lambda:klik(2))
btn3=Button(mansLogs, text="3", padx="40", pady="20", command=lambda:klik(3))
btn4=Button(mansLogs, text="4", padx="40", pady="20", command=lambda:klik(4))
btn5=Button(mansLogs, text="5", padx="40", pady="20", command=lambda:klik(5))
btn6=Button(mansLogs, text="6", padx="40", pady="20", command=lambda:klik(6))
btn7=Button(mansLogs, text="7", padx="40", pady="20", command=lambda:klik(7))
btn8=Button(mansLogs, text="8", padx="40", pady="20", command=lambda:klik(8))
btn9=Button(mansLogs, text="9", padx="40", pady="20", command=lambda:klik(9))
btna=Button(mansLogs, text="+", padx="40", pady="20", command=lambda:darbibas("+"))
btnb=Button(mansLogs, text="-", padx="40", pady="20", command=lambda:darbibas("-"))
btnc=Button(mansLogs, text="c", padx="40", pady="20")
btnr=Button(mansLogs, text="*", padx="40", pady="20", command=lambda:darbibas("*"))
btnp=Button(mansLogs, text="/", padx="40", pady="20", command=lambda:darbibas("/"))
btnd=Button(mansLogs, text="=", padx="40", pady="20")

e=Entry(mansLogs, width=15)
btn1.grid(row=3, column=0)
btn2.grid(row=3, column=1)
btn3.grid(row=3, column=2)

btn4.grid(row=2, column=0)
btn5.grid(row=2, column=1)
btn6.grid(row=2, column=2)

btn7.grid(row=1, column=0)
btn8.grid(row=1, column=1)
btn9.grid(row=1, column=2)

btn0.grid(row=4, column= 0)
btna.grid(row=4, column=1)
btnb.grid(row=4, column=2)
btnc.grid(row=4, column=3)

btnr.grid(row=2, column=3)
btnp.grid(row=3, column=3)

btnd.grid(row=5, column=3, rowspan=3)
e.grid(row=0, column=0, columnspan=10)

def klik(skaitlis):
    tagad=e.get()
    e.delete(0, END)
    jauns=str(tagad)+str(skaitlis)
    e.insert(0, jauns)

    return 0

def dzest():
    e.delete(0, END)

    return 0

def darbibas(darbs):
    global num1
    global mat0p
    mat0p=darbs
    num1=int(e.get())
    e.delete(0, END)
    return 0

def vienads():
    num2=int(e.get())
    rezultats=0
    if mat0p=="+":
        rezultats=num1+num2
    elif mat0p=="-":
        rezultats=num1-num2
    elif mat0p=="*":
        rezultats=num1*num2
    e.delete(0, END)
    e.insert(0,str(rezultats))
    return 0


mansLogs.mainloop()
