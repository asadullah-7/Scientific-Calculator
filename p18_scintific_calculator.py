import tkinter as tk
from tkinter import messagebox
import math

root = tk.Tk()
root.title("Scintific Calculator")
root.geometry("400x600")

display = tk.Entry(root,font=("Arial",20),borderwidth=5,relief="solid",justify="right")
display.grid(row=0,column=0,columnspan=10,pady=10,padx=10)

def button_click(number):
  current = display.get()
  display.delete(0,tk.END)
  display.insert(0,current+str(number))
def clear_display():  
  display.delete(0,tk.END)
  display.insert(0,"")
def delete_last():
  current = display.get()
  display.delete(0,tk.END)
  display.insert(0,current[:-1])
# Operations Function
def operator(op):
  current = display.get()
  display.delete(0,tk.END)
  display.insert(0,current+op)

def Result():
  try:
    current = display.get()
    display.delete(0,tk.END)
    display.insert(0,eval(current))
  except ZeroDivisionError:
    messagebox.showerror("Math Error", "Cannot divide by ZERO!")
    clear_display()
  except Exception:
    messagebox.showerror("Error","Invalid Input!")
    clear_display()
#================= KEYBOARD USAGE ==================
def key_event(event):
  key = event.char
  if key.isdigit()or key in ['+', '-', '/', '*', '.'] :
    button_click(key)
    return "break"

  elif key == '\r':
    Result()
    return "break"
  elif key == '\x08':
    delete_last()
    return "break"

root.bind("<Key>",key_event)

# ============================ SCIENTIFIC FUNCTIONS ============================
def sqrt_fun():
  try:
    current = float(display.get())
    result = math.sqrt(current)
    display.delete(0,tk.END)
    display.insert(0,str(result))

  except Exception:
    messagebox.showerror("Error", "Invalid Input!")
    clear_display()
def power_fun():
  try:
    current=float(display.get())
    result = math.pow(current,2)
    display.delete(0,tk.END)
    display.insert(0,str(result))

  except Exception:
    messagebox.showerror("Error", "Invalid Input!")
    clear_display()

def sin_fun():
  try:
    current = float(display.get())
    result = math.sin(math.radians(current))
    display.delete(0,tk.END)
    display.insert(0,str(result))

  except Exception:
    messagebox.showerror("Error", "Invalid Input!")
    clear_display()

def cos_fun():
  try:
    current = float(display.get())
    result = math.cos(math.radians(current))
    display.delete(0,tk.END)
    display.insert(0,str(result))

  except Exception:
    messagebox.showerror("Error", "Invalid Input!")
    clear_display()

def tan_fun():
  try:
    current = float(display.get())
    result = math.tan(math.radians(current))
    display.delete(0,tk.END)
    display.insert(0,str(result))

  except Exception:
    messagebox.showerror("Error", "Invalid Input!")
    clear_display()
########################################################################################################
btnErase = tk.Button(root,text="C",width=5,height=2,bg="red",fg="black",command=lambda:clear_display())
btnErase.grid(row=1,column=0)
btnDel = tk.Button(root,text="<",width=5,height=2,bg="red",fg="black",command=lambda:delete_last())
btnDel.grid(row=1,column=1)
# =============================== OPERATIONAL BUTTONS ==================================
btnDivide = tk.Button(root,text="/",width=5,height=2,bg="orange",fg="black",command= lambda:operator("/"))
btnDivide.grid(row=1,column=2)
btnMul = tk.Button(root,text="x",width=5,height=2,bg="orange",fg="black",command=lambda:operator("*"))
btnMul.grid(row=1,column=3)
btnSub = tk.Button(root,text="-",width=5,height=2,bg="orange",fg="black",command=lambda:operator("-"))
btnSub.grid(row=2,column=3)
btnAdd = tk.Button(root,text="+",width=5,height=6,bg="orange",fg="black",command=lambda:operator("+"))
btnAdd.grid(row=3,column=3,rowspan=2,sticky="ns")
btnEq = tk.Button(root,text = "=",width=5,height=2,bg="lightgreen",fg="black",command= lambda:Result())
btnEq.grid(row=5,column=3)

# ================================= SCIENTIFIC BUTTONS ==================================
btnSqrt = tk.Button(root,text="√",width=5,height=2,bg="black",fg="white",command=sqrt_fun)
btnSqrt.grid(row=1,column=4)
btnPwr = tk.Button(root,text="x²",width=5,height=2,bg="black",fg="white",command=power_fun)
btnPwr.grid(row=2,column=4)
btnSin = tk.Button(root,text="sin",width=5,height=2,bg="black",fg="white",command=sin_fun)
btnSin.grid(row=3,column=4)
btnCos = tk.Button(root,text="cos",width=5,height=2,bg="black",fg="white",command=cos_fun)
btnCos.grid(row=4,column=4)
btnTan = tk.Button(root,text="tan",width=5,height=2,bg="black",fg="white",command=tan_fun)
btnTan.grid(row=5,column=4)
# ======================================================================================
btn1 = tk.Button(root,text = "1",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(1))
btn1.grid(row=2,column=0)
btn2 = tk.Button(root,text = "2",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(2))
btn2.grid(row=2,column=1)
btn3 = tk.Button(root,text = "3",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(3))
btn3.grid(row=2,column=2)
btn4 = tk.Button(root,text = "4",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(4))
btn4.grid(row=3,column=0)
btn5 = tk.Button(root,text = "5",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(5))
btn5.grid(row=3,column=1)
btn6 = tk.Button(root,text = "6",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(6))
btn6.grid(row=3,column=2)
btn7 = tk.Button(root,text = "7",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(7))
btn7.grid(row=4,column=0)
btn8 = tk.Button(root,text = "8",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(8))
btn8.grid(row=4,column=1)
btn9 = tk.Button(root,text = "9",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(9))
btn9.grid(row=4,column=2)
btn0 = tk.Button(root,text = "0",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click(0))
btn0.grid(row=5,column=0)
btn00 = tk.Button(root,text = "00",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click("00"))
btn00.grid(row=5,column=1)
btnptr = tk.Button(root,text = ".",width=5,height=2,bg="lightblue",fg="black", command=lambda:button_click("."))
btnptr.grid(row=5,column=2)



root.mainloop()