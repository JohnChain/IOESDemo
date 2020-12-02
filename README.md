# IOESDemo
## 功能介绍
1. 图片预览
2. 对图片做base64后构造协议http json请求(支持local debug模式存入本地文件)
3. 支持手动填入（x, y, w, h）参数，在预览的图片中画标识矩形框
4. 根据接收到的http json回复，在相应图片中使用不同颜色的矩形框标出图片中的不同目标
5. 鼠标悬浮于目标矩形框区域，显示预览窗口展示目标参数
6. 支持将所有图片的json回复信息导出到Excel表格
7. 预览图片自适应自窗口大小(or 支持放大缩小)
8. 记录日志到文件
9. 支持logo应用图标
10. 支持双击目标在左下侧框中显示单个目标输出字段信息
11. 其他彩蛋 >.....<

#### TODO
1. IAS 协议
2. 鼠标悬浮于目标矩形框区域，显示目标截图的预览图

## 开发环境
MacOS Mojave    
VSCode Version 1.38.1      
Python 3.7.3    
PyQT5  
QT Designer 5.12.3  
logzero 

## 安装依赖
pip install PyQt5 -i https://pypi.douban.com/simple   
pip install PyQt5-tools -i https://pypi.douban.com/simple   
pip install openpyxl -i https://pypi.douban.com/simple  
pip install requests -i https://pypi.douban.com/simple  

## 更新UI
pyuic5 IOESDemo.ui -o IOESDemo.py

## 通过python执行
python3 mainUI.py

## 打包为单个可执行文件
MacSO: pyinstaller -F -w -i resource/logo.icns mainUI.py  
Windows: pyinstaller -F -w -i resource/logo.ico mainUI.py
## 效果预览
![](resource/demo_osx.png)

## refs:
https://www.riverbankcomputing.com/static/Docs/PyQt4/classes.html   
https://openpyxl.readthedocs.io/en/stable/  
https://www.cnblogs.com/hester/p/11460121.html  
https://github.com/metachris/logzero    
