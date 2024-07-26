import  base64
import os
import rsa
from binascii import b2a_hex
def encrypt(filepath,public_key,exeFilePath):
    '''
    函数功能：对当前目录下的特定类型文件进行加密
    :param filepath: 文件路径名
    :param public_key: 公钥
    :param exeFilePath: 长久储存分割下标数据的文件路径
    '''
    try:
        with open(filepath,mode='rb') as file:  # 以二进制方式读取文件
            data=file.read(83).strip()  # 把文件数据保存到 data: bytes类型
            if data==b'':
                return
            b64data=base64.b64encode(data).decode()  # 得到原文件base64编码后字符串格式
            b64list=list(b64data)  # 将base64字符串转换成列表类型
    except:
        print("抱歉，无法打开指定路径的文件!")  # 处理无法打开指定路径的文件或路径不存在的异常情况
        print('\n')
        return
    for i in range(0,len(b64list)):  # 分类对原文件进行不同方式的加密算法
        if i%3==0:
            pass
        elif i%3==1:
            b64list[i]=chr(ord(b64list[i])+4)  # 将当前位置处字符的ASC码值向后平移4位
        else:
            encry_i=rsa.encrypt(bytes(b64list[i],encoding='utf-8'),public_key)  # 使用RSA算法加密
            b64list[i]=b2a_hex(encry_i).decode()  # 将原位置处的字符替换为相应的密文
    split_list=[]  # 创建存储解密时每一个分割下标的列表
    # 写入加密后的文件
    with open(filepath+".Sec",mode='wb') as f:  # 以二进制方式写入文件
        temp_len=0  # 定义存储每一次分割下标值的变量
        for i in range(0,len(b64list)):  # 遍历所有要分割的位置
            temp_len+=(len(b64list[i])-1)  # 更新下一个分割下标
            split_list.append(temp_len)  # 存储解密时每一个分割下标
            temp_len+=1
            f.write(bytes(b64list[i],encoding='utf-8'))  # 将加密后的内容覆盖文件的原来内容
    for i in range(0,len(split_list)):
        split_list[i]=base64.b64encode(str(split_list[i]).encode())  # 将数字转换成base64编码
    with open(exeFilePath,mode='a') as exeFile:
        exeFile.write(filepath+'.Sec'+'*')  # 将原文件的路径写入存储程序数据的文件中
        for i in split_list:
            exeFile.write(i.decode()+' ')  # 将base64编码写入存储程序数据的文件中，并与原文件的路径组成键值对
        exeFile.write('\n')  # 写入一个换行符
    # 删除原始文件
    os.remove(filepath)
    # 显示提示信息
    print("文件加密成功~~~")
    print('\n')
