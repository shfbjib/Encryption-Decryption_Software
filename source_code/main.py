import  base64,os,rsa
from encryptFiles import encrypt
from decryptFiles import decrypt

# 生成RSA加密算法的公钥和私钥
public_key,private_key=rsa.newkeys(2048)
ctrl_var=True # 定义控制变量
print("********************欢迎进入加密、解密工具箱~~~********************")
while(ctrl_var==True):
    print("***** 加密，请输入0 ***** 解密，请输入1 ***** 退出，请输入2 *****")
    print('温馨提示：只能输入这三个数字哦~~~')

    isInputLogical=False  # 定义判断输入是否合法的逻辑变量
    while(isInputLogical==False):  # 如果输入不合法，则要求重新输入
        try:
            choice=input('*请输入您的选择：')
            num = int(choice)  # 检验输入是否为合法数字
            if not(num==0 or num==1 or num==2):
                raise ValueError("您的输入不符合格式要求，请重新输入！")  # 触发异常
            isInputLogical=True  # 将逻辑变量的值修改为真
        except:
            print('您的输入不符合要求，请重新输入！')
    if num==2:
        exit()  # 实现退出功能
    elif num==0:
        filepath=input('*好的，请输入待加密文件的绝对路径：').strip('"')  # 输入加密文件的路径，并去除头尾的双引号
        filepath_list=list(filepath)  # 将输入的文件路径转换成列表类型
        new_filepath=''
        # 遍历路径中的每一个字符
        for i in filepath_list:
            if i=="\\":  # 判断当前字符是否为\
                i="\\\\"  # 将所有原字符串里的\改为\\
                new_filepath+=i
                continue
            new_filepath += i
        encrypt(new_filepath,public_key)  # 调用加密函数，生成加密后的文件
    else:
        filepath = input('*好的，请输入待解密文件的绝对路径：').strip('"')  # 输入加密文件的路径，并去除头尾的双引号
        filepath_list = list(filepath)  # 将输入的文件路径转换成列表类型
        new_filepath = ''
        for i in filepath_list:
            if i == "\\":  # 判断当前字符是否为\
                i = "\\\\"  # 将所有原字符串里的\改为\\
                new_filepath += i
                continue
            new_filepath += i
        decrypt(new_filepath,private_key)  # 调用解密函数，生成解密后的文件

