原项目地址：https://github.com/benjaminwan/OcrLiteOnnx

本项目是基于原项目编译好后的OcrLiteOnnx文字识别系统，可以实现提取图片中的文字及文字中心点坐标等功能。

目录结构：
image目录中ocrliteonnx.PNG文件是需要识别的图片文件，默认位置设置在这个目录下，也可以自行更改（同时需要修改run-test.bat中的图片路径）。
models目录中存放已经训练好了的模型。
win_x64目录中存放已经编译好之后的exe文件。

使用方法：
通过调用run-test.bat批处理文件，可以将/image/ocrliteonnx.PNG路径图片中的文字识别出来，并保存到ocrliteonnx.PNG-result.txt中，以下检测文字是否存在以及获取图片中文字中心点坐标均是通过对ocrliteonnx.PNG-result.txt文件进行解析得到的结果。
