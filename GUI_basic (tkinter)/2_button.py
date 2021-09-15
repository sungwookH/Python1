from tkinter import *

root = Tk()
root.title("Nado GUI")

btn1 = Button(root, text="버튼1") # 버튼 위젯 만들기
btn1.pack() # 버튼 표출

btn2 = Button(root, padx=5, pady=10, text="버튼2") # text 기준 좌, 우 여백 / 버튼 크기가 고정되진 않음
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=5, text="버튼4444444444444444444") # 크기를 설정, 설정된 크기는 고정됨 / 즉 글자가 잘릴수도
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg 글자색, bg 배경색
btn5.pack()

photo = PhotoImage(file="GUI_basic (tkinter)/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def click():
    print("버튼이 클릭되었어요.")
btn7 = Button(root, text="동작하는 버튼", command=click)
btn7.pack()




root.mainloop() # 창이 닫히지 않도록