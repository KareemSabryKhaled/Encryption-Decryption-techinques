import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from AES import *
from elgamal import *
from des import *
from RSA2 import *
class Client:
    def __init__(self, host = '192.168.1.17', port = 55555):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

        self.root = tk.Tk()
        self.chat_window = scrolledtext.ScrolledText(self.root)
        self.chat_window.pack()
        self.msg_entry = tk.Entry(self.root)
        self.msg_entry.bind("<Return>", self.write)
        self.msg_entry.pack()
        self.button1 = tk.Button(self.root, text="Command 1", command=self.command1)
        self.button1.pack()
        self.button2 = tk.Button(self.root, text="Command 2", command=self.command2)
        self.button2.pack()
        self.button3 = tk.Button(self.root, text="Command 3", command=self.command3)
        self.button3.pack()
        self.button4 = tk.Button(self.root, text="Command 4", command=self.command4)
        self.button4.pack()

        self.messages = []
        self.stop_thread = False

    def command1(self):
        # self.client.send('Command 1 was triggered'.encode('utf-8'))
        #self.client.send(self.msg_entry.get().encode('utf-8'))
        print(self.msg_entry.get())
        cc = AESCallEncrypt(self.msg_entry.get())
        cc = cc + '1'
        self.client.send(cc.encode('utf-8'))




    def command2(self):
        print(self.msg_entry.get())
        cc = encrypt(self.msg_entry.get())
        cc = cc + '2'
        self.client.send(cc.encode('utf-8'))


    def command3(self):
        #self.client.send('Command 3 was triggered'.encode('utf-8'))
        cc = encryption_elgamal(self.msg_entry.get())
        cc = cc + '3'
        self.client.send(cc.encode('utf-8'))



    def command4(self):
        #self.client.send('Command 3 was triggered'.encode('utf-8'))
        cc = cipherRSA(self.msg_entry.get())
        cc = cc + '4'
        self.client.send(cc.encode('utf-8'))

    def receive_messages(self):
        while not self.stop_thread:
            try:
                message = self.client.recv(1024).decode('utf-8')
                self.messages.append(message)
            except:
                print("An error occured!")
                self.client.close()
                break

    def update_messages(self):
        if self.messages:
            ddd = ''
            holder = self.messages.pop(0)
            if holder[-1] == '1':

                ddd = AESCallDecrypt(holder[0:len(holder)-1])
            elif holder[-1] == '2':

                ddd = decrypt((holder[0:len(holder)-1]))

            elif holder[-1] == '3':

                ddd = decryption_elgamal(holder[0:len(holder)-1])
            elif holder[-1] == '4':

                ddd = decipherRSA(holder[0:len(holder)-1])
            self.chat_window.insert(tk.END, ddd)
            print('ddd', ddd)
        self.root.after(100, self.update_messages)

    def write(self, event=None):
        message = f'{self.msg_entry.get()}'
        self.msg_entry.delete(0, tk.END)
        self.client.send(message.encode('utf-8'))

    def stop(self):
        self.stop_thread = True
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.protocol("WM_DELETE_WINDOW", self.stop)
        threading.Thread(target=self.receive_messages).start()
        self.root.after(100, self.update_messages)
        self.root.mainloop()

client = Client()
client.run()