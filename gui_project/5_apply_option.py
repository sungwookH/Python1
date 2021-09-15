from tkinter import *  # __all__
from tkinter.ttk import Combobox, Progressbar
from tkinter import filedialog,messagebox
from PIL import Image
import os

root = Tk()
root.title("Nado GUI")

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요.", \
        filetypes = (("PNG 파일", "*.png"), ("모든 파일", "*.*")), \
        initialdir=r"C:/Users/sunguk/Desktop/python workspace")

    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)


# 파일 삭제
def del_file():
    for index in reversed(list_file.curselection()):   # 정상 순서로 지우면 인덱스 값이 변하기에, 뒤에서부터 지워야함
        list_file.delete(index)

# 찾아보기
def save():
    folder_selected = filedialog.askdirectory()
    if folder_selected == "":
        return
    txt_dest_path.delete(0, END)   # 기선택내용 삭제
    txt_dest_path.insert(0, folder_selected) # 후 추가

# 시작
def start():

    if list_file.size() == 0:   # get == "" 도 가능
        messagebox.showinfo("No list", "선택된 파일이 없습니다. 다시 확인해주세요.")
        return
    if len(txt_dest_path.get()) == 0:   # get == "" 도 가능
        messagebox.showerror("저장경로", "저장경로가 선택되지 않았습니다.")
        return

    merge_image()

def merge_image():
    try:
    # 선택한 가로넓이 옵션
        selected_width = cmb_width.get()
        if selected_width == "원본유지":
            slt_image_width = -1
        else:
            slt_image_width = int(selected_width)

    # 선택한 이미지 간격
        selected_space = cmb_space.get()
        if selected_space == "좁게":
            slt_space = 30
        elif selected_space == "보통":
            slt_space = 60
        elif selected_space == "넓게":
            slt_space = 90
        else:
            slt_space = 0
    # 선택한 포맷 옵션
        selected_format = cmb_format.get().lower()

        images = [Image.open(i) for i in list_file.get(0, END)]
        images_sizes = []
    
    # 이미지 크기 조절
        if slt_image_width > -1:
            images_sizes = [(int(slt_image_width), int(slt_image_width * x.size[1] / x.size[0])) for x in images]
        else:
            images_sizes = [(x.size[0], x.size[1]) for x in images]
        
        width, height = zip(*(images_sizes))  # →→→→→→→ imgs_width = [x.size[0] for x in images]
        m_width, T_height = max(width), sum(height)   # imgs_height = [x.size[1] for x in images]

    # 스케치북
        if slt_space > 0:
            T_height += slt_space * (len(images) - 1)

        result_image = Image.new("RGB", (m_width, T_height), (255, 255, 255))
        y_offset = 0
        for idx, image in enumerate(images):
            if slt_image_width > -1:
                image = image.resize(images_sizes[idx])

            result_image.paste(image, (0, y_offset))
            y_offset += image.size[1] + slt_space
    # progress_bar
            progress = (idx+1) / len(images) * 100
            p_var.set(progress)
            progressbar.update()
    # 포맷 옵션 처리
        file_name = "Nado." + selected_format
        save_path = os.path.join(txt_dest_path.get(), file_name)
        result_image.save(save_path)
        messagebox.showinfo("완료", "이미지가 성공적으로 저장되었습니다.")
    except Exception as err:
        messagebox.showerror("에러", err)

# 파일 프레임 (파일 추가, 선택 삭제)

file_frame = Frame(root)
file_frame.pack(fill="x", padx=5, pady=5)

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일추가", command=add_file)
btn_add_file.pack(side="left")
btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="파일삭제", command=del_file)
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

btn_dest_path = Button(path_frame, text="찾아보기", width=10, command=save)
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

btn_start = Button(run_frame, padx=5, pady=5, text = "시작", width=12, command=start)
btn_start.pack(side="right", padx=5, pady=5)



scrollbar.config(command=list_file.yview)
root.resizable(False, False)
root.mainloop()