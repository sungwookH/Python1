from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0) # selectmode - single(한개만), extended(다중 선택가능)
listbox.insert(0, "사과")                                # height - 보여줄 목록 갯수, 0이면 목록 전체 보여줌
listbox.insert(1, "포도")                                # height가 목록보다 작을 때, scroll 위치를 안 보여줌 
listbox.insert(2, "복숭아")
listbox.insert(END, "수박") # END - 목록 마지막에 추가
listbox.insert(END, "딸기")
listbox.pack()


def btncmd():
    listbox.delete(END) # 맨 뒤 항목 삭제
    listbox.delete(0) # 맨 앞 항목 삭제

    # 갯수 확인
    print("리스트에는", listbox.size(), "개가 있어요.")
    # 항목 확인 (시작 idx, 끝 idx)
    print("1번째부터 3번째까지의 항목 : ", listbox.get(0, 2))
    # 선택된 항목 확인 (위치로 반환)
    print("선택된 항목 : ", listbox.curselection())


btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop()