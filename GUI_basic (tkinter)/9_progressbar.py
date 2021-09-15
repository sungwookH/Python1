import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
progressbar = ttk.Progressbar(root, maximum=100, mode="determinate") # 게이지가 움직이는 형태
progressbar.start(10)
progressbar.pack()

p_var = DoubleVar() # 실수 형태로 값 저장
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var) # length - progressbar 길이
progressbar2.pack()


def btncmd():
#    progressbar.stop() # 중지
    for i in range(101):
        time.sleep(0.01) # 0.01 초 대기

        p_var.set(i) # progress bar 의 값 설정
        progressbar2.update() # ui 업데이트 for 문 안 실행내용을 실시간 display 에 반영
        print(p_var.get())

btn = Button(root, text="시작", command=btncmd)
btn.pack()

root.mainloop()