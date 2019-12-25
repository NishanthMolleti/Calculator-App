from tkinter import *
root=Tk()
root.title("Calculator App")
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def add(n):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(n))

def clear():
    e.delete(0, END)

def ad():
    first=e.get()
    global fnum
    global math
    math="addition"
    fnum= int(first)
    e.delete(0, END)

def equal():
    sec=e.get()
    e.delete(0, END)

    if math=="addition"
        e.insert(0, fnum+int(sec))
    if math=="subtraction"
        e.insert(0, fnum-int(sec))
    if math=="multiplication"
        e.insert(0, fnum*int(sec))
    if math=="division"
        e.insert(0, fnum/int(sec))
def sub():
    first=e.get()
    global fnum
    global math
    math="subtraction"
    fnum= int(first)
    e.delete(0, END)

def mul():
    first=e.get()
    global fnum
    global math
    math="multiplication"
    fnum= int(first)
    e.delete(0, END)

def div():
    first=e.get()
    global fnum
    global math
    math="division"
    fnum= int(first)
    e.delete(0, END)


b1=Button(root,text='1',padx=40,pady=20,command=lambda:add(1))
b2=Button(root,text='2',padx=40,pady=20,command=lambda:add(2))
b3=Button(root,text='3',padx=40,pady=20,command=lambda:add(3))
b4=Button(root,text='4',padx=40,pady=20,command=lambda:add(4))
b5=Button(root,text='5',padx=40,pady=20,command=lambda:add(5))
b6=Button(root,text='6',padx=40,pady=20,command=lambda:add(6))
b7=Button(root,text='7',padx=40,pady=20,command=lambda:add(7))
b8=Button(root,text='8',padx=40,pady=20,command=lambda:add(8))
b9=Button(root,text='9',padx=40,pady=20,command=lambda:add(9))
b0=Button(root,text='0',padx=87,pady=20,command=lambda:add(0))
ba=Button(root,text='+',padx=39,pady=20,command=lambda:ad())
#bs=Button(root,text='-',padx=40,pady=20,command=lambda:add())
be=Button(root,text='=',padx=86,pady=20,command=lambda:equal())
bc=Button(root,text='C',padx=40,pady=20,command=lambda:clear())

bs=Button(root,text='-',padx=41,pady=20,command=lambda:sub())
bm=Button(root,text='*',padx=40,pady=20,command=lambda:mul())
bdiv=Button(root,text='/',padx=41,pady=20,command=lambda:div())

b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=1,column=2)
b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)
b7.grid(row=3,column=0)
b8.grid(row=3,column=1)
b9.grid(row=3,column=2)
b0.grid(row=4,column=1,columnspan=2)
ba.grid(row=4,column=0)
bc.grid(row=5,column=0)
be.grid(row=5,column=1,columnspan=2)
bs.grid(row=6,column=0)
bm.grid(row=6,column=1)
bdiv.grid(row=6,column=2)
root.mainloop()
