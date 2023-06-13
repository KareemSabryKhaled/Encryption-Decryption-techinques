from client import*
from RSAnew import*
from RSA2 import*
from tkinter import*
import tkinter
from server import*
from client import*
top = tkinter.Tk()
top.geometry("350x450")
top.configure(bg='black')
my_text = Text(top,width=25,height=5)
my_text.pack(pady=20)
msg = my_text.get("1.0",END)

B1 = tkinter.Button(top, text ="AES", command ="" ,bg='#116530',fg='white',height= 2, width=10)
B1.pack(padx=20,pady=10)
B2 = tkinter.Button(top, text ="DES", command ="" ,bg='#116530',fg='white',height= 2, width=10)
B2.pack(padx=20,pady=10)
#B3 = tkinter.Button(top, text ="RSA", command =  lambda: RSA(my_text.get("1.0",END)),bg='#116530',fg='white',height= 2, width=10)
#B3.pack(padx=20,pady=10)
B4 = tkinter.Button(top, text ="Al-Gammal", command = server ,bg='#116530',fg='white',height= 2, width=10)
B4.pack(padx=20,pady=10)

B5 = tkinter.Button(top, text ="RSA", command =  lambda: RSA2(my_text.get("1.0",END)),bg='#116530',fg='white',height= 2, width=10)
B5.pack(padx=20,pady=10)
top.mainloop()