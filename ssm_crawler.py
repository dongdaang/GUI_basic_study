import keyboard
import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
import requests
from tkinter import *

class Login:
    def __init__(self, root):
        self.root = root
        
        # 사용자 정보
        self.id = ""
        self.pwd = ""
        
        # 전체 프레임
        self.login_frame = Frame(root)
        self.login_frame.pack(fill="both")
        
        # 제목
        self.title_label = Label(self.login_frame, text="New SSM Crawler", height=15)
        self.title_label.pack(fill="x", padx=5, pady=5, ipady=20)
        
        # id, pw 프레임
        self.id_frame = Frame(self.login_frame)
        self.pw_frame = Frame(self.login_frame)
        self.id_frame.pack(padx=5, pady=5)
        self.pw_frame.pack(padx=5, pady=5)
        
        self.id_label = Label(self.id_frame, text="ID")
        self.id_label.pack(fill="x", side="left", padx=5, pady=5)
        self.id_entry = Entry(self.id_frame)
        self.id_entry.pack(fill="x", side="right", padx=5, pady=5)
        
        self.pw_label = Label(self.pw_frame, text="PW")
        self.pw_label.pack(fill="x", side="left", padx=2, pady=5)
        self.pw_entry = Entry(self.pw_frame, show="*")
        self.pw_entry.pack(fill="x", side="right", padx=5, pady=5)
    
        # 로그인, 종료 버튼
        self.login_button = Button(self.login_frame, text="Login", command=self.get_user_info)
        self.exit_button = Button(self.login_frame, text="Exit", command=root.quit)
        self.login_button.pack(padx=5, pady=5)
        self.exit_button.pack(padx=5, pady=5)

    def get_user_info(self):
        self.id = self.id_entry.get()
        self.pw = self.pw_entry.get()
        if self.id == "a":
            self.login_frame.destroy()
            crawler = Crawler(self.root)
        else:
            msgbox.showwarning("로그인 실패", "아이디 혹은 비밀번호가 잘못되었습니다.")
        
    
class Crawler:
    def __init__(self, root):
        # 전체 프레임
        self.crawler_frame = Frame(root)
        self.crawler_frame.pack(fill="both")
        
        # 로그 파일 프레임
        self.logfile_frame = Frame(self.crawler_frame, height=50)
        self.logfile_frame.pack(fill="x", padx=5, pady=5)
        
        self.logfile_scrollbar = Scrollbar(self.logfile_frame)
        self.logfile_scrollbar.pack(side="right", fill="y")
        
        self.logfile_listbox = Listbox(self.logfile_frame, yscrollcommand=self.logfile_scrollbar.set)
        self.logfile_listbox.pack(fill="both", padx=5, pady=5)
        
        # 옵션 프레임
        self.option_frame = LabelFrame(self.crawler_frame, text="옵션", height=10)
        self.option_frame.pack(fill="x", padx=5, pady=5)
        
        # 1. 모드
        self.mode_label = Label(self.option_frame, text="모드")
        self.mode_label.pack(side="left", padx=5, pady=5)
        
        modes = ["전체 데이터", "도킹 실패 데이터"]
        self.mode_combobox = ttk.Combobox(self.option_frame, values=modes, width=15)
        self.mode_combobox.pack(side="left", padx=5, pady=5)
        
        # 2. 시간
        self.time_label = Label(self.option_frame, text="시간")
        self.time_label.pack(side="left", padx=5, pady=5)
        
        time = [str(i) + ":00" for i in range(24)]
        self.start_time_combobox = ttk.Combobox(self.option_frame, values=time, width=15)
        self.start_time_combobox.pack(side="left", padx=5, pady=5)
        
        self.tmp_label = Label(self.option_frame, text="~")
        self.tmp_label.pack(side="left", padx=5, pady=5)
        
        self.end_time_combobox = ttk.Combobox(self.option_frame, values=time, width=15)
        self.end_time_combobox.pack(side="left", padx=5, pady=5)
        
        # 로그 파일 다운
        self.logfile_down_label = Label(self.option_frame, text="로그 파일 다운")
        self.logfile_down_label.pack(side="left", padx=5, pady=5)
        
        yesno = ["예", "아니오"]
        self.logfile_down_combobox = ttk.Combobox(self.option_frame, values=yesno, width=5)
        self.logfile_down_combobox.pack(side="left", padx=5, pady=5)
        
        # 프로그레스 바 프레임
        self.progressbar_frame = LabelFrame(self.crawler_frame)
        self.progressbar_frame.pack(fill="x", padx=3, pady=3)
        
        p_var = DoubleVar()
        self.progressbar = ttk.Progressbar(self.progressbar_frame, maximum=100, length=150, variable=p_var)
        self.progressbar.pack(fill="x", padx=5, pady=5)
        
        # 시작 종료 버튼 프레임
        self.start_finish_button_frame = Frame(self.crawler_frame)
        self.start_finish_button_frame.pack(padx=5, pady=5)
        
        self.start_button = Button(self.start_finish_button_frame, text="시작")
        self.finish_button = Button(self.start_finish_button_frame, text="끝내기", command=root.quit)
        self.start_button.pack(padx=5, pady=5)
        self.finish_button.pack(padx=5, pady=5)
        

def main():
    root = Tk()
    root.title("New SSM Crawler")
    root.geometry("800x600")
    root.resizable(False, False)
    
    login = Login(root)
    
    root.mainloop()
    

if __name__ == "__main__":
    main()