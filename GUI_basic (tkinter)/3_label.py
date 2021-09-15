from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label1 = Label(root, text="안녕하세요")
label1.pack()

photo = PhotoImage(file="GUI_basic (tkinter)/img.png")
label2 = Label(root, image=photo)
label2.pack()



def change():
    label1.config(text="또 만나요")

    global photo2
    photo2 = PhotoImage(file="GUI_basic (tkinter)/img2.png") # garbage collection 이 함수가 끝나면 내부변수를 지워버림
    label2.config(image=photo2)                              # 전역변수 설정으로 이걸 방지

btn = Button(root, text="클릭", command=change)
btn.pack()

root.mainloop()