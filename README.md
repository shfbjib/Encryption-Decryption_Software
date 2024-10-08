# 首页说明

​	大家好，这是我写的开源原创软件赛道的参赛作品，非常荣幸能得到您的浏览！

​	这是一个基于**Python 3.11.9**的项目，**Pycharm 2023.3.6(Community)**作为开发的 IDE，主要内容为编程实现一款**轻量级、具备与用户交互功能**的**文件加密解密二合一软件**，其中包括**加密文件**、**解密文件**和**退出程序**三个功能。

​	项目风格朴素简约，在这款软件中，没有眼花缭乱的装饰点缀，只有**精准高效**的加解密功能(**加密算法**是我**精心设计了很久**的)，希望大家能喜欢，最后，本款软件的**设计初衷**是，想让大家都保护好自己的文件数据，守护好你的**数据安全**！

> ​	p.s. 一个优秀的项目，离不开各位的参与与支持，欢迎大家对本项目进行**fork、pr以及其他各种合法的方式提出宝贵的意见**，感谢大家**watch、star**支持！
>

# 关于项目

## (1) 项目功能

​	本项目具有**加密文件**、**解密文件**和**退出程序**的三个功能，本项目综合运用**RSA算法(密钥长度为2048位)、ASCⅡ码的移位**等加密方法，并结合**Base64编码**，对数据进行了灵活的处理，以实现预期的加密、解密效果。关于加密、解密算法的具体内容，可以参考**源代码及其注释**。

> ​	p.s.本项目下一步**优化目标**(**欢迎大家与我分享你的实现方法**)：实现 **程序重启后仍能解密之前加密过的文件** 的功能，解决 **软件一直运行才能无限次加解密** 的问题。

## (2) 安装步骤

#### 本项目可直接下载**可执行程序软件**(免安装)，具体操作如下：

​	1.单击**Code按钮**，下方会出现**Download ZIP**选项，单击此选项，等待下载完成该项目的压缩包。

​	2.解压该压缩包，在解压后的文件里找到 **Encryption&Decryption_Software** 文件夹，双击打开，点击**Encryption&Decryption_Software.exe** 可执行程序，即可运行该软件。

> p.s.本仓库共分为三部分内容，**README文件**、**exe可执行程序**(**即Encryption&Decryption_Software文件夹**)以及**源代码包**。

## (3) 使用方法

* #### **加密文件**

  ​	在程序输入框中，输入**0**即可进入**加密模式**，接着输入要加密文件的路径地址**(tips:右键单击文件图标，选择“复制文件地址”)**，待程序运行结束后，即可看到加密后的文件(与原文件地址相同)。

  > p.s.加密文件推荐使用**txt**文本文件，**docx**和**pdf**文件暂不支持，**敬请期待后期不定期更新**！

* #### **解密文件**

  ​	在程序输入框中，输入**1**即可进入**解密模式**，接着输入要解密文件的路径地址**(tips:右键单击文件图标，选择“复制文件地址”)**，待程序运行结束后，即可看到解密后的文件(与解密前文件地址相同)。

* #### **退出程序**

  ​	在程序输入框中，输入**2**即可**退出程序**。

  > p.s. 请**不要修改加密后生成文件**的**后缀名**，否则将无法解密，后果自负！

# 结尾致谢

​	本篇文档说明到此就要结束了，感谢各位的观看与支持！祝，一切顺利！
