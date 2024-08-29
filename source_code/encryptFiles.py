import  base64
import os
import rsa

def encrypt(filepath,public_key):
    '''
    函数功能：对指定路径下特定类型的文件进行加密
    :param filepath: 文件路径名
    :param public_key: 公钥
    '''
    if '.Sec' in filepath:  # 处理已加密文件的情况
        print('文件已加密，请勿重复加密！')
        return
    try:
        with open(filepath,mode='r',encoding='utf-8') as file:  # 以文本模式读取文件
            file.seek(0)  # 重置游标至文件开头处
            data=file.read(43)  # 把文件数据读取到 data中
            others=file.read()  # 继续读取文件剩余内容
            if data=='':  # 处理文件为空或读取文件失败的情况
                print('*此文件为空，无法进行加密！')
                return
    except:
        print('抱歉，无法正常读取此文件 或 此文件不存在！')
        return
    try:
        b64data=base64.b64encode(data.encode())  #  将原文件前43个字符进行base64编码成二进制数据类型
        encry_i = rsa.encrypt(b64data, public_key)  # 使用RSA算法加密
        others_list=list(base64.b64encode(others.encode()).decode())  # 将原字符串经过base64编码后再转换成列表类型
    except:
        print('抱歉，部分内容因格式原因，加密失败！')
        return
    for i in range(0,len(others_list)):  # 分类对原文件进行不同方式的加密算法
        if i%3==1:
            if ord(others_list[i]) >= 48 and ord(others_list[i]) <= 57:  # 对数字移位
                others_list[i] = chr((ord(others_list[i]) - 44) % 10 + 48)  # 循环向右移动4位
            elif ord(others_list[i]) >= 65 and ord(others_list[i]) <= 90:  # 对大写字母移位
                others_list[i] = chr((ord(others_list[i]) - 60) % 26 + 65)  # 循环向右移动5位
            elif ord(others_list[i]) >= 97 and ord(others_list[i]) <= 122:  # 对小写字母移位
                others_list[i] = chr((ord(others_list[i]) - 90) % 26 + 97)  # 循环向右移动7位
            elif others_list[i]=='+':  # 将原来的‘+’替换成‘/’
                others_list[i] = '/'
            elif others_list[i]=='/':  # 将原来的‘/’替换成‘+’
                others_list[i] = '+'
        try:
            others_list[i] = base64.b64encode(others_list[i].encode()).decode()  # 再进行一次base64编码
        except:
            print('抱歉，部分内容因格式原因，加密失败！')
            return
    others_str=''
    for i in range(0,len(others_list)):
        others_str+=others_list[i]  # 将列表中的逐个元素拼接成一个字符串
        others_str += '-'  # 每个元素之间用‘-’号隔开
    # 写入加密后的文件
    newpath=filepath+'.Sec'
    try:
        with open(newpath,mode='w',encoding='utf-8') as f:
            f.write(base64.b64encode(encry_i).decode())  # 对RSA加密后的数据再进行base64编码，将其写入存储程序数据的文件中
            f.write('@@%%&&$')  # 写入换行符，作为两部分加密内容的分隔符
            f.write(others_str)  # 写入后半部分加密后的数据
    except:
        print('无法将加密后的数据写入新文件中，加密失败！')
        return
    try:
        # 删除原始文件
        os.remove(filepath)
    except:
        print('加密成功，但无法删除加密前的文件，请检查系统权限是否正常！')
        return
    # 显示提示信息
    print("*文件加密成功~~~")
