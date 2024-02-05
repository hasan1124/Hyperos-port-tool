import tkinter
from tkinter import *
from tkinter.ttk import *
from sv_ttk import use_dark_theme


class Main(Tk):
    def __init__(self):
        super().__init__()
        self.title("澎湃自动移植工具")
        self.gui()

    def gui(self):
        Label(self, text="我心澎湃！", font=(None, 20)).pack(padx=5, pady=5)
        Separator(self).pack(padx=5, pady=5, fill=X)
        Label(self, text="底包链接", font=(None, 20)).pack(padx=5, pady=5)
        Entry(self).pack(padx=5, pady=5)
        Label(self, text="移植包链接", font=(None, 20)).pack(padx=5, pady=5)
        Entry(self).pack(padx=5, pady=5)
        Text(self).pack(padx=5, pady=5)
        Button(self, text="开始移植！").pack(padx=5, pady=5)


if __name__ == "__main__":
    app = Main()
    use_dark_theme()
    app.mainloop()
