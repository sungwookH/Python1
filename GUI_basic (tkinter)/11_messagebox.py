import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료!")

def warn():
    msgbox.showwarning("경고", "해당 좌석 매진!")
    msgbox.showerror("에러", "결제오류, 재접속 요망")

def okcancel():
    response = msgbox.askokcancel("확인/취소", "해당 좌석은 유아동반석, 예매하시겠습니까?")
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    msgbox.askretrycancel("재시도/취소", "일시적인 오류입니다. 다시 시도하시겠습니까?")
def yesno():
    msgbox.askyesno("예/아니오", "좌석은 역방향입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message="예매 내역이 저장되지 않았습니다\n저장하시겠습니까?")
    # 네 : 저장 후 종료
    # 아니오 : 저장 하지 않고 종료
    # 취소 : 프로그램 종료 취소 (현재 화면 유지)
    print("응답 :", response)
    if response == 1:
        print("예")
    elif response == 0:
        print("아니오")
    else:
        print("취소")

Button(root, text="알림", command=info).pack()
Button(root, text="경고", command=warn).pack()
Button(root, text="확인/취소", command=okcancel).pack()
Button(root, text="예 아니오", command=yesno).pack()
Button(root, text="예 아니오 취소", command=yesnocancel).pack()


root.mainloop()