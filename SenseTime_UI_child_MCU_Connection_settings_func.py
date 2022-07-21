
from SenseTime_UI_child_MCU_Connection_settings import Ui_Child_MCU_Connection_settings
import paramiko
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import *
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5 import QtCore

import time



class MCU_Connection_settings_Window(QMainWindow,Ui_Child_MCU_Connection_settings):
    def __init__(self):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(MCU_Connection_settings_Window,self).__init__()
        #初始化界面组件
        self.setupUi(self)

        self.setWindowTitle('MCU连接设置')

        self.pushButton_test_MCU_connection.clicked.connect(self.ConnecttoHost)
        self.pushButton_test_MCU_connection_2.clicked.connect(self.command_exec)

    def connect(self,ip,port,usr,pwd):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=ip, username=usr, password=pwd, port=port)
            self.update_textBrowser(self.textBrowser_MCU_connection, time.strftime('%Y-%m-%d %H:%M:%S') +':Got Connection')
            return client
        except Exception as ex:
            self.update_textBrowser(self.textBrowser_MCU_connection,time.strftime('%Y-%m-%d %H:%M:%S') +':Error connecting...')
            self.update_textBrowser(self.textBrowser_MCU_connection,time.strftime('%Y-%m-%d %H:%M:%S') +':' +str(ex))

    def ConnecttoHost(self):
        self.session=self.test_connection_MCU()

    def test_connection_MCU(self):
        IP_MCU=self.lineEdit_IP_MCU.text()
        port_MCU=self.lineEdit_port_MCU.text()
        usr_MCU=self.lineEdit_usr_MCU.text()
        pwd_MCU=self.lineEdit_Pwd_MCU.text()
        self.connect(IP_MCU,port_MCU,usr_MCU,pwd_MCU)

    # def treeview_project(self):
    #     self.model = QFileSystemModel()
    #     self.project_root_path=self.new_project_path
    #     # print(self.project_root_path)
    #     self.model.setRootPath(self.project_root_path)
    #     self.treeView.setModel(self.model)
    #     self.treeView.setRootIndex(self.model.index(self.project_root_path))
    #     for col in range(1, 4):
    #         self.treeView.setColumnHidden(col, True)

    def command_exec(self):
        try:
            command_line=self.textEdit.toPlainText()
            stdin, stdout, stderr = self.session.exec_command(command_line)
            return stdout.readlines()
        except Exception as ex:
            print("Error executing commands...")
            print(ex)



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