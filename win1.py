import tkinter as tk1
import requests
from bs4 import BeautifulSoup
html_data = requests.get('http://tw.yahoo.com')
soup = BeautifulSoup(html_data.text,"html.parser")
def push_1():
    print("按下去的結果")
    soup.title
base = tk1.Tk()
button=tk1.Button(base, text="月曆查詢",command=push_1,width=100)
button.pack()
base.mainloop()