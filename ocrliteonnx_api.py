#! /usr/bin/env python3
# coding=utf-8

import os
import time
import win32gui
import pyautogui

class OcrLiteOnnxApi:

    def config_runtest(self, path):
        # 修改run-test.bat中默认图片文件路径
        runtest_path = os.getcwd() + "\\run-test.bat"
        file_data = ""
        with open(runtest_path, "r", encoding="utf8") as f:
            for line in f.readlines():
                if "SET TARGET_IMG=" in line:
                    line = line.replace(line.split("=")[1], path) + "\n"
                file_data += line
        with open(runtest_path, "w", encoding="utf8") as f:
            f.write(file_data)

    def anayse_result(self):
        # 执行run-test.bat并获取其返回值[text, position, crnntime]
        os.chdir(os.getcwd())
        res = os.popen("run-test.bat", "r")
        result = res.buffer.readlines()
        TextBox, crnnTime, textLine, ocrliteonnx = [], [], [], []
        for line in result:
            trs_code = str(line, encoding="utf8").strip()
            if "TextBox[" in trs_code:
                text = trs_code.rstrip("]\n").split("),")[1] + "]"
                x1 = text.strip().split("x:")[1].split(",")[0]
                x2 = text.strip().split("x:")[2].split(",")[0]
                y2 = text.strip().split("y:")[2].split("],")[0]
                y3 = text.strip().split("y:")[3].split("],")[0]
                text_pos = (int(int(x1)/2 + int(x2)/2), int(int(y2)/2 + int(y3)/2))
                TextBox.append(text_pos)
            elif "crnnTime[" in trs_code:
                crnnTime.append(trs_code.strip(")").split("](")[1])
            elif "textLine[" in trs_code:
                textLine.append(trs_code.strip(")").split("(")[1])
            elif "FullDetectTime(" in trs_code:
                FullDetectTime = trs_code.strip(")").split("(")[1]
                ocrliteonnx.append(f"FullDetectTime:{FullDetectTime}")
                print(f"FullDetectTime:{FullDetectTime}")
        for i in range(len(TextBox)):
            ocrliteonnx.append([textLine[i], TextBox[i], crnnTime[i]])
        return ocrliteonnx

    def check_if_text_in_image(self, text, image_path=None):
        # 判断图片中是否含有指定text字段
        if image_path is not None:
            OcrLiteOnnxApi().config_runtest(path=image_path)
        image_ocr = OcrLiteOnnxApi().anayse_result()
        for line in image_ocr:
            if text in line[0]:
                print(f"图片中存在{text}字段")
                return True
        print(f"未在图片中找到{text}字段")
        return False

    def check_if_text_in_window(self, text, title_name):
        # 检测title_name窗口中是否含有text字段
        try:
            image_path = os.getcwd() + "\\image\\ocrliteonnx.PNG"
            hwnd = win32gui.FindWindow(None, title_name)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
            time.sleep(0.01)
            pyautogui.screenshot(image_path, [left, top, right - left, bottom - top])
            time.sleep(0.01)
            image_ocr = OcrLiteOnnxApi().anayse_result()
            for line in image_ocr:
                if text in line[0]:
                    print(f"{title_name}窗口中存在{text}字段")
                    return True
            print(f"{title_name}窗口中不存在{text}字段")
            return False
        except Exception as e:
            print(e)
            return False

    def get_text_position_by_image(self, text, image_path=None):
        # 返回图片中text字段的中心位置坐标
        if image_path is not None:
            OcrLiteOnnxApi().config_runtest(path=image_path)
        image_ocr = OcrLiteOnnxApi().anayse_result()
        for line in image_ocr:
            if text in line[0]:
                print(f"{text} 中心点坐标:{line[1]}")
                return line[1]
        print(f"未在图片中找到{text}字段")
        return None

    def get_text_position_in_window(self, text, title_name=None):
        # 返回指定窗口(title_name=None时则在全屏窗口中匹配text字段)中text字段的中心位置坐标，不唯一则返回第一个位置坐标
        try:
            image_path = os.getcwd() + "\\image\\ocrliteonnx.PNG"
            left, top, right, bottom = 0, 0, 0, 0
            OcrLiteOnnxApi().config_runtest(image_path)
            if title_name is not None:
                hwnd = win32gui.FindWindow(None, title_name)
                left, top, right, bottom = win32gui.GetWindowRect(hwnd)
                time.sleep(0.01)
                pyautogui.screenshot(image_path, [left, top, right-left, bottom-top])
            else:
                pyautogui.screenshot(image_path)
            time.sleep(0.01)
            image_ocr = OcrLiteOnnxApi().anayse_result()
            for line in image_ocr:
                if text in line[0]:
                    position = (left + line[1][0], top + line[1][1])
                    print(f"{text} 中心点坐标:{position}")
                    return position
            print(f"未在{title_name}窗口中找到{text}字段")
            return None
        except Exception as e:
            print(e)
            return None


if __name__ == "__main__":
    time.sleep(5)
    OcrLiteOnnxApi().get_text_position_in_window("我的手机")