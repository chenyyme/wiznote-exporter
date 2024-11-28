import os.path
import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askdirectory
from tkinter.ttk import *

from login_dialog import LoginDialog

version = 'v0.1'


class AppWindow(Tk):
    """ 应用窗体 """

    def __init__(self):
        super().__init__()
        self.title("为知笔记批量导出")
        self.copy_right = '为知笔记批量导出 ' + version + ' \n\n版权所有 © alexc'

        self.window_width = 600
        self.window_height = 480
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.window_width) / 2
        y = (screen_height - self.window_height) / 2
        # 窗口大小和位置
        self.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height, x, y))
        # 不允许改变窗体大小
        self.resizable(False, False)
        # 初始化界面
        self._init_widgets()

    # ---------------------------------------------------------------------------------------------
    # 界面初始化
    # ---------------------------------------------------------------------------------------------

    def _init_widgets(self):
        width = self.window_width - 20
        height = self.window_height - 70
        row = 0
        # ---------------------------------------
        # 登录
        Button(self, text=r'登 录', command=self._show_login_dialog) \
            .grid(row=row, column=2, padx=5, pady=5,
                  sticky=tkinter.N + tkinter.E + tkinter.W)

        # ---------------------------------------
        # 标签页容器
        row += 1
        self.notebook = Notebook(self, style='my.TNotebook', width=width, height=height)
        self.notebook.grid(row=row, column=1, columnspan=3, padx=10, pady=10)

        # ---------------------------------------
        # 导出笔记
        self.tab_export_note = Frame(self.notebook, width=width, height=height)
        self.tab_export_note.grid(row=1, column=1, padx=5, pady=5)
        self._init_tab_gen_docs(self.tab_export_note)
        self.notebook.add(self.tab_export_note, text=r'导出笔记')

        # ---------------------------------------
        # 运行配置
        self.tab_app_config = Frame(self.notebook, width=width, height=height)
        self.tab_app_config.grid(row=1, column=1, padx=5, pady=5)
        self._init_tab_app_config(self.tab_app_config)
        self.notebook.add(self.tab_app_config, text=r'运行配置')

        # ------------------------------------
        # 进度条
        row += 1
        self.progress_bar = Progressbar(self, orient=HORIZONTAL, length=width, mode="determinate")
        self.progress_bar.grid(row=row, column=1, columnspan=3,
                               sticky=tkinter.N + tkinter.E + tkinter.W)
        self.progress_bar['maximum'] = 100
        self.progress_bar['value'] = 0

    def _show_login_dialog(self):
        login_dialog = LoginDialog(self)

    def _init_tab_gen_docs(self, master):
        """ 文件生成 页面布局初始化 """
        pass

    def _init_tab_app_config(self, master):
        """ 运行配置 页面布局初始化"""
        master.bind('<FocusIn>', self.on_active_tab_app_config)
        master.bind('<FocusOut>', self.on_deactive_tab_app_config)


    def on_active_tab_app_config(self, event):
        pass

    def on_deactive_tab_app_config(self, event):
        pass

    # ---------------------------------------------------------------------------------------------
    # 进度条 辅助函数
    # ---------------------------------------------------------------------------------------------

    def _init_progress(self, maximum):
        self.progress_bar['maximum'] = maximum
        self.progress_bar['value'] = 0
        self.progress_bar.update()


    def _update_progress(self, count):
        value = self.progress_bar.cget("value")
        maximum = self.progress_bar.cget("maximum")
        if value <= maximum:
            self.progress_bar['value'] = count
            self.progress_bar.update()
