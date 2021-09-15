import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # state 설정
readonly_combobox.pack()
readonly_combobox.current(0) # 초기 설정 값

def btncmd():
    print(combobox.get()) # 선택된 값 표시 (항목 선택 대신 문자를 쓸 경우 쓴 문자가 출력)
    print(readonly_combobox.get())

btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop()