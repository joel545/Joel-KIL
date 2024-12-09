import tkinter as tk1
def push_1():
    print("按下去的結果")

base = tk1.Tk()
button=tk1.Button(base, text="月曆查詢",command=push_1,width=100)
button.pack()
base.mainloop()