# SZTU-autologin
SZTU深圳技术大学北区校园网自动登录脚本

觉得好用不妨点个star

## How to use?

本脚本使用python编写，使用很简单。以vscode为例说明。

1. 至少下载autologin.py和requirements.txt

2. 在终端使用`pip install -r requirements.txt`来安装脚本必须的运行库

3. 修改autologin.py中的学号和密码两行为自己的，即可运行。（更新后,请以实际代码提示为准）

## Better use

显然我们不想每次开机都先打开ide,然后再来运行登录程序(这和打开浏览器联网有什么区别)，因此我们需要将python程序**打包使用**,让电脑每次开机即可自动联网

1. 安装pyinstaller

   在vscode的终端运行

   ```
   pip install pyinstaller
   ```

2. 在终端中运行

   ```
   pyinstaller -F autologin.py
   ```

   即可生成一个会打开命令行的python程序了

   若不想看见命令行，可以改用

   ```
   pyinstaller -F -w autologin.py
   ```

   [详细打包教程](https://blog.csdn.net/libaineu2004/article/details/112612421)

3. 放入开机自启动任务

   [任务计划法](https://blog.csdn.net/baidu_38493460/article/details/118081809)

   [开机文件夹法](https://jingyan.baidu.com/article/5d368d1ebfdf1a3f60c057f8.html)

## Question

在打包模块时可能会出现找不到文件的问题

![image-20230512213139159](https://raw.githubusercontent.com/shadow-aaa/markdown_photo/main/PicGo/202305122131185.png)

使用cd命令将终端路径切换到代码保存的文件夹

如`cd D:\code`

然后再次运行pyinstaller的打包命令即可解决问题

也可参考前文的**详细打包教程**来解决问题

## THE END

本文代码来自[xia0ji233's blog](https://xia0ji233.pro/2021/12/08/%E6%A0%A1%E5%9B%AD%E7%BD%91%E6%A8%A1%E6%8B%9F%E7%99%BB%E5%BD%95/)，进行了小幅修改，原理可看文章详情。同时深澜软件的联网软件可以看看[BitSrunLoginGo](https://github.com/Mmx233/BitSrunLoginGo)，支持多平台😉
