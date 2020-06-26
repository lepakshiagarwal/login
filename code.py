import tkinter

#setting the screen
window = tkinter.Tk()
window.geometry("500x500")
window.title("login")

#making feilds
box1 = tkinter.Label(window, text="email/username:")
text1 = tkinter.Entry(window)

box2 = tkinter.Label(window, text="password:")
text2 = tkinter.Entry(window)

button = tkinter.Button(window, text="login")
box1.pack()
text1.pack()
box2.pack()
text2.pack()
button.pack()

window.mainloop()
