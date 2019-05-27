import re
# s1 = "11.192.10.2 吉林省 长春市 13512345678 czj@chinasofti.com"
# s2="asd@qq.com"
#
# tel = re.findall("\d{11}",s1)
# print("电话为：",tel)
# email = re.findall("\w*@\w*\.\w*",s1)
# print(email)
# ip = re.findall("\d+\.\d+\.\d+\.\d+",s1)
# print("地址为：",ip)

while(True):
    list1=[]
    list2=[]
    list3=[]
    list4=[]
    list5=[]
    name = input("请输入用户名：")
    mima = input("请输入密码：")
    email = input("请输入邮箱：")
    phone = input("请输入手机号：")
    ID = input("请输入身份证号：")
    sum = 0
    dict={}

    namenew = re.findall("^[a-zA-Z][a-zA-Z0-9_]{1,8}$",name)
    list1.append(name)
    if list1 !=namenew:
        print("请输入正确的用户名！")
        sum = sum + 1

    mimanew = re.findall("^[A-Za-z0-9]{6,8}$",mima)
    list2.append(mima)
    if list2 != mimanew:
        print("请输入正确的密码！")
        sum = sum + 1

    emailnew = re.findall("^\w*@\w*\.\w*",email)
    list3.append(email)
    if emailnew != list3:
        print("请输入正确的邮箱！")
        sum = sum + 1

    phonenew = re.findall("^1[3|4|5|7|8][0-9]{9}$",phone)
    list4.append(phone)
    if list4 != phonenew:
        print("请输入正确的电话号！")
        sum = sum + 1

    IDnew = re.findall("^\d{17}\d|x|X$",ID)
    list5.append(ID)
    if IDnew != list5:
        print("请输入正确的身份证号！")
        sum = sum+1

    if sum == 0:
        dict["用户名"]=name
        dict["密码"]=mima
        dict["邮箱"]=email
        dict["电话号"]=phone
        dict["身份证号"]=ID
        print(dict)