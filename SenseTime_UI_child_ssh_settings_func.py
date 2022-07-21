
from SenseTime_UI_child_SSH_settings import Ui_Child_SSH_settings
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import *
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

import time



class SSH_settings_Window(QMainWindow,Ui_Child_SSH_settings):
    def __init__(self):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(SSH_settings_Window,self).__init__()
        #初始化界面组件
        self.setupUi(self)

        self.setWindowTitle('SSH连接设置')

        self.pushButton.clicked.connect(self.test)

    def test(self):
        self.update_textBrowser(self.textBrowser,'this is a test')


    def update_textBrowser(self, textBrowser, addtext="..."):
        """
        文本框追加信息
        :param textBrowser: 文本框句柄
        :param addtext: 需要添加的文本
        :return:
        """
        textBrowser.append(addtext)  # 文本框逐条添加数据
        # textBrowser.append("\n")
        textBrowser.moveCursor(textBrowser.textCursor().End)  # 文本框显示到底部
        QApplication.processEvents()  # 刷新窗口