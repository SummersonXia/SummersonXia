
import os
import time
import threading


class LogAnalyzer_ges():
    def __init__(self, log_folder, gesture_sequence, other_gesture_keyword, gt_csv_path, result_csv_path, thread_num):
        self.log_folder = log_folder
        self.gesture_sequence = gesture_sequence
        self.other_gesture_keyword = other_gesture_keyword
        self.gt_csv_path = gt_csv_path
        self.result_csv_path = result_csv_path
        self.thread_num = thread_num

    def chunk_list(self):
        # chunk log file list in thread_num
        self.log_list = []
        self.chunked_log_list = []
        for root, _, files in os.walk(self.log_folder):
            for file in files:
                if not file.endswith(".log"):
                    continue
                self.log_list.append(file)
        log_all_num = len(self.log_list)
        chunked_list_length = log_all_num // self.thread_num
        if self.thread_num > 1:
            for i in range(self.thread_num - 1):
                self.chunked_log_list.append(self.log_list[i * chunked_list_length: (i + 1) * chunked_list_length])
            self.chunked_log_list.append(self.log_list[(i + 1) * chunked_list_length:])
        else:
            self.chunked_log_list = [self.log_list]

    def analyze_log_list(self, list_index):
        for log_name in self.chunked_log_list[list_index]:
            video_name = log_name.replace("^", "/").replace(".log", "")
            try:
                gt_line = self.gt_csv_dict[video_name]
            except:
                continue
            # get result from log
            log_gesture_result_list = [0] * len(self.gesture_sequence)
            with open(self.log_folder + os.sep + log_name) as log_file:
                for line in log_file.readlines():
                    for i in range(len(self.gesture_sequence)):
                        if self.gesture_sequence[i] in line:
                            log_gesture_result_list[i] = 1
                            break
                    else:
                        if "GESTURE_FIVE" in line:
                            log_gesture_result_list[4] = 1
                            continue
                        if self.other_gesture_keyword in line:
                            log_gesture_result_list[-1] = 1
                        if "Frame:" in line:
                            log_gesture_result_list[-1] = 1
            self.result_lines_list[list_index] += log_name + "," + video_name + "," + ",".join(
                gt_line).strip() + "," + ",".join([str(value) for value in log_gesture_result_list]) + "\n"

    def analyze_log_all(self):
        self.result_lines_list = [""] * self.thread_num
        self.gt_csv_dict = {}
        with open(self.gt_csv_path, "r") as gt_csv_file:
            for line in gt_csv_file.readlines():
                try:
                    self.gt_csv_dict[line.split(",")[0]] = line.split(",")[1:]
                except:
                    continue
        self.chunk_list()
        thread_list = []
        for i in range(self.thread_num):
            thread = threading.Thread(target=self.analyze_log_list, args=(i,))
            thread.start()
            thread_list.append(thread)
        for thread in thread_list:
            thread.join()
        result_csv_lines = "".join(self.result_lines_list)
        with open(self.result_csv_path, "w+") as result_csv_file:
            result_csv_file.write(result_csv_lines)


class LogAnalyzer_ged():
    def __init__(self, log_folder, gesture_sequence, other_gesture_keyword, gt_csv_path, result_csv_path, thread_num):
        self.log_folder = log_folder
        self.gesture_sequence = gesture_sequence
        self.other_gesture_keyword = other_gesture_keyword
        self.gt_csv_path = gt_csv_path
        self.result_csv_path = result_csv_path
        self.thread_num = thread_num

    def chunk_list(self):
        # chunk log file list in thread_num
        self.log_list = []
        self.chunked_log_list = []
        for root, _, files in os.walk(self.log_folder):
            for file in files:
                if not file.endswith(".log"):
                    continue
                self.log_list.append(file)
        log_all_num = len(self.log_list)
        chunked_list_length = log_all_num // self.thread_num
        if self.thread_num > 1:
            for i in range(self.thread_num - 1):
                self.chunked_log_list.append(self.log_list[i * chunked_list_length: (i + 1) * chunked_list_length])
            self.chunked_log_list.append(self.log_list[(i + 1) * chunked_list_length:])
        else:
            self.chunked_log_list = [self.log_list]

    def analyze_log_list(self, list_index):
        for log_name in self.chunked_log_list[list_index]:
            video_name = log_name.replace("^", "/").replace(".log", "")
            try:
                gt_line = self.gt_csv_dict[video_name]
            except:
                continue
            # get result from log
            log_gesture_result_list = [0] * len(self.gesture_sequence)
            with open(self.log_folder + os.sep + log_name) as log_file:
                for line in log_file.readlines():
                    for i in range(len(self.gesture_sequence)):
                        if self.gesture_sequence[i] in line:
                            log_gesture_result_list[i] = 1
                            break
                    else:
                        if self.other_gesture_keyword in line:
                            log_gesture_result_list[-1] = 1
                        if "Frame:" in line:
                            log_gesture_result_list[-1] = 1
            self.result_lines_list[list_index] += log_name + "," + video_name + "," + ",".join(
                gt_line).strip() + "," + ",".join([str(value) for value in log_gesture_result_list]) + "\n"

    def analyze_log_all(self):
        self.result_lines_list = [""] * self.thread_num
        self.gt_csv_dict = {}
        with open(self.gt_csv_path, "r") as gt_csv_file:
            for line in gt_csv_file.readlines():
                try:
                    self.gt_csv_dict[line.split(",")[0]] = line.split(",")[1:]
                except:
                    continue
        self.chunk_list()
        thread_list = []
        for i in range(self.thread_num):
            thread = threading.Thread(target=self.analyze_log_list, args=(i,))
            thread.start()
            thread_list.append(thread)
        for thread in thread_list:
            thread.join()
        result_csv_lines = "".join(self.result_lines_list)
        with open(self.result_csv_path, "w+") as result_csv_file:
            result_csv_file.write(result_csv_lines)


class LogAnalyzer_oms_action():
    def __init__(self, log_folder, smoke_keyword, call_keyword, gt_csv_path, result_csv_path, thread_num):
        self.log_folder = log_folder
        self.smoke_keyword = smoke_keyword
        self.call_keyword = call_keyword
        self.gt_csv_path = gt_csv_path
        self.result_csv_path = result_csv_path
        self.thread_num = thread_num

    def chunk_list(self):
        # chunk log file list in thread_num
        self.log_list = []
        self.chunked_log_list = []
        for root, _, files in os.walk(self.log_folder):
            for file in files:
                if not file.endswith(".log"):
                    continue
                self.log_list.append(file)
        log_all_num = len(self.log_list)
        chunked_list_length = log_all_num // self.thread_num
        if self.thread_num > 1:
            for i in range(self.thread_num - 1):
                self.chunked_log_list.append(self.log_list[i * chunked_list_length: (i + 1) * chunked_list_length])
            self.chunked_log_list.append(self.log_list[(i + 1) * chunked_list_length:])
        else:
            self.chunked_log_list = [self.log_list]

    def analyze_log_list(self, list_index):
        for log_name in self.chunked_log_list[list_index]:
            video_name = log_name.replace("^", "/").replace(".log", "")
            try:
                gt_line = self.gt_csv_dict[video_name]
            except:
                continue
            # get result from log
            log_action_set = set()
            with open(self.log_folder + os.sep + log_name) as log_file:
                for line in log_file.readlines():
                    if self.smoke_keyword in line:
                        log_action_set.add("smoke")
                    # elif self.drink_keyword in line:
                    #     log_action_set.add("drink")
                    elif self.call_keyword in line:
                        log_action_set.add("call")
                if not log_action_set:
                    log_action_set.add("none")
            if "none" in log_action_set:
                log_result = 0
            elif (len(log_action_set) == 1) and ("smoke" in log_action_set):
                log_result = 1
            elif (len(log_action_set) == 1) and ("drink" in log_action_set):
                log_result = 2
            elif (len(log_action_set) == 1) and ("call" in log_action_set):
                log_result = 3
            elif (len(log_action_set) == 2) and ("smoke" in log_action_set) and ("drink" in log_action_set):
                log_result = 4
            elif (len(log_action_set) == 2) and ("smoke" in log_action_set) and ("call" in log_action_set):
                log_result = 5
            elif (len(log_action_set) == 2) and ("drink" in log_action_set) and ("call" in log_action_set):
                log_result = 6
            elif len(log_action_set) == 3:
                log_result = 7
            self.result_lines_list[list_index] += log_name + "," + video_name + "," + ",".join(
                gt_line).strip() + "," + str(log_result) + "\n"

    def analyze_log_all(self):
        self.result_lines_list = [""] * self.thread_num
        self.gt_csv_dict = {}
        with open(self.gt_csv_path, "r") as gt_csv_file:
            for line in gt_csv_file.readlines():
                try:
                    self.gt_csv_dict[line.split(",")[0]] = line.split(",")[1:]
                except:
                    continue
        self.chunk_list()
        thread_list = []
        for i in range(self.thread_num):
            thread = threading.Thread(target=self.analyze_log_list, args=(i,))
            thread.start()
            thread_list.append(thread)
        for thread in thread_list:
            thread.join()
        result_csv_lines = "".join(self.result_lines_list)
        with open(self.result_csv_path, "w+") as result_csv_file:
            result_csv_file.write(result_csv_lines)


class LogAnalyzer_dms_action():
    def __init__(self, log_folder, smoke_keyword, drink_keyword, call_keyword, gt_csv_path, result_csv_path,
                 thread_num):
        self.log_folder = log_folder
        self.smoke_keyword = smoke_keyword
        self.drink_keyword = drink_keyword
        self.call_keyword = call_keyword
        self.gt_csv_path = gt_csv_path
        self.result_csv_path = result_csv_path
        self.thread_num = thread_num

    def chunk_list(self):
        # chunk log file list in thread_num
        self.log_list = []
        self.chunked_log_list = []
        for root, _, files in os.walk(self.log_folder):
            for file in files:
                if not file.endswith(".log"):
                    continue
                self.log_list.append(file)
        log_all_num = len(self.log_list)
        chunked_list_length = log_all_num // self.thread_num
        if self.thread_num > 1:
            for i in range(self.thread_num - 1):
                self.chunked_log_list.append(self.log_list[i * chunked_list_length: (i + 1) * chunked_list_length])
            self.chunked_log_list.append(self.log_list[(i + 1) * chunked_list_length:])
        else:
            self.chunked_log_list = [self.log_list]

    def analyze_log_list(self, list_index):
        for log_name in self.chunked_log_list[list_index]:
            video_name = log_name.replace("^", "/").replace(".log", "")
            try:
                gt_line = self.gt_csv_dict[video_name]
            except:
                continue
            # get result from log
            log_action_set = set()
            with open(self.log_folder + os.sep + log_name) as log_file:
                for line in log_file.readlines():
                    if self.smoke_keyword in line:
                        log_action_set.add("smoke")
                    elif self.drink_keyword in line:
                        log_action_set.add("drink")
                    elif self.call_keyword in line:
                        log_action_set.add("call")
                if not log_action_set:
                    log_action_set.add("none")
            if "none" in log_action_set:
                log_result = 0
            elif (len(log_action_set) == 1) and ("smoke" in log_action_set):
                log_result = 1
            elif (len(log_action_set) == 1) and ("drink" in log_action_set):
                log_result = 2
            elif (len(log_action_set) == 1) and ("call" in log_action_set):
                log_result = 3
            elif (len(log_action_set) == 2) and ("smoke" in log_action_set) and ("drink" in log_action_set):
                log_result = 4
            elif (len(log_action_set) == 2) and ("smoke" in log_action_set) and ("call" in log_action_set):
                log_result = 5
            elif (len(log_action_set) == 2) and ("drink" in log_action_set) and ("call" in log_action_set):
                log_result = 6
            elif len(log_action_set) == 3:
                log_result = 7
            self.result_lines_list[list_index] += log_name + "," + video_name + "," + ",".join(
                gt_line).strip() + "," + str(log_result) + "\n"

    def analyze_log_all(self):
        self.result_lines_list = [""] * self.thread_num
        self.gt_csv_dict = {}
        with open(self.gt_csv_path, "r") as gt_csv_file:
            for line in gt_csv_file.readlines():
                try:
                    self.gt_csv_dict[line.split(",")[0]] = line.split(",")[1:]
                except:
                    continue
        self.chunk_list()
        thread_list = []
        for i in range(self.thread_num):
            thread = threading.Thread(target=self.analyze_log_list, args=(i,))
            thread.start()
            thread_list.append(thread)
        for thread in thread_list:
            thread.join()
        result_csv_lines = "".join(self.result_lines_list)
        with open(self.result_csv_path, "w+") as result_csv_file:
            result_csv_file.write(result_csv_lines)


class LogAnalyzer_emotion():
    def __init__(self, log_folder, neutral_keyword, positive_keyword, negative_keyword, gt_csv_path, result_csv_path,
                 thread_num):
        self.log_folder = log_folder
        self.neutral_keyword = neutral_keyword
        self.positive_keyword = positive_keyword
        self.negative_keyword = negative_keyword
        self.gt_csv_path = gt_csv_path
        self.result_csv_path = result_csv_path
        self.thread_num = thread_num

    def chunk_list(self):
        # chunk log file list in thread_num
        self.log_list = []
        self.chunked_log_list = []
        for root, _, files in os.walk(self.log_folder):
            for file in files:
                if not file.endswith(".log"):
                    continue
                self.log_list.append(file)
        log_all_num = len(self.log_list)
        chunked_list_length = log_all_num // self.thread_num
        if self.thread_num > 1:
            for i in range(self.thread_num - 1):
                self.chunked_log_list.append(self.log_list[i * chunked_list_length: (i + 1) * chunked_list_length])
            self.chunked_log_list.append(self.log_list[(i + 1) * chunked_list_length:])
        else:
            self.chunked_log_list = [self.log_list]

    def analyze_log_list(self, list_index):
        for log_name in self.chunked_log_list[list_index]:
            video_name = log_name.replace("^", "/").replace(".log", "")
            try:
                gt_line = self.gt_csv_dict[video_name]
            except:
                continue
            # get result from log
            log_emotion_set = set()
            with open(self.log_folder + os.sep + log_name) as log_file:
                for line in log_file.readlines():
                    if self.neutral_keyword in line:
                        log_emotion_set.add("neutral")
                    elif self.positive_keyword in line:
                        log_emotion_set.add("positive")
                    elif self.negative_keyword in line:
                        log_emotion_set.add("negative")
                if not log_emotion_set:
                    log_emotion_set.add("none")
            if "none" in log_emotion_set:
                log_result = 4
            elif (len(log_emotion_set) == 1) and ("neutral" in log_emotion_set):
                log_result = 0
            elif (len(log_emotion_set) == 1) and ("positive" in log_emotion_set):
                log_result = 1
            elif (len(log_emotion_set) == 1) and ("negative" in log_emotion_set):
                log_result = 2
            elif (len(log_emotion_set) == 2) and ("positive" in log_emotion_set) and ("neutral" in log_emotion_set):
                log_result = 1
            elif (len(log_emotion_set) == 2) and ("negative" in log_emotion_set) and ("neutral" in log_emotion_set):
                log_result = 2
            elif (len(log_emotion_set) == 2) and ("positive" in log_emotion_set) and ("negative" in log_emotion_set):
                log_result = 3
            elif (len(log_emotion_set) == 3):
                log_result = 3
            self.result_lines_list[list_index] += log_name + "," + video_name + "," + ",".join(
                gt_line).strip() + "," + str(log_result) + "\n"

    def analyze_log_all(self):
        self.result_lines_list = [""] * self.thread_num
        self.gt_csv_dict = {}
        with open(self.gt_csv_path, "r") as gt_csv_file:
            for line in gt_csv_file.readlines():
                try:
                    self.gt_csv_dict[line.split(",")[0]] = line.split(",")[1:]
                except:
                    continue
        self.chunk_list()
        thread_list = []
        for i in range(self.thread_num):
            thread = threading.Thread(target=self.analyze_log_list, args=(i,))
            thread.start()
            thread_list.append(thread)
        for thread in thread_list:
            thread.join()
        result_csv_lines = "".join(self.result_lines_list)
        with open(self.result_csv_path, "w+") as result_csv_file:
            result_csv_file.write(result_csv_lines)


