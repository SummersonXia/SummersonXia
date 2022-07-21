
from SenseTime_OVI_TestTool import Ui_MainWindow
from SenseTime_UI_child_ssh_settings_func import SSH_settings_Window
from SenseTime_UI_child_MCU_Connection_settings_func import MCU_Connection_settings_Window
from SenseTime_UI_child_log_analysis_func import log_analysis_Window
from SenseTime_OVI_Diaglog import *
from SenseTime_Cabin_Service_func_run_analysis import SenseAuto_Cabin_Service_run_analysis
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
from PyQt5 import QtCore
import sys

import time

class RunThread(QThread):
    def __init__(self, count):
        super().__init__()
        self.count = count

    def run(self):
        for i in range(100):
            print('thread%s' % self.count, i, QThread().currentThreadId())
            # self.update_pb.emit(i)
            time.sleep(1)
        pass

# class DialogWindow(QMainWindow, Ui_MainWindow):
#     def __init__(self, parent=None):
#         super(DialogWindow, self).__init__(parent)
#         self.setupUi(self)
#
#     def update_progressbar(self, p_int):
#         self.progressBar.setValue(p_int)  # 更新进度条






class MainWindow(QMainWindow,Ui_MainWindow):
    # _signal=pyqtSignal(str)
    def __init__(self):
        #继承(QMainWindow,Ui_MainWindow)父类的属性
        super(MainWindow,self).__init__()
        #初始化界面组件
        self.setupUi(self)
        self.count=0

        # menubar signal connection
        self.actionNew_Project.triggered.connect(self.make_project_file)
        self.actionSSH.triggered.connect(self.ssh_settings)
        self.action_openfile.triggered.connect(self.loaddata)
        self.action_savefile.triggered.connect(self.savedata)
        self.action_Functions_statistics.triggered.connect(self.expand_functions)
        self.action_Functions_GT.triggered.connect(self.expand_functions)
        self.action_Functions_log.triggered.connect(self.expand_functions)
        self.action_Functions_script.triggered.connect(self.expand_functions)
        self.action_runanalysis.triggered.connect(self.runAnalysis)
        self.actionMCU_Connection_Settings.triggered.connect(self.MCU_Connection_Settings)
        self.actionlog_analysis.triggered.connect(self.log_analysis)

        # treeWidget signal connection
        self.treeWidget_functions.itemChanged.connect(self.treechild_state)

        # tabWidget signal connection
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

        # treeView signal connection
        self.treeView.doubleClicked.connect(self.treeview_doubleclick)


        self.treeWidget_functions.topLevelItem(0).child(0).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(1).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(2).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(3).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(0).child(4).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(0).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(1).setCheckState(0,Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(2).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(3).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(4).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(5).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(1).child(6).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(2).child(0).setCheckState(0, Qt.Unchecked)
        self.treeWidget_functions.topLevelItem(2).child(1).setCheckState(0, Qt.Unchecked)

        palette = QPalette()
        palette.setBrush(QPalette.Background, QBrush(QPixmap("./icon/SenseAuto.jpg")))
        self.tabWidget.setStyleSheet("background-color:rgb(200, 200, 200)")
        self.treeView.setStyleSheet("background-color:rgb(230, 230, 230)")
        self.treeWidget_functions.setStyleSheet("background-color:rgb(230, 230, 230)")
        self.tabWidget.setPalette(palette)
        # self.window


    def loaddata(self):
        self.loaddata_csvpath = QFileDialog.getOpenFileNames(QMainWindow(), '请选择结果文件', './',
                                                                 "csv Files(*.csv)")
        self.loaddata_csvfile=open(self.loaddata_csvpath[0][0],'r')
        self.loaddata_csvfile_ls=self.loaddata_csvfile.readlines()
        text_line=''
        for line in self.loaddata_csvfile_ls:
            text_line+=line
        self.display_loaddata(self.loaddata_csvpath[0][0], text_line)

        self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据加载完成')
        # self.Dialog_textBrowser.setText(text_line)

    def log_analysis(self):
        function=self.choosed_function
        if len(function)>0:
            self.log_analysis_child_window=log_analysis_Window(function)
            self.log_analysis_child_window.show()
        else:
            self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择分析功能')

    def savedata(self):
        pass

    def expand_functions(self):
        self.treeWidget_functions.expandAll()

    def make_project_file(self):
        self.new_project_path = QFileDialog.getExistingDirectory(QMainWindow(),'请选择项目文件夹','./')
        # print(self.new_project_path)
        try:
            os.makedirs(self.new_project_path+os.sep+'log')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'gt')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'result')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'SDK')
        except:
            pass
        try:
            os.makedirs(self.new_project_path + os.sep + 'video')
        except:
            pass
        self.treeview_project()

    def treeview_project(self):
        self.model = QFileSystemModel()
        self.project_root_path=self.new_project_path
        # print(self.project_root_path)
        self.model.setRootPath(self.project_root_path)
        self.treeView.setModel(self.model)
        self.treeView.setRootIndex(self.model.index(self.project_root_path))
        for col in range(1, 4):
            self.treeView.setColumnHidden(col, True)

    def treeview_doubleclick(self,Qmodelidx):
        clicked_file_path = self.model.filePath(Qmodelidx)
        # file_path_ls=os.listdir(file_path)
        # print(file_path)
        # print(file_path_ls)
        if not os.path.isdir(clicked_file_path):
            if clicked_file_path.endswith('.csv'):
                self.read_txt_csv(clicked_file_path)
            elif clicked_file_path.endswith('txt'):
                self.read_txt_csv(clicked_file_path)
            else:
                self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':暂不支持该格式文件')
        else:
            pass

    def read_txt_csv(self,file_path):
        self.txt_csv_file=open(file_path,'r').readlines()
        txt_csv_line=''
        for line in self.txt_csv_file:
            txt_csv_line+=line
        self.display_loaddata(file_path,txt_csv_line)

    # def set_window_test(self):
    #     self.SSH_child_window = DialogWindow()
    #     self.SSH_child_window.show()

    def ssh_settings(self):
        # app = QApplication(sys.argv)
        self.SSH_child_window = DialogWindow()
        self.SSH_child_window.show()
        self.thread = RunThread(self.set_window_test())
        self.count+=1
        self.thread.start()

        # sys.exit(app.exec_())

    def treechild_state(self,item,column):
        self.choosed_function=[]
        if item.checkState(column)==Qt.Checked:
            self.choosed_function.append(item.text(column))


    def runAnalysis(self):
        print(self.choosed_function)
        run_analysis=SenseAuto_Cabin_Service_run_analysis(self.loaddata_csvfile_ls)
        if len(self.choosed_function)<1:
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择功能')
        elif len(self.loaddata_csvfile_ls)<1:
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择有效结果文件')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='DMS Action':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS Action 结果分析中...')
            res_run_analysis=run_analysis.analyze_DMS_Action()
            sm_res_all_line=(',').join(str(i) for i in res_run_analysis[0][0])
            # print(sm_res_all_line)
            sm_res_wgh_line=(',').join(str(i) for i in res_run_analysis[0][1])
            dr_res_all_line=(',').join(str(i) for i in res_run_analysis[1][0])
            dr_res_wgh_line=(',').join(str(i) for i in res_run_analysis[1][1])
            ca_res_all_line=(',').join(str(i) for i in res_run_analysis[2][0])
            ca_res_wgh_line=(',').join(str(i) for i in res_run_analysis[2][1])
            tab_lines='         TP FN FP TN P N SUM TPR FPR PRE'+'\n'+\
                      'Smoke(all cases): '+sm_res_all_line+'\n'+'Smoke Weighted(P:N=1:3): '+sm_res_wgh_line+'\n'+\
                      'Drink(all cases): '+dr_res_all_line+'\n'+'Drink Weighted(P:N=1:3): '+dr_res_wgh_line+'\n'+ \
                      'Call(all cases): '+ca_res_all_line+'\n'+'Call Weighted(P:N=1:3): '+ca_res_wgh_line+'\n'
            # print(tab_lines)
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Distraction':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS分心检测 结果分析中...')
            res_run_analysis=run_analysis.analyze_Distraction()
            dstr_res_all_line=(',').join(str(i) for i in res_run_analysis)
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        '分析检测(all cases): ' + dstr_res_all_line
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser,time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Drowsiness':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS疲劳检测 结果分析中...')
            res_run_analysis = run_analysis.analyze_Drowsiness()
            drow_res_all_line = (',').join(str(i) for i in res_run_analysis[0])
            drow_res_wgh_line = (',').join(str(i) for i in res_run_analysis[1])
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        '疲劳检测(all cases): ' + drow_res_all_line + '\n' + \
                        '疲劳检测(P:N=1:1): '+ drow_res_wgh_line
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='GAZEAOI':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
            run_analysis.analyze_GAZEAOI()

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='OMS Action':
            self.update_textBrowser(self.Dialog_textBrowser,
                                    time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS Action 结果分析中...')
            res_run_analysis = run_analysis.analyze_OMS_Action()
            sm_res_all_line = (',').join(str(i) for i in res_run_analysis[0][0])
            # print(sm_res_all_line)
            sm_res_wgh_line = (',').join(str(i) for i in res_run_analysis[0][1])
            # dr_res_all_line = (',').join(str(i) for i in res_run_analysis[1][0])
            # dr_res_wgh_line = (',').join(str(i) for i in res_run_analysis[1][1])
            ca_res_all_line = (',').join(str(i) for i in res_run_analysis[1][0])
            ca_res_wgh_line = (',').join(str(i) for i in res_run_analysis[1][1])
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        'Smoke(all cases): ' + sm_res_all_line + '\n' + 'Smoke Weighted(P:N=1:3): ' + sm_res_wgh_line + '\n' + \
                        'Call(all cases): ' + ca_res_all_line + '\n' + 'Call Weighted(P:N=1:3): ' + ca_res_wgh_line + '\n'
            # print(tab_lines)
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Age':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS年龄检测 结果分析中...')
            res_run_analysis = run_analysis.analyze_Age()
            age_res_all_line = (',').join(str(i) for i in res_run_analysis)
            tab_lines = '         right wrong invalid sum PRE' + '\n' + \
                        '年龄检测(all cases): ' + age_res_all_line
            # print(tab_lines)
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Gender':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS性别检测 结果分析中...')
            res_run_analysis = run_analysis.analyze_Gender()
            gender_res_all_line = (',').join(str(i) for i in res_run_analysis)
            tab_lines = '         right wrong invalid sum PRE' + '\n' + \
                        '性别检测(all cases): ' + gender_res_all_line
            # print(tab_lines)
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Child':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':DMS疲劳检测 结果分析中...')
            res_run_analysis = run_analysis.analyze_Child()
            child_res_all_line = (',').join(str(i) for i in res_run_analysis[0])
            child_res_wgh_line = (',').join(str(i) for i in res_run_analysis[1])
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        '儿童检测(all cases): ' + child_res_all_line + '\n' + \
                        '儿童检测(P:N=1:1): ' + child_res_wgh_line
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='PA':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS乘客位置 结果分析中...')
            res_run_analysis = run_analysis.analyze_PA()
            pa_res_all_line = (',').join(str(i) for i in res_run_analysis)
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        '乘客位置(all cases): ' + pa_res_all_line
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Emotion':
            self.update_textBrowser(self.Dialog_textBrowser,
                                    time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS Action 结果分析中...')
            res_run_analysis = run_analysis.analyze_Emotion()
            pos_res_all_line = (',').join(str(i) for i in res_run_analysis[0])
            calm_res_all_line = (',').join(str(i) for i in res_run_analysis[1])
            neg_res_all_line = (',').join(str(i) for i in res_run_analysis[2])
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        'Positive(all cases): ' + pos_res_all_line + '\n' + \
                        'Calm(all cases): ' + calm_res_all_line + '\n' + \
                        'Negative(all cases): ' + neg_res_all_line
            # print(tab_lines)
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Safety Seat':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':OMS安全座椅 结果分析中...')
            res_run_analysis = run_analysis.analyze_Safetyseat()
            ss_res_all_line = (',').join(str(i) for i in res_run_analysis[0])
            ss_res_wgh_line = (',').join(str(i) for i in res_run_analysis[1])
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        '安全座椅(all cases): ' + ss_res_all_line + '\n' + \
                        '安全座椅(P:N=1:1): ' + ss_res_wgh_line
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='FACEID':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':功能开发中...')
            run_analysis.analyze_Faceid()

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Static':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':Static Gesture 结果分析中...')
            print(run_analysis.analyze_Ges())
            res_run_analysis=run_analysis.analyze_Ges()
            A_res_ori_line = (',').join(str(i) for i in res_run_analysis[0][0])
            A_res_wgh_line = (',').join(str(i) for i in res_run_analysis[0][1])
            B_res_ori_line = (',').join(str(i) for i in res_run_analysis[1][0])
            B_res_wgh_line = (',').join(str(i) for i in res_run_analysis[1][1])
            C_res_ori_line = (',').join(str(i) for i in res_run_analysis[2][0])
            C_res_wgh_line = (',').join(str(i) for i in res_run_analysis[2][1])
            D_res_ori_line = (',').join(str(i) for i in res_run_analysis[3][0])
            D_res_wgh_line = (',').join(str(i) for i in res_run_analysis[3][1])
            E_res_ori_line = (',').join(str(i) for i in res_run_analysis[4][0])
            E_res_wgh_line = (',').join(str(i) for i in res_run_analysis[4][1])
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        'Driver(all cases): ' + A_res_ori_line + '\n' + \
                        'Driver Weighted(1:1): ' + A_res_wgh_line + '\n' + \
                        'Codriver(all cases): ' + B_res_ori_line + '\n' + \
                        'Codriver Weighted(1:1): ' + B_res_wgh_line + '\n' + \
                        'RearLeft(all cases): ' + C_res_ori_line + '\n' + \
                        'RearLeft Weighted(1:1): ' + C_res_wgh_line + '\n'+ \
                        'RearRight(all cases): ' + D_res_ori_line + '\n' + \
                        'RearRight Weighted(1:1): ' + C_res_wgh_line + '\n' + \
                        'RearMid(all cases): ' + E_res_ori_line + '\n' + \
                        'RearMid Weighted(1:1): ' + E_res_wgh_line + '\n'
                # print(tab_lines)
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')

        elif len(self.choosed_function)==1 and len(self.loaddata_csvfile_ls)>0 and self.choosed_function[0]=='Dynamic':
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':Dynamic Gesture 结果分析中...')
            # print(run_analysis.analyze_Ged())
            res_run_analysis = run_analysis.analyze_Ged()
            A_res_ori_line = (',').join(str(i) for i in res_run_analysis[0][0])
            A_res_wgh_line = (',').join(str(i) for i in res_run_analysis[0][1])
            B_res_ori_line = (',').join(str(i) for i in res_run_analysis[1][0])
            B_res_wgh_line = (',').join(str(i) for i in res_run_analysis[1][1])
            C_res_ori_line = (',').join(str(i) for i in res_run_analysis[2][0])
            C_res_wgh_line = (',').join(str(i) for i in res_run_analysis[2][1])
            D_res_ori_line = (',').join(str(i) for i in res_run_analysis[3][0])
            D_res_wgh_line = (',').join(str(i) for i in res_run_analysis[3][1])
            E_res_ori_line = (',').join(str(i) for i in res_run_analysis[4][0])
            E_res_wgh_line = (',').join(str(i) for i in res_run_analysis[4][1])
            tab_lines = '         TP FN FP TN P N SUM TPR FPR PRE' + '\n' + \
                        'Driver(all cases): ' + A_res_ori_line + '\n' + \
                        'Driver Weighted(1:1): ' + A_res_wgh_line + '\n' + \
                        'Codriver(all cases): ' + B_res_ori_line + '\n' + \
                        'Codriver Weighted(1:1): ' + B_res_wgh_line + '\n' + \
                        'RearLeft(all cases): ' + C_res_ori_line + '\n' + \
                        'RearLeft Weighted(1:1): ' + C_res_wgh_line + '\n' + \
                        'RearRight(all cases): ' + D_res_ori_line + '\n' + \
                        'RearRight Weighted(1:1): ' + C_res_wgh_line + '\n' + \
                        'RearMid(all cases): ' + E_res_ori_line + '\n' + \
                        'RearMid Weighted(1:1): ' + E_res_wgh_line + '\n'
            # print(tab_lines)
            self.display_analysis_result(tab_lines)
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':数据分析完成')
        else:
            self.update_textBrowser(self.Dialog_textBrowser, time.strftime('%Y-%m-%d %H:%M:%S') + ':请选择单一功能')

    def display_loaddata(self,file_path,text):
        self.tab_add=QWidget()
        self.addTab_textBrowser=QTextBrowser()
        self.addTab_textBrowser.setText(text)
        self.layout_add=QHBoxLayout()
        self.layout_add.addWidget(self.addTab_textBrowser)
        self.tab_add.setLayout(self.layout_add)
        self.tabWidget.addTab(self.tab_add,file_path.strip('.csv').split('/')[-1])
        tabCount=self.tabWidget.count()
        self.tabWidget.setCurrentIndex(tabCount-1)

    def display_analysis_result(self,txt_lines):
        self.tab_add = QWidget()
        self.addTab_textBrowser = QTextBrowser()
        self.addTab_textBrowser.setText(txt_lines)
        self.layout_add = QHBoxLayout()
        self.layout_add.addWidget(self.addTab_textBrowser)
        self.tab_add.setLayout(self.layout_add)
        self.tabWidget.addTab(self.tab_add, 'result')
        tabCount = self.tabWidget.count()
        self.tabWidget.setCurrentIndex(tabCount - 1)



    def close_tab(self,index):
        self.tabWidget.removeTab(index)

    def MCU_Connection_Settings(self):
        # self.MCU_Connection_Settings_child_window = MCU_Connection_settings_Window()
        # self.MCU_Connection_Settings_child_window.show()


        self.dialog= DialogWindow(self)
        self.dialog.show()
        self.thread=RunThread(self.count)
        self.count+=1
        self.thread.start()


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

    def test(self):
        self.update_textBrowser(self.Dialog_textBrowser,'this is a test')

    # def funcion_choose_slot(self):
    #     function=self.choosed_function
    #     self._signal.emit(function)