chcp 65001

SET TARGET_IMG=D:\OcrLiteOnnx\image\ocrliteonnx.PNG

@ECHO OFF
@SETLOCAL
echo "Setting the Number of Threads=%NUMBER_OF_PROCESSORS% Using an OpenMP Environment Variable"
set OMP_NUM_THREADS=%NUMBER_OF_PROCESSORS%

if not exist %TARGET_IMG% (
echo "找不到待识别的目标图片：%TARGET_IMG%，请打开本文件并编辑TARGET_IMG"
PAUSE
exit
)

SET EXE_PATH=%~dp0\win_x64

%EXE_PATH%\OcrLiteOnnx.exe --version
%EXE_PATH%\OcrLiteOnnx.exe --models models ^
--det dbnet.onnx ^
--cls angle_net.onnx ^
--rec crnn_lite_lstm.onnx ^
--keys keys.txt ^
--image %TARGET_IMG% ^
--numThread %NUMBER_OF_PROCESSORS% ^
--padding 0 ^
--maxSideLen 0 ^
--boxScoreThresh 0.6 ^
--boxThresh 0.3 ^
--unClipRatio 2.0 ^
--doAngle 1 ^
--mostAngle 1

echo.
GOTO:EOF

@ENDLOCAL