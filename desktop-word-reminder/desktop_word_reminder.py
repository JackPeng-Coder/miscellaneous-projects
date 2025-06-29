import tkinter as tk
import json
import random
import threading
import time
from datetime import datetime
import os
import tkinter as tk

class DesktopWordReminder:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.load_words()
        self.load_birthdays()
        self.current_word = None
        self.setup_ui()
        self.start_timer()
        
    def setup_window(self):
        """设置窗口属性"""
        self.root.title("桌面单词提示")
        self.root.overrideredirect(True)  # 去除窗口边框
        self.root.attributes('-alpha', 1.0)  # 设置窗口完全不透明
        self.root.attributes('-topmost', False)  # 不置顶
        self.root.wm_attributes('-transparentcolor', 'black')  # 设置黑色为透明色
        
        # 设置窗口大小和位置（居中上方）
        window_width = 800
        window_height = 240
        screen_width = self.root.winfo_screenwidth()
        x = (screen_width - window_width) // 2
        y = 50  # 距离顶部50像素
        
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")
        self.root.configure(bg='black')
        
    def load_words(self):
        """加载词库"""
        try:
            with open('GaoKao_3500.json', 'r', encoding='utf-8') as f:
                self.words = json.load(f)
            print(f"成功加载 {len(self.words)} 个单词")
        except FileNotFoundError:
            print("词库文件未找到")
            self.words = []
        except json.JSONDecodeError:
            print("词库文件格式错误")
            self.words = []
            
    def load_birthdays(self):
        """加载生日数据"""
        try:
            with open('birthdays.json', 'r', encoding='utf-8') as f:
                self.birthdays = json.load(f)
            print(f"成功加载 {len(self.birthdays)} 个学生生日")
        except FileNotFoundError:
            print("生日文件未找到")
            self.birthdays = []
        except json.JSONDecodeError:
            print("生日文件格式错误")
            self.birthdays = []
            
    def setup_ui(self):
        """设置用户界面"""
        # 创建主框架，实现垂直居中
        main_frame = tk.Frame(self.root, bg='black')
        main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # 设置字体
        try:
            import tkinter.font as tkFont
            
            # 英文单词使用Times New Roman，支持音标显示
            word_font = tkFont.Font(family='Times New Roman', size=36, weight='bold')
            # 音标使用微软雅黑，支持中文标识和音标符号
            phonetic_font = tkFont.Font(family='Microsoft YaHei', size=24)
            # 中文释义使用微软雅黑
            meaning_font = tkFont.Font(family='Microsoft YaHei', size=24)
        except Exception as e:
            print(f"字体加载失败: {e}")
            # 如果字体加载失败，使用系统默认字体
            word_font = ('Times New Roman', 36, 'bold')
            phonetic_font = ('Microsoft YaHei', 24)
            meaning_font = ('Microsoft YaHei', 24)
        
        # 单词标签
        self.word_label = tk.Label(
            main_frame,
            text="",
            font=word_font,
            fg='white',
            bg='black',
            justify='center'
        )
        self.word_label.pack(pady=(0, 8))
        
        # 音标标签
        self.phonetic_label = tk.Label(
            main_frame,
            text="",
            font=phonetic_font,
            fg='white',
            bg='black',
            justify='center'
        )
        self.phonetic_label.pack(pady=(0, 8))
        
        # 释义标签
        self.meaning_label = tk.Label(
            main_frame,
            text="",
            font=meaning_font,
            fg='white',
            bg='black',
            justify='center',
            wraplength=750,  # 增加换行宽度
            anchor='center'  # 居中对齐
        )
        self.meaning_label.pack(pady=(0, 0))
        
        # 显示第一个单词
        self.show_random_word()
        
    def on_click(self, event):
        """点击事件处理"""
        # 如果今天有生日，点击时不做任何操作，保持显示生日祝福
        birthday_students = self.check_today_birthdays()
        if not birthday_students:
            # 只有在没有生日时才允许点击切换单词
            self.show_random_word()
        
    def check_today_birthdays(self):
        """检查今日是否有学生生日"""
        today = datetime.now().strftime("%m-%d")
        birthday_students = []
        
        for student in self.birthdays:
            if student['birthday'] == today:
                birthday_students.append(student['name'])
                
        return birthday_students
        
    def show_birthday_greeting(self, students):
        """显示生日祝福"""
        if len(students) == 1:
            greeting = f"{students[0]} 同学，生日快乐！"
        else:
            names = "、".join(students)
            greeting = f"{names} 同学，生日快乐！"
            
        # 显示生日祝福
        self.word_label.config(text=greeting)
        # self.phonetic_label.config(text="生日快乐！🎉🎂🎈")
        # self.meaning_label.config(text="祝你们在新的一岁里身体健康，学习进步，天天开心！")
        


    def show_random_word(self):
        """显示随机单词或生日祝福"""
        # 首先检查今日是否有学生生日
        birthday_students = self.check_today_birthdays()
        if birthday_students:
            # 如果是生日当天，默认只显示生日祝福
            self.show_birthday_greeting(birthday_students)
            return
            
        # 如果没有生日，显示随机单词
        if not self.words:
            return
            
        self.current_word = random.choice(self.words)
        
        # 显示单词
        self.word_label.config(text=self.current_word['name'])
        
        # 智能显示音标
        uk_phone = self.current_word.get('ukphone', '').strip()
        us_phone = self.current_word.get('usphone', '').strip()
        
        if uk_phone == us_phone and uk_phone:
            # 英式美式音标相同且不为空，直接显示
            phonetic = f"英 & 美 [{uk_phone}]"
        elif not uk_phone and us_phone:
            # 只有美式音标
            phonetic = f"美 [{us_phone}]"
        elif uk_phone and not us_phone:
            # 只有英式音标
            phonetic = f"英 [{uk_phone}]"
        elif uk_phone and us_phone and uk_phone != us_phone:
            # 两种音标都有且不同，检查长度
            full_phonetic = f"英 [{uk_phone}] / 美 [{us_phone}]"
            # 如果组合音标过长（超过30个字符），只显示英式音标
            if len(full_phonetic) > 30:
                phonetic = f"英 [{uk_phone}]"
            else:
                phonetic = full_phonetic
        else:
            # 都为空的情况
            phonetic = "[无音标]"
            
        self.phonetic_label.config(text=phonetic)
        
        # 显示释义（优化长文本处理）
        meanings = self.current_word['trans']
        
        # 限制释义数量，避免过长
        max_meanings = 3
        if len(meanings) > max_meanings:
            meanings = meanings[:max_meanings]
            
        meaning_text = '; '.join(meanings)
        
        # 如果文本过长，进行截断处理
        max_length = 120  # 最大字符数
        if len(meaning_text) > max_length:
            meaning_text = meaning_text[:max_length] + '...'
            
        self.meaning_label.config(text=meaning_text)
        
    def start_timer(self):
        """启动定时器，每分钟更换单词"""
        def timer_thread():
            last_minute = datetime.now().minute
            while True:
                current_minute = datetime.now().minute
                if current_minute != last_minute:
                    # 分钟发生变化，更换单词
                    self.root.after(0, self.show_random_word)
                    last_minute = current_minute
                time.sleep(1)  # 每秒检查一次
                
        timer = threading.Thread(target=timer_thread, daemon=True)
        timer.start()
        
    def run(self):
        """运行程序"""
        # 绑定鼠标点击事件
        self.root.bind('<Button-1>', self.on_click)
        self.root.bind('<Button-3>', lambda e: self.root.quit())
        self.root.mainloop()

if __name__ == "__main__":
    app = DesktopWordReminder()
    app.run()