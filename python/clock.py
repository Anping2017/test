import time
import tkinter as tk
from tkinter import messagebox

class PomodoroTimer:
    def __init__(self, root):
        self.root = root
        self.root.title("Pomodoro Timer")
        
        self.work_duration = 25 * 60  # 默认工作时间为25分钟
        self.break_duration = 5 * 60  # 默认休息时间为5分钟
        self.working = False

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="", font=("Helvetica", 48))
        self.label.pack(pady=20)

        self.start_button = tk.Button(self.root, text="开始工作", command=self.start_work)
        self.start_button.pack()
        
        self.reset_button = tk.Button(self.root, text="重置", command=self.reset_timer)
        self.reset_button.pack()
        
        self.work_entry = tk.Entry(self.root, width=5)
        self.work_entry.insert(0, "25")
        self.work_entry.pack()
        
        self.break_entry = tk.Entry(self.root, width=5)
        self.break_entry.insert(0, "5")
        self.break_entry.pack()
        
        self.set_button = tk.Button(self.root, text="设置时间", command=self.set_times)
        self.set_button.pack()

    def start_work(self):
        if not self.working:
            self.working = True
            self.start_button.config(state="disabled")
            self.reset_button.config(state="disabled")
            self.work_countdown(self.work_duration)

    def work_countdown(self, remaining_time):
        if remaining_time <= 0:
            self.show_message("工作时间结束！", "开始休息吧！")
            self.working = False
            self.start_button.config(state="normal")
            self.reset_button.config(state="normal")
            self.break_countdown(self.break_duration)
        else:
            mins, secs = divmod(remaining_time, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            self.label.config(text=time_str)
            self.root.after(1000, self.work_countdown, remaining_time - 1)

    def break_countdown(self, remaining_time):
        if remaining_time <= 0:
            self.show_message("休息时间结束！", "准备好下一轮工作了吗？")
            self.start_work()
        else:
            mins, secs = divmod(remaining_time, 60)
            time_str = f"{mins:02d}:{secs:02d}"
            self.label.config(text=time_str)
            self.root.after(1000, self.break_countdown, remaining_time - 1)

    def reset_timer(self):
        self.working = False
        self.start_button.config(state="normal")
        self.reset_button.config(state="normal")
        self.label.config(text="")
        
    def set_times(self):
        work_time_str = self.work_entry.get()
        break_time_str = self.break_entry.get()
        
        try:
            self.work_duration = int(work_time_str) * 60
            self.break_duration = int(break_time_str) * 60
        except ValueError:
            self.show_message("输入错误", "请输入有效的分钟数")
            
    def show_message(self, title, message):
        messagebox.showinfo(title, message)

if __name__ == "__main__":
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()
