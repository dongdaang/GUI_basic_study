from tkinter import *

class SampleApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

class StartPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Label(self, text="Start page", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go to page one",
                  command=lambda: master.switch_frame(PageOne)).pack()
        Button(self, text="Go to page two",
                  command=lambda: master.switch_frame(PageTwo)).pack()

class PageOne(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='blue')
        Label(self, text="Page one", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

class PageTwo(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        Frame.configure(self,bg='red')
        Label(self, text="Page two", font=('Helvetica', 18, "bold")).pack(side="top", fill="x", pady=5)
        Button(self, text="Go back to start page",
                  command=lambda: master.switch_frame(StartPage)).pack()

if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()