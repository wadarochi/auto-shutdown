# -*- coding: utf-8 -*-

from tkinter import messagebox, Frame, Button, Entry, GROOVE, END, Tk, Label, BOTTOM, RIGHT, BOTH
import subprocess


class AutoShutdown(object):
    """
    提供一个自动关机的定时任务，关机过程中会显示倒计时，此时可以取消关机
    """

    def __init__(self, count):
        super(AutoShutdown, self).__init__()
        self.pause = False
        self.count = count
        self.time = 120
        self.INTERVAL = 1000
        self.setup_ui()

    def setup_ui(self):
        """att"""
        self.root = Tk()
        self.root.title('自动关机')

        self.f1 = Frame(self.root, width=200, height=200, bg='lightblue')
        self.b1 = Button(self.f1, text='立刻关机', fg='red', bg ='white', command=self.shutdown)
        self.b2 = Button(self.f1, text='晚点再关', fg='green', bg ='white', command=self.delay)
        self.b3 = Button(self.f1, text='不要关机', fg='purple', bg ='white', command=self.exit)
        self.entry = Entry(self.root, width=10)
        self.l1 = Label(self.root, text='晚多久关？（分钟）')

        self.f2 = Frame(self.root)
        self.l2 = Label(self.f2, text='Enter Time!', relief=GROOVE)

        self.f2.pack(side=BOTTOM)
        self.entry.pack(side=RIGHT)
        self.l1.pack(side=RIGHT)
        self.l2.pack(side=BOTTOM)

        self.f1.pack(fill=BOTH)
        self.b1.pack(fill=BOTH)
        self.b2.pack(fill=BOTH)
        self.b3.pack(fill=BOTH)

    def update_timer(self):
        if self.pause:
            self.root.after(self.INTERVAL, self.update_timer)
            return
        self.count -= 1
        if self.count <= 0:
            self.shutdown()
            return
        self.l2.config(text="系统将在%d秒后自动关机" % self.count)
        self.root.after(self.INTERVAL, self.update_timer)

    def run(self):
        self.update_timer()
        self.root.mainloop()

    def delay(self):
        ttext = self.entry.get()
        try:
            self.time = int(ttext)
            if self.time <= 0:
                self.wrong_input()
                return
            self.count = self.time * 60
        except:
            self.wrong_input()
            return 1

    def wrong_input(self):
        messagebox.showerror('错误', '请输入一个正整数')
        self.entry.delete(0, END)

    def shutdown(self):
        subprocess.call(["shutdown", "-s","-f"])

    def exit(self):
        self.pause = True
        msg = messagebox.askyesno('退出', '终止自动关机？')
        if msg is True:
            self.root.destroy()
        else:
            self.pause = False


if __name__ == "__main__":
    auto_shutdown = AutoShutdown(120)
    auto_shutdown.run()
