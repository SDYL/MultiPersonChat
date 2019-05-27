from tkinter.scrolledtext import ScrolledText
from tkinter import Toplevel, Text, Button
from tkinter import END, UNITS
from time import strftime, localtime, time


class WindowChat(Toplevel):
    def __init__(self):
        # 调用父类方法初始化窗口
        super(WindowChat, self).__init__()
        # 设置窗体宽高
        self.geometry('%dx%d' % (795, 505))
        # 设置聊天室宽高不可修改
        self.resizable(False, False)
        # 设置窗体
        self.add_widgets()

    def add_widgets(self):
        # 聊天内容显示文本框
        chat_textarea = ScrolledText(self)
        chat_textarea['width'] = 110
        chat_textarea['height'] = 30
        chat_textarea.grid(row=0, column=0, columnspan=2)
        # 添加2个标签
        chat_textarea.tag_config('green', foreground='#008B00')
        chat_textarea.tag_config('system', foreground='red')
        self.children['chat_textarea'] = chat_textarea
        # 聊天文本框
        chat_inputarea = Text(self, name='chat_inputarea')
        chat_inputarea['width'] = 100
        chat_inputarea['height'] = 7
        chat_inputarea.grid(row=1, column=0, pady=10)
        # 发送按钮
        send_button = Button(self, name='send_button')
        send_button['text'] = '发送'
        send_button['width'] = 5
        send_button['height'] = 2
        send_button.grid(row=1, column=1)

    def set_title(self,title):
        """设置窗口标题"""
        self.title('欢迎 %s 进入聊天室！' % title)

    def clear_inputs(self):
        """Remove Chat Content"""
        # Remove Input Content
        self.children['chat_inputarea'].delete(0.0, END)

    def get_inputs(self):
        """Get Chat Content"""
        return self.children['chat_inputarea'].get(0.0, END)

    def append_message(self, sender, message):
        """追加聊天内容"""
        # Get time
        send_time = strftime("%Y-%m-%d %H:%M:%S", localtime(time()))
        sender_info = '%s:  %s\n' %(sender, send_time)
        self.children['chat_textarea'].insert(END, sender_info, 'green')
        self.children['chat_textarea'].insert(END, ' ' + message + '\n')
        # 滚动条移动三个单位
        self.children['chat_textarea'].yview_scroll(3, UNITS)

    def on_window_closed(self, command):
        """窗口关闭事件处理方法"""
        self.protocol('WM_DELETE_WINDOW', command)

    def on_send_button_click(self, command):
        """发送按钮点击事件处理方法"""
        self.children['send_button']['command'] = command
