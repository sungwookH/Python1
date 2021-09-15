from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

label = Label(text="메뉴를 선택해주세요").pack(side="top")

Button(root, text="order").pack(side="bottom")


frame_burger = Frame(root, relief="solid", bd=1) # Frame / relief - 테두리 bd - 테두리 두께

frame_burger.pack(side="left",fill="both", expand=True) # fill both - 위 아래로 꽉 채움 / expand - 펼치기



Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

frame_drink = LabelFrame(root, text="음료", bd=1) # LabelFrame
frame_drink.pack(side="right",fill="both", expand=True)

Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()



root.mainloop()