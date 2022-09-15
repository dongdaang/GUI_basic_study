from tkinter import *

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")

# 메뉴
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_edit = Menu(menu, tearoff=0)
menu_write = Menu(menu, tearoff=0)
menu_view = Menu(menu, tearoff=0)
menu_help = Menu(menu, tearoff=0)
menu_file.add_command(label="열기")
menu_file.add_command(label="저장")
menu_file.add_command(label="끝내기")

menu.add_cascade(label="파일", menu=menu_file)
menu.add_cascade(label="편집", menu=menu_edit)
menu.add_cascade(label="서식", menu=menu_write)
menu.add_cascade(label="보기", menu=menu_view)
menu.add_cascade(label="도움말", menu=menu_help)

# 텍스트

txt = Text(root, width=640, height=480)
txt.pack()


root.config(menu=menu)
root.mainloop()