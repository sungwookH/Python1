from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

frame = Frame(root,relief="solid")
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")  # 위 아래로 채움


listbox = Listbox(frame, selectmode="single", height=10, yscrollcommand=scrollbar.set) # listbox 와 scrollbar 호환
listbox.pack(side="left")
for i in range(1, 32):
    listbox.insert(END, f"{i}일")

scrollbar.config(command=listbox.yview) # listbox 와 scrollbar 호환

root.mainloop()