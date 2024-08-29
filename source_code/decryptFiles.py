import  base64
import os
import rsa

def decrypt(filepath,private_key):
    '''
    # 函数功能：对指定路径下的特定类型文件进行解密
    # :param filepath: 文件路径名
    # :param private_key: 私钥
    '''
    if not '.Sec' in filepath:  # 处理文件未加密的情况
        print('文件未加密，无法进行解密！')
        return
    try:
        with open(filepath,mode='r',encoding='utf-8') as f:
            f.seek(0)  # 重置游标至文件开头处
            div = f.read().index('@@%%&&$')  # 查找分隔符下标
            f.seek(0)  # 重置游标至文件开头处
            contents=f.read(div)  # 读取文件里前半部分加密过的内容
            f.seek(div+7)  # 跳到文件里未加密内容的位置
            rest=f.read()  # 读取剩余全部内容
    except:
        print("*抱歉，无法正常读取指定路径的此文件 或 此文件不存在!")  # 处理无法读取指定路径的文件或路径不存在的异常情况
        return
    try:
        encri=base64.b64decode(contents.encode())  # 将前半部分进行base64解码
        decry=rsa.decrypt(encri,private_key)  # 对前半部分内容进行解密
        forehalf=base64.b64decode(decry).decode()  # 保存解密后的数据
        rest_list=rest.split('-')  # 将字符串按照‘-’进行拆分
        rest_list.pop(-1)  # 删除最后的空串元素
    except:
        print('抱歉，部分内容因格式原因，解密失败！')
        return

    # 逐个解密分割后的子串
    for i in range(0,len(rest_list)):
        try:
            contents_bytes = base64.b64decode(rest_list[i].encode())  # 对相应位置处的字符进行base64解码
            rest_list[i] = contents_bytes.decode()  # 将解密后原文记录到相应位置中
        except:
            print('抱歉，部分内容因格式原因，解密失败！')
            return
        if i%3==1:
            if ord(rest_list[i])>=48 and ord(rest_list[i])<=57:  # 对数字复位
                rest_list[i]=chr((ord(rest_list[i])-42)%10+48)  # 循环向左移动4位
            elif ord(rest_list[i])>=65 and ord(rest_list[i])<=90:  # 对大写字母复位
                rest_list[i] = chr((ord(rest_list[i]) -44) % 26 + 65)  # 循环向左移动5位
            elif ord(rest_list[i]) >= 97 and ord(rest_list[i]) <= 122:  # 对小写字母复位
                rest_list[i] = chr((ord(rest_list[i]) -78) % 26 + 97)  # 循环向左移动7位
            elif rest_list[i]=='+':  # 将原来的‘+’替换成‘/’
                rest_list[i]='/'
            elif rest_list[i]=='/':  # 将原来的‘/’替换成‘+’
                rest_list[i]='+'
    try:
        rest=''.join(rest_list)  # 重新拼接成完整的字符串
        rest_text=base64.b64decode(rest.encode()).decode()  # 再进行一次base64解码
        decryptedFilePath=filepath.replace('.Sec','')  # 更改解密后文件名后缀
        # 写入解密后的文件
        with open(decryptedFilePath,mode='w',encoding='utf-8') as f:
            f.write(forehalf)  # 将前半部分原文写入文件中
            f.write(rest_text)  # 将后半部分原文写入文件中
    except:
        print('无法将解密后的数据写入新文件中，解密失败！')
        return
    try:
        # 删除加密得到的文件
        os.remove(filepath)
    except:
        print('解密成功，但无法删除解密前的文件，请检查系统权限是否正常！')
        return
    # 显示提示信息
    print("*文件解密成功~~~")
