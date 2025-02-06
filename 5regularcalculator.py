from ttkthemes import ThemedTk
from tkinter import *

screen = ThemedTk(theme="black")
screen.configure(themebg="black")
screen.title("Parathyro") #titlos
screen.geometry('360x290')#parathyro megethos
screen.resizable(width=False,height=False)
screen.configure(bg='black')

def press(num): # grafei sto entry meta to teleuteo pragma pou eixe
    ent.insert(END,num)

def clear():
    ent.delete(0 , END)

def equal ():
    try:
        x =ent.get()
        result = eval(x)
        ent.delete(0,END)
        ent.insert(END,result)
    except:
        ent.delete(0,END)
        ent.insert(END,"Error")



ent=Entry(screen,width=40,font='Impact')
btn1=Button(screen,text="1",bg='black',width=10,height=2,fg='green',font='Impact',command=lambda: press('1'))
btn2=Button(screen,text="2",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('2'))
btn3=Button(screen,text="3",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('3'))
btnmultiply=Button(screen,text="*",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('*'))
btn4=Button(screen,text="4",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('4'))
btn5=Button(screen,text="5",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('5'))
btn6=Button(screen,text="6",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('6'))
btnplus=Button(screen,text="+",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('+'))
btn7=Button(screen,text="7",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('7'))
btn8=Button(screen,text="8",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('8'))
btn9=Button(screen,text="9",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('9'))
btnminus=Button(screen,text="-",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('-'))
btndot=Button(screen,text=".",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('.'))
btn0=Button(screen,text="0",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('0'))
btnclear=Button(screen,text="C",width=10,height=2,bg='black',fg='green',font='Impact',command=clear)
btndivide=Button(screen,text="/",width=10,height=2,bg='black',fg='green',font='Impact',command=lambda: press('/'))
btnequal=Button(screen,text='=',width=40,height=2,bg='black',fg='green',font='Impact',command=equal)

ent.grid(row =0,column=0,columnspan=4)
btn1.grid(row = 1,column=0)
btn2.grid(row = 1,column=1)
btn3.grid(row = 1,column=2)
btnmultiply.grid(row =1,column=3)
btn4.grid(row=2,column=0)
btn5.grid(row=2,column=1)
btn6.grid(row = 2,column=2)
btnplus.grid(row = 2,column=3)
btn7.grid(row = 3,column=0)
btn8.grid(row = 3,column=1)
btn9.grid(row = 3,column=2)
btnminus.grid(row = 3,column=3)
btnclear.grid(row = 4,column=0)
btn0.grid(row = 4,column=1)
btndot.grid(row = 4,column=2)
btndivide.grid(row = 4,column=3)
btnequal.grid(row = 5,column=0,columnspan=4)

screen.mainloop() #kleinei programma