from tkinter import*
root=Tk()
root.geometry("400x300")
root.title("password game")
def toplevel():
    top=Toplevel()
    top.geometry("180x100")
    top.title("my toplevel!")
    L1=Label(top,text="this is the toplevel window!")
    L1.pack()
    top.mainloop()

L=Label(root,text='u have to guess the password!!!')
btn=Button(root,text='click here to open another window',command=toplevel)
secret_password = "harry potter"
guess = input("Guess the secret password: ")
if guess != secret_password:
  print("Wrong!")
if guess == secret_password:
  print("You guessed it!")
L.pack()
btn.pack()
root.mainloop()