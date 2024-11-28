import ctypes
import hashlib
import tkinter
from tkinter import Toplevel, StringVar, messagebox
from tkinter.ttk import *

import requests

from app_logger import logger


class LoginDialog(Toplevel):
    """登陆为知笔记 对话框"""

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.title('登陆为知笔记')

        # 窗口宽度
        self.window_width = 300
        # 窗口高度
        self.window_height = 120
        # 初始化窗口大小和位置
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) / 2
        y = (screen_height - self.window_height) / 2
        self.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height, x, y))
        # 不允许调整大小
        self.resizable(False, False)

        # 登录地址
        self.url = "https://as.wiz.cn/as/user/login"
        self.username = StringVar(value=r'')
        self.password = StringVar(value=r'')

        # ---------------------------------------
        # 用户名
        row = 1
        Label(self, text=r'用户名：') \
            .grid(row=row, column=1, padx=5, pady=5, sticky=tkinter.E)

        self.usr_entry = Entry(self, textvariable=self.username)
        self.usr_entry.grid(row=row, column=2, columnspan=2, padx=5, pady=5,
                            sticky=tkinter.N + tkinter.E + tkinter.W)
        self.usr_entry.bind('<Return>', self.username_enter)
        self.usr_entry.focus()

        # ---------------------------------------
        # 密码
        row = row + 1
        Label(self, text=r'密 码：') \
            .grid(row=row, column=1, padx=5, pady=5, sticky=tkinter.E)

        self.pwd_entry = Entry(self, show='*', textvariable=self.password)
        self.pwd_entry.grid(row=row, column=2, columnspan=2, padx=5, pady=5,
                            sticky=tkinter.N + tkinter.E + tkinter.W)
        self.pwd_entry.bind('<Return>', self.password_enter)

        # ---------------------------------------
        # 登录按钮
        row = row + 1
        Button(self, text=r'登 录', command=self.login) \
            .grid(row=row, column=2, padx=5, pady=5,
                  sticky=tkinter.N + tkinter.E + tkinter.W)
        Button(self, text=r'取 消', command=self.close) \
            .grid(row=row, column=3, padx=5, pady=5,
                  sticky=tkinter.N + tkinter.E + tkinter.W)

        # 注册关闭按钮事件
        self.protocol('WM_DELETE_WINDOW', self.close)

        self.mainloop()

    def username_enter(self, event):
        self.pwd_entry.focus()

    def password_enter(self, event):
        self.login()

    # 调用登录接口
    def login(self):
        data = {
            'username': self.username.get(),
            'password': self.password.get()
        }
        headers = {
            'api-version': 'V1'
        }

        try:
            rsp = requests.post(url=self.url, data=data, headers=headers).json()
            if 200 == rsp.get('code'):
                # 显示主窗口
                self.master.deiconify()
                # 隐藏登录窗口
                self.withdraw()
            else:
                logger.error('登录失败：用户名或密码错误，请重试！')
                messagebox.showinfo('登录失败', r'用户名或密码错误，请重试！')
        except Exception as e:
            logger.error('登录失败：无法连接到为知笔记：%s', e)
            messagebox.showinfo('登录失败', r'无法连接到为知笔记！')

    # 点击右上角关闭按钮时调用
    def close(self):
        self.master.destroy()
