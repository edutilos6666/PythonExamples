from tkinter import *
from tkinter import messagebox

def example1():
    mainFrame = Tk()
    mainFrame.geometry("400x400")
    lblTitle = Label(mainFrame, text = "Welcome to the Tkinter")
    lblId = Label(mainFrame, text = "Id: ")
    entryId = Entry(mainFrame)
    lblName = Label(mainFrame, text= "Name: ")
    entryName = Entry(mainFrame)
    lblAge = Label(mainFrame, text = "Age: ")
    entryAge = Entry(mainFrame)
    lblWage = Label(mainFrame , text = "Wage: ")
    entryWage = Entry(mainFrame)
    lblActive = Label(mainFrame , text = "Active: ")
    entryActive = Entry(mainFrame)

    def btnOkPressed():
        info = """id = {0}
name = {1}
age = {2}
wage = {3}
active = {4}
        """.format(entryId.get(), entryName.get(), entryAge.get(), entryWage.get(), entryActive.get())
        messagebox.showinfo("buttonOK pressed", info)


    def btnClearPressed():
        entryId.delete(0, 'end')
        entryName.delete(0, "end")
        entryAge.delete(0, "end")
        entryWage.delete(0, "end")
        entryActive.delete(0, "end")

    btnOk = Button(mainFrame, text= "Ok", command = btnOkPressed)
    btnClear = Button(mainFrame, text="Clear", command = btnClearPressed)






    lblTitle.grid(row= 0 , column = 1)
    lblId.grid(row = 1, column = 0)
    entryId.grid(row=1, column = 2)
    lblName.grid(row = 2, column = 0)
    entryName.grid(row = 2, column = 2)
    lblAge.grid(row = 3, column = 0)
    entryAge.grid(row=3, column = 2)
    lblWage.grid(row=4, column = 0)
    entryWage.grid(row=4, column=2)
    lblActive.grid(row=5, column=0)
    entryActive.grid(row=5, column=2)
    btnOk.grid(row=6, column=1)
    btnClear.grid(row=6, column=2)



    mainFrame.mainloop()