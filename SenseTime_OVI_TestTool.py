# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SenseTime_OVI_TestTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1270, 863)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/捕获.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setAutoFillBackground(True)
        MainWindow.setStyleSheet("")
        MainWindow.setIconSize(QtCore.QSize(256, 256))
        MainWindow.setAnimated(True)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.treeWidget_functions = QtWidgets.QTreeWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.treeWidget_functions.sizePolicy().hasHeightForWidth())
        self.treeWidget_functions.setSizePolicy(sizePolicy)
        self.treeWidget_functions.setObjectName("treeWidget_functions")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_functions)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_functions)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget_functions)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        self.gridLayout.addWidget(self.treeWidget_functions, 2, 1, 3, 1)
        self.Dialog_textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.Dialog_textBrowser.sizePolicy().hasHeightForWidth())
        self.Dialog_textBrowser.setSizePolicy(sizePolicy)
        self.Dialog_textBrowser.setObjectName("Dialog_textBrowser")
        self.gridLayout.addWidget(self.Dialog_textBrowser, 4, 2, 1, 4)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.gridLayout.addWidget(self.tabWidget, 0, 2, 4, 4)
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setObjectName("treeView")
        self.gridLayout.addWidget(self.treeView, 0, 1, 2, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 3, 2)
        self.verticalLayout.addLayout(self.gridLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 26))
        self.menubar.setObjectName("menubar")
        self.menuGT = QtWidgets.QMenu(self.menubar)
        self.menuGT.setObjectName("menuGT")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        self.menu_display = QtWidgets.QMenu(self.menubar)
        self.menu_display.setObjectName("menu_display")
        MainWindow.setMenuBar(self.menubar)
        self.actionSSH = QtWidgets.QAction(MainWindow)
        self.actionSSH.setObjectName("actionSSH")
        self.actionlog_analysis = QtWidgets.QAction(MainWindow)
        self.actionlog_analysis.setObjectName("actionlog_analysis")
        self.actionStatic_Gesture = QtWidgets.QAction(MainWindow)
        self.actionStatic_Gesture.setObjectName("actionStatic_Gesture")
        self.actionDynamic_Gesture = QtWidgets.QAction(MainWindow)
        self.actionDynamic_Gesture.setObjectName("actionDynamic_Gesture")
        self.actionChild_Detection = QtWidgets.QAction(MainWindow)
        self.actionChild_Detection.setObjectName("actionChild_Detection")
        self.actionOMS_Action = QtWidgets.QAction(MainWindow)
        self.actionOMS_Action.setObjectName("actionOMS_Action")
        self.actionOMS_Safety_Belt = QtWidgets.QAction(MainWindow)
        self.actionOMS_Safety_Belt.setObjectName("actionOMS_Safety_Belt")
        self.actionOMS_PA = QtWidgets.QAction(MainWindow)
        self.actionOMS_PA.setObjectName("actionOMS_PA")
        self.actionOMS_Attribute = QtWidgets.QAction(MainWindow)
        self.actionOMS_Attribute.setObjectName("actionOMS_Attribute")
        self.actionFACE_ID = QtWidgets.QAction(MainWindow)
        self.actionFACE_ID.setObjectName("actionFACE_ID")
        self.actionDMS_Action = QtWidgets.QAction(MainWindow)
        self.actionDMS_Action.setObjectName("actionDMS_Action")
        self.actionDMS_GAZEAOI = QtWidgets.QAction(MainWindow)
        self.actionDMS_GAZEAOI.setObjectName("actionDMS_GAZEAOI")
        self.action_runanalysis = QtWidgets.QAction(MainWindow)
        self.action_runanalysis.setObjectName("action_runanalysis")
        self.action_openfile = QtWidgets.QAction(MainWindow)
        self.action_openfile.setObjectName("action_openfile")
        self.action_savefile = QtWidgets.QAction(MainWindow)
        self.action_savefile.setObjectName("action_savefile")
        self.actionNew_Project = QtWidgets.QAction(MainWindow)
        self.actionNew_Project.setObjectName("actionNew_Project")
        self.action_Functions_statistics = QtWidgets.QAction(MainWindow)
        self.action_Functions_statistics.setObjectName("action_Functions_statistics")
        self.actionOpen_Project = QtWidgets.QAction(MainWindow)
        self.actionOpen_Project.setObjectName("actionOpen_Project")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.action_Functions_GT = QtWidgets.QAction(MainWindow)
        self.action_Functions_GT.setObjectName("action_Functions_GT")
        self.action_Functions_log = QtWidgets.QAction(MainWindow)
        self.action_Functions_log.setObjectName("action_Functions_log")
        self.action_Functions_script = QtWidgets.QAction(MainWindow)
        self.action_Functions_script.setObjectName("action_Functions_script")
        self.actionRun_Script = QtWidgets.QAction(MainWindow)
        self.actionRun_Script.setObjectName("actionRun_Script")
        self.actionGenerate_GT = QtWidgets.QAction(MainWindow)
        self.actionGenerate_GT.setObjectName("actionGenerate_GT")
        self.actionMCU_Connection_Settings = QtWidgets.QAction(MainWindow)
        self.actionMCU_Connection_Settings.setObjectName("actionMCU_Connection_Settings")
        self.menuGT.addAction(self.action_Functions_GT)
        self.menuGT.addAction(self.actionGenerate_GT)
        self.menu.addAction(self.actionSSH)
        self.menu.addAction(self.actionNew_Project)
        self.menu.addAction(self.actionOpen_Project)
        self.menu.addAction(self.actionExit)
        self.menu.addAction(self.actionHelp)
        self.menu_2.addAction(self.action_Functions_script)
        self.menu_2.addAction(self.actionRun_Script)
        self.menu_2.addAction(self.actionMCU_Connection_Settings)
        self.menu_3.addAction(self.action_Functions_log)
        self.menu_3.addAction(self.actionlog_analysis)
        self.menu_display.addAction(self.action_Functions_statistics)
        self.menu_display.addAction(self.action_runanalysis)
        self.menu_display.addAction(self.action_openfile)
        self.menu_display.addAction(self.action_savefile)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuGT.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_display.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SenseAuto Cabin Smart Test Tool"))
        self.treeWidget_functions.headerItem().setText(0, _translate("MainWindow", "Functions"))
        __sortingEnabled = self.treeWidget_functions.isSortingEnabled()
        self.treeWidget_functions.setSortingEnabled(False)
        self.treeWidget_functions.topLevelItem(0).setText(0, _translate("MainWindow", "DMS"))
        self.treeWidget_functions.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "FACEID"))
        self.treeWidget_functions.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Drowsiness"))
        self.treeWidget_functions.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "GAZEAOI"))
        self.treeWidget_functions.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Distraction"))
        self.treeWidget_functions.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "DMS Action"))
        self.treeWidget_functions.topLevelItem(1).setText(0, _translate("MainWindow", "OMS"))
        self.treeWidget_functions.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "OMS Action"))
        self.treeWidget_functions.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "Gender"))
        self.treeWidget_functions.topLevelItem(1).child(2).setText(0, _translate("MainWindow", "Age"))
        self.treeWidget_functions.topLevelItem(1).child(3).setText(0, _translate("MainWindow", "Emotion"))
        self.treeWidget_functions.topLevelItem(1).child(4).setText(0, _translate("MainWindow", "Child"))
        self.treeWidget_functions.topLevelItem(1).child(5).setText(0, _translate("MainWindow", "PA"))
        self.treeWidget_functions.topLevelItem(1).child(6).setText(0, _translate("MainWindow", "Safety Seat"))
        self.treeWidget_functions.topLevelItem(2).setText(0, _translate("MainWindow", "GES"))
        self.treeWidget_functions.topLevelItem(2).child(0).setText(0, _translate("MainWindow", "Static"))
        self.treeWidget_functions.topLevelItem(2).child(1).setText(0, _translate("MainWindow", "Dynamic"))
        self.treeWidget_functions.setSortingEnabled(__sortingEnabled)
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.menuGT.setTitle(_translate("MainWindow", "GT生成"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "脚本运行"))
        self.menu_3.setTitle(_translate("MainWindow", "log分析"))
        self.menu_display.setTitle(_translate("MainWindow", "统计与显示"))
        self.actionSSH.setText(_translate("MainWindow", "SSH"))
        self.actionlog_analysis.setText(_translate("MainWindow", "Analyze Log"))
        self.actionStatic_Gesture.setText(_translate("MainWindow", "Static Gesture"))
        self.actionDynamic_Gesture.setText(_translate("MainWindow", "Dynamic Gesture"))
        self.actionChild_Detection.setText(_translate("MainWindow", "OMS Child"))
        self.actionOMS_Action.setText(_translate("MainWindow", "OMS Action"))
        self.actionOMS_Safety_Belt.setText(_translate("MainWindow", "OMS Safety Belt"))
        self.actionOMS_PA.setText(_translate("MainWindow", "OMS PA"))
        self.actionOMS_Attribute.setText(_translate("MainWindow", "OMS Attribute"))
        self.actionFACE_ID.setText(_translate("MainWindow", "DMS FACEID"))
        self.actionDMS_Action.setText(_translate("MainWindow", "DMS Action"))
        self.actionDMS_GAZEAOI.setText(_translate("MainWindow", "DMS GAZEAOI"))
        self.action_runanalysis.setText(_translate("MainWindow", "Run Analysis"))
        self.action_openfile.setText(_translate("MainWindow", "Open File"))
        self.action_savefile.setText(_translate("MainWindow", "Save File"))
        self.actionNew_Project.setText(_translate("MainWindow", "New Project"))
        self.action_Functions_statistics.setText(_translate("MainWindow", "Functoins"))
        self.actionOpen_Project.setText(_translate("MainWindow", "Open Project"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.action_Functions_GT.setText(_translate("MainWindow", "Functions"))
        self.action_Functions_log.setText(_translate("MainWindow", "Functions"))
        self.action_Functions_script.setText(_translate("MainWindow", "Functions"))
        self.actionRun_Script.setText(_translate("MainWindow", "Run Script"))
        self.actionGenerate_GT.setText(_translate("MainWindow", "Generate GT"))
        self.actionMCU_Connection_Settings.setText(_translate("MainWindow", "MCU Connection Settings"))

