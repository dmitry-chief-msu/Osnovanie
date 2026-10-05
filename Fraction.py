from tkinter import *
root=Tk()
root.title("Калькулятор новый дробей")
root.geometry("400x200+200+200")

frame = Frame(root)
frame.pack(pady=40)
num1=Entry(frame,width=2)
num1.config(font=("Arial",15))

num1.grid(row=0,column=0)



root.mainloop()




