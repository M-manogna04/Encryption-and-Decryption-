import tkinter as tk
import base64

window = tk.Tk()
window.title("Python Encrypter & Decrypter")
window.config(bg="lavender")
window.geometry('500x500')

message = tk.StringVar()
key = tk.StringVar()
result = tk.StringVar()

def Encode():
    res = ""
    mes = message.get()
    ke = key.get()
    for i in range(len(mes)):
        char = ke[i%len(ke)]
        res+=chr((ord(mes[i]) + ord(char))%256)

    result.set(base64.urlsafe_b64encode(res.encode()))

def Decode():
    res = ""
    mes = base64.urlsafe_b64decode(message.get()).decode()
    ke = key.get()
    for i in range(len(mes)):
        char = ke[i%len(ke)]
        res+=chr((ord(mes[i])-ord(char))%256)
    result.set(res)

def Reset():
    message.set("")
    key.set("")
    result.set("")

def Exit():
    window.destroy()


tk.Label(window, text = "Encrypt&Decrypt", font= '"times new roman" 16 italic underline').pack()

tk.Label(window, text = "Message", font = '"times new roman" 12 bold').place(x=120,y=60)
tk.Entry(window, font = '"times new roman" 12', textvariable = message).place(x=240,y=60)

tk.Label(window, text = "Key", font = '"times new roman" 12 bold').place(x=120,y=100)
tk.Entry(window, font = '"times new roman" 12', textvariable = key).place(x=240,y=100)

tk.Label(window,text="Result",font='"times new roman" 12 bold').place(x=120,y=215)
tk.Entry(window, textvariable = result, font= '"times new roman" 12 bold').place(x=240,y=215)

tk.Button(window, text = "Encrypt", font = '"times new roman" 12 bold', command=Encode, width=10,bg='blue').place(x=140,y=160)
tk.Button(window, text = "Decrypt", font = '"times new roman" 12 bold', command=Decode, width=10,bg='ghost white').place(x=260,y=160)

tk.Button(window, text = "Reset", font = '"times new roman" 12 bold', command = Reset, width=10,bg='green').place(x=140,y=260)
tk.Button(window, text = "Exit", font = '"times new roman" 12 bold', command = Exit, width=10,bg='red').place(x=260,y=260)

window.mainloop()

    





