# IOESDemo

## 开发环境
MacOS Mojave    
VSCode Version 1.38.1      
Python 3.7.3    
PyQT5  
QT Designer 5.12.3  

## 安装依赖
pip install PyQt5 -i https://pypi.douban.com/simple   
pip install PyQt5-tools -i https://pypi.douban.com/simple   
pip install openpyxl -i https://pypi.douban.com/simple  
pip install requests -i https://pypi.douban.com/simple  

## 通过python执行
python3 mainUI.py

## 打包为单个可执行文件
pyinstaller -F -w -i resource/logo.icns mainUI.py

## 效果预览
![](resource/demo_osx.png)

## refs:
https://www.riverbankcomputing.com/static/Docs/PyQt4/classes.html  
https://openpyxl.readthedocs.io/en/stable/  
