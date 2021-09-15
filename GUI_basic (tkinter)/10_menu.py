from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

def create_new_file():
    print("새로운 파일을 생성합니다.")

menu_my = Menu(root) # root에 존재하는 Menu 클래스를 menu_my라는 변수로 생성

# File 메뉴
menu_my_file = Menu(menu_my, tearoff=0) # 내 메뉴 리스트 menu_my안에 보여질 하위 메뉴 menu_my_file 생성
menu_my_file.add_command(label = "New File", command=create_new_file)
menu_my_file.add_command(label = "New Window")
menu_my_file.add_separator() # 구분자 생성
menu_my_file.add_command(label="Open File")
menu_my_file.add_separator()
menu_my_file.add_command(label="Save All", state="disable") # 비활성화
menu_my_file.add_separator()
menu_my_file.add_command(label="Exit", command=root.quit)

menu_my.add_cascade(label="FILE", menu=menu_my_file) # 내 메뉴 리스트 menu_my에 하위 메뉴 meny_my_file를 표출

# Edit 메뉴 (빈 값)
menu_my.add_cascade(label="EDIT")

# Language 메뉴 추가 (radio 버튼 통해서 택 1)
menu_my_language = Menu(menu_my, tearoff=0)
menu_my_language.add_radiobutton(label="python")
menu_my_language.add_radiobutton(label="jave")
menu_my_language.add_radiobutton(label="C++")

menu_my.add_cascade(label="Language", menu = menu_my_language)

# View 메뉴 추가 (checkboxq 버튼)
menu_my_view = Menu(menu_my, tearoff=0)
menu_my_view.add_checkbutton(label="Show Minimap")

menu_my.add_cascade(label="View", menu=menu_my_view)

root.config(menu=menu_my) # 내가 Menu 클래스로 만든 menu_my를 메뉴 리스트로써 생성
root.mainloop()