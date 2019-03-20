from tkinter import *
root=Tk()

expression=" "
equation=StringVar()
def press(num):  
    global expression  
    expression = expression + str(num) 
    equation.set(expression)
def a(): 
    global expression 
    total = str(eval(expression)) 
    equation.set(total)
    expression=" "
def clear():
    global expression
    equation.set("")
    expression=" "

l1=Label(root,text="CALCULATOR",fg="blue",bg="pink")
l1.grid(row=0,columnspan=4)
expression_field = Entry(root, textvariable=equation) 
expression_field.grid(row=3,columnspan=4,ipadx=70) 
equation.set('enter your expression') 

button1=Button(root,text="1",fg="black",bg="blue",command=lambda:press(1),height=1,width=7)
button1.grid(row=6, column=0)

button2=Button(root,text="2",fg="black",bg="blue",command=lambda:press(2),height=1,width=7)
button2.grid(row=6,column=1)
 
button3=Button(root,text="3",fg="black",bg="blue",command=lambda:press(3),height=1,width=7)
button3.grid(row=6,column=2)

button4=Button(root,text="4",fg="black",bg="blue",command=lambda:press(4),height=1,width=7)
button4.grid(row=7,column=0)

button5=Button(root,text="5",fg="black",bg="blue",command=lambda:press(5),height=1,width=7)
button5.grid(row=7,column=1)

button6=Button(root,text="6",fg="black",bg="blue",command=lambda:press(6),height=1,width=7)
button6.grid(row=7,column=2)

button7=Button(root,text="7",fg="black",bg="blue",command=lambda:press(7),height=1,width=7)
button7.grid(row=8,column=0)

button8=Button(root,text="8",fg="black",bg="blue",command=lambda:press(8),height=1,width=7)
button8.grid(row=8,column=1)

button9=Button(root,text="9",fg="black",bg="blue",command=lambda:press(9),height=1,width=7)
button9.grid(row=8,column=2)

button10=Button(root,text="0",fg="black",bg="blue",command=lambda:press(0),height=1,width=7)
button10.grid(row=9,column=0)

plus = Button(root, text=' + ', fg='black', bg='red', command=lambda:press("+"), height=1, width=7) 
plus.grid(row=6, column=3) 
  
minus = Button(root, text=' - ', fg='black', bg='red', command=lambda:press("-"), height=1, width=7) 
minus.grid(row=7, column=3) 
  
multiply = Button(root, text=' * ', fg='black', bg='red', command=lambda:press("*"), height=1, width=7) 
multiply.grid(row=8, column=3) 
  
divide = Button(root, text=' / ', fg='black', bg='red', command=lambda:press("/"), height=1, width=7) 
divide.grid(row=9, column=3) 
  
equal = Button(root, text=' = ', fg='black', bg='red', command=a, height=1, width=7) 
equal.grid(row=9, column=2) 
  
clear = Button(root, text='Clear', fg='black', bg='red', command=clear, height=1, width=7) 
clear.grid(row=9, column='1')

root.mainloop()
