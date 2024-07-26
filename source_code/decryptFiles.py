import  base64
import os
import rsa
from binascii import a2b_hex
def findSplitList(filepath,exeFilePath):
    '''
    函数功能：判断当前文件是否加密过，如果加密过，则返回其保存分割下标的列表
    :param filepath: 当前文件的路径地址
    :param exeFilePath: 保存程序数据记录的文件路径
    :return: 以整数类型表示分割下标的列表
    '''
    split_list=[]
    with open(exeFilePath,mode='r') as datafile:  # 打开程序数据记录文件
        temp_list=datafile.read().split("\n")  # 将每一条记录分成单独一个字符串
        for i in range(0,len(temp_list)):
            temp_list[i]=temp_list[i].split("*")  # 将每一个记录的分割下标分成单独一个字符串
        for j in range(0,len(temp_list)):  # 遍历查询所有的记录
            if temp_list[j][0]==filepath:  # 判断是否找到当前文件的路径地址
                # 处理temp_list[j][1]中base64编码后的字符串，并以列表的形式作为函数返回值
                split_list=temp_list[j][1].split(" ")
                split_list.pop(len(split_list)-1)  # 删除最后一个空字符串
                for k in range(0,len(split_list)):
                    '''split_list[k]=split_list[k].encode()
                    print(split_list[k])
                    split_list[k]=base64.b64decode(split_list[k])
                    print(split_list[k])
                    print(split_list[k].decode())
                    print(int(str(split_list[k])))'''
                    split_list[k]=int(base64.b64decode(split_list[k].encode()).decode())  # 将base64编码后的字符串解码，回到数字类型
                # 将记录程序数据的文件中相应加密记录删除
                with open(exeFilePath, mode='r') as datafile:  # 打开程序数据记录文件
                    l = datafile.readlines()   # 逐行读取文件里的内容，并保存在列表中
                    l.pop(j)  # 删除相应的加密记录
                    l_str=' '.join(l)  # 将列表中所有内容拼接成完整的字符串
                with open(exeFilePath, mode='w') as datafile:  # 打开程序数据记录文件
                    datafile.write(l_str)   # 将修改后的记录写入程序数据文件
                return split_list  # 查找成功，返回解码后存储分割下标的列表
            if j==len(temp_list)-1:  # 判断当前记录的地址是否为最后一条
                return []  # 查找失败，返回空列表

def decrypt(filepath,private_key,exeFilePath):
    '''
    函数功能：对当前目录下的特定类型文件进行解密
    :param filepath: 文件路径名
    :param private_key: 私钥
    :param exeFilePath: 保存分割下标的文件路径
    '''
    try:
        with open(filepath,mode='r') as f:
            contents:str=f.read()  # 读取文件的内容
    except:  # 读取文件失败直接退出函数
        print("抱歉，无法读取指定路径的文件!")  # 处理无法读取指定路径的文件或路径不存在的异常情况
        print('\n')
        return
    split_list=findSplitList(filepath,exeFilePath)  # 从保存分割下标的文件中提取出base64编码后的下标记录
    if split_list==[]:
        print("该文件未加密，无法进行解密！")  # 处理当前文件未加密的情况
        print('\n')
        return
    splited_list=[]  # 创建用于存放分割后字符串的列表
    splited_list.append(contents[0:split_list[0]+1])  # 分割第一个子串
    # 依次进行中间子串的分割
    for i in range(1,len(split_list)):
        splited_list.append(contents[split_list[i-1]+1:split_list[i]+1])  # 将分割形成的新子串存储到列表中
    if not(split_list[len(split_list)-1]+1==len(contents)):
        splited_list.append(contents[split_list[len(split_list)-1]+1:len(contents)])  # 分割最后一个子串
    # 逐个解密分割后的子串
    for i in range(0,len(splited_list)):
        if i%3==0:
            pass
        elif i%3==1:
            splited_list[i] = chr(ord(splited_list[i])-4)  # 将当前位置处字符的ASC码值向前平移4位
        else:
            if not(len(splited_list[i])%2==0):  # 如果十六进制字符串的长度为奇数时，在前面补一个0，使其正常转换成bytes类型
                splited_list[i]='0'+splited_list[i]
            decry_i=rsa.decrypt(a2b_hex(splited_list[i]),private_key) # 使用RSA算法解密
            splited_list[i]=decry_i.decode()  # 将原位置处的字符替换为相应的密文
    decryptedFilePath=filepath.replace('.Sec','')  # 更改解密后文件名后缀
    # 写入解密后的文件
    with open(decryptedFilePath,mode='w') as f:
        b64str=''
        for i in range(0,len(splited_list)):
            b64str+=splited_list[i]  # 将分割后得到的列表组成一个完整的字符串
        f.write(base64.b64decode(b64str).decode())  # 将用base64解码后的内容写入文件中
    # 删除加密得到的文件
    os.remove(filepath)
    # 显示提示信息
    print("文件解密成功~~~")
    print('\n')