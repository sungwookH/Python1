# 1. title : 제목 없음 - Windows 메모장/
# 2. 메뉴 : 파일, 편집, 서식, 보기, 도움말/
# 3. 실제 메뉴 구현 : 파일 메뉴 내에서 열기, 저장, 끝내기 3개만 처리/
# 3-1. 열기 : mynote.txt 파일 내용 열어서 보여주기/
# 3-1. 저장 : mynote.txt 파일에 현재 내용 저장하기/
# 3-3. 끝내기 : 프로그램 종료/
# 4. 프로그램 시작 시 본문은 비어 있는 상태/
# 5. 프로그램 크기, 위치는 자유롭게 하되 크기 조정 가능 /
# 6. 본문 우측에 상하 스크롤 바 넣기
import os
import tkinter.font
from tkinter import *

note = Tk()
note.title("제목 없음 - Windows 메모장")
note.geometry("640x480+100+100")
note.resizable(True, True)

fontsize = tkinter.font.Font(size=20)

scrollbar = Scrollbar(note)
scrollbar.pack(side="right", fill="y")

txt = Text(note, font=fontsize, yscrollcommand=scrollbar.set)
txt.pack(side="left", fill="both", expand=True)

filename = "mynote.txt"


my_menu = Menu(note)

my_menu_file = Menu(my_menu, tearoff=0)
def open_file():
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf8") as txt_file:
            txt.delete("1.0", END) # 텍스트 위젯 본문 삭제
            txt.insert(END, txt_file.read()) # 파일 내용을 본문에 입력

my_menu_file.add_command(label="열기", command=open_file)

def save():
    with open(filename, "w", encoding="utf8") as txt_file:
        txt_file.write(txt.get("1.0", END))

my_menu_file.add_command(label="저장", command=save)

my_menu_file.add_separator()
my_menu_file.add_command(label="끝내기", command=note.quit)
my_menu.add_cascade(label="파일", menu = my_menu_file)
my_menu.add_cascade(label="편집")
my_menu.add_cascade(label="서식")
my_menu.add_cascade(label="보기")
my_menu.add_cascade(label="도움말")


scrollbar.config(command=txt.yview)
note.config(menu=my_menu)

note.mainloop() # 창이 닫히지 않도록