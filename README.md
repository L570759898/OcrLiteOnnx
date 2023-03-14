原项目地址：https://github.com/benjaminwan/OcrLiteOnnx

本项目是基于原项目编译好后的OcrLiteOnnx文字识别系统，可以实现提取图片中的文字及文字中心点坐标等功能。

目录结构：
![image](https://user-images.githubusercontent.com/86114552/224941799-f801b279-6d8c-499d-aa35-8a3e0e58a658.png)
image目录中ocrliteonnx.PNG文件是需要识别的图片文件，默认位置设置在这个目录下，也可以自行更改（同时需要修改run-test.bat中的图片路径）。
models目录中存放已经训练好了的模型。
win_x64目录中存放已经编译好之后的exe文件。

使用方法：
通过调用run-test.bat批处理文件，可以将/image/ocrliteonnx.PNG路径图片中的文字识别出来，并保存到ocrliteonnx.PNG-result.txt中，以下检测文字是否存在以及获取图片中文字中心点坐标均是通过对ocrliteonnx.PNG-result.txt文件进行解析得到的结果。

在全屏窗口中匹配"我的手机"字段，并返回该字段中心的坐标，示例如下：

FullDetectTime:2559.871300ms 
我的手机 中心点坐标:(1091, 701)

![image](https://user-images.githubusercontent.com/86114552/224943108-e0fe9321-7c0f-41a9-af0e-1bddd67fe5a7.png)

图片文字识别示例（其中有极个别文字识别错误，放大文字字体后可以正常识别出来）：
![image](https://user-images.githubusercontent.com/86114552/224942332-b2df8dc2-9bca-4871-a690-939228ce781b.png)
![image](https://user-images.githubusercontent.com/86114552/224942369-c03c2e58-c8de-4655-9405-0116689609c9.png)
