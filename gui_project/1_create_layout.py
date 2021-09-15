from tkinter import *
from tkinter.ttk import Combobox, Progressbar

root = Tk()
root.title("Nado GUI")

# 파일 프레임 (파일 추가, 선택 삭제)

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가")
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="파일삭제")
btn_del_file.pack(side="right")


# 리스트 프레임

list_frame = Frame(root)
list_frame.pack(fill="both", padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar.set)
list_file.pack(side="left", fill="both", expand=True)

# 저장 경로 프레임

path_frame = LabelFrame(root, text="저장 경로", padx=5, pady=5)
path_frame.pack(fill="x", padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side="left", fill="x", expand=True, ipady=4, padx=5, pady=5)

btn_dest_path = Button(path_frame, text="찾아보기", width=10)
btn_dest_path.pack(side="right", padx=5, pady=5)

# 옵션 프레임

opt_frame = LabelFrame(root, text="옵션", padx=5, pady=5)
opt_frame.pack(padx=5, pady=5, ipady=5)

    # 1. 가로 넓이 옵션
label_width = Label(opt_frame, text="가로넓이", width=8)
label_width.pack(side="left")

opt_width = ["원본유지", "1024", "800", "640"]
cmb_width = Combobox(opt_frame, width=10, state="readonly", values=opt_width)
cmb_width.current(0)
cmb_width.pack(side="left")


    # 2. 간격 옵션
label_space = Label(opt_frame, text="간격", width=8)
label_space.pack(side="left")

opt_space = ["없음", "좁게", "보통", "넓게"]
cmb_space = Combobox(opt_frame, width=10, state="readonly", values=opt_space)
cmb_space.current(0)
cmb_space.pack(side="left")


    # 3. 파일 포맷 옵션
label_format = Label(opt_frame, text="포맷", width=8)
label_format.pack(side="left")

opt_format = ["PNG", "JPG", "BMP"]
cmb_format = Combobox(opt_frame, width=10, state="readonly", values=opt_format)
cmb_format.current(0)
cmb_format.pack(side="left")

# 진행 상황 Progress Bar

prog_frame = LabelFrame(root, text="진행상황", padx=5, pady=5)
prog_frame.pack(fill="x", padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progressbar = Progressbar(prog_frame, maximum = 100, variable=p_var)
progressbar.pack(fill="x", padx=5, pady=5)

# 실행 프레임

run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_quit = Button(run_frame, padx=5, pady=5, text = "닫기", width =12, command=root.quit)
btn_quit.pack(side="right", padx=5, pady=5)

btn_start = Button(run_frame, padx=5, pady=5, text = "시작", width=12)
btn_start.pack(side="right", padx=5, pady=5)



scrollbar.config(command=list_file.yview)
root.resizable(False, False)
root.mainloop()