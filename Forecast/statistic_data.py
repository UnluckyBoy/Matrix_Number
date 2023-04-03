# ---************************************************---
# @coding: utf-8
# @Time : 2023/4/2 0002 11:58
# @Author : Matrix
# @File : statistic_data.py
# @Software: PyCharm
# ---************************************************---
import argparse
import re
from collections import Counter

from Forecast.Mean_value import LoadFile, GetDict


def GetInput():
    """
    #获取输入内容
    :return:
    """
    mStr=input("请输入:\n")
    print("输入内容:",mStr)
    result=SetData(mStr)
    return result
    pass

def SetData(mStr):
    """
    #截取文本并返回对应数据
    #mStr格式：2,35,18,32,49,9各30米
    :param mStr:
    :return:
    """

    # # test=mStr.split("各")[0]
    # # print(mStr.split("各")[0].split(","))
    # # print(re.split("\,|\，",mStr.split("各")[0]))#同时分多个条件，使用RE模块
    # result_str=re.split("\,|\，|\ |\.|\。|\-",mStr.split("各")[0])#同时分多个条件，使用RE模块
    # # result_str.append(mStr)
    # print("result_str：",result_str)
    # # resulr_dict=dict(result_str,mStr.split("各")[1])
    # # print("字典:",resulr_dict)
    number=[]
    for i in mStr:
        try:
            int(i)
            # print(i + '是数字字符')
            number.append(str(i))
            # GetNum2Str(i)
        except Exception as e:
            # print(i + '不是数字字符')
            number.append(" ")
            match i:
                case "鼠":
                    # print("鼠")
                    number.append("04 16 28 40 ")
                    pass
                case "牛":
                    # print("牛")
                    number.append("03 15 27 39 ")
                    pass
                case "虎":
                    # print("虎")
                    number.append("02 14 28 38 ")
                    pass
                case "兔":
                    # print("兔")
                    number.append("01 13 25 37 49 ")
                    pass
                case "龙":
                    # print("龙")
                    number.append("12 24 36 48 ")
                    pass
                case "蛇":
                    # print("蛇")
                    number.append("11 23 35 47 ")
                    pass
                case "马":
                    # print("马")
                    number.append("10 22 34 46 ")
                    pass
                case "羊":
                    # print("羊")
                    number.append("09 21 33 45 ")
                    pass
                case "猴":
                    # print("猴")
                    number.append("08 20 32 44 ")
                    pass
                case "鸡":
                    # print("鸡")
                    number.append("07 19 31 43 ")
                    pass
                case "狗":
                    # print("狗")
                    number.append("06 18 30 42 ")
                    pass
                case "猪":
                    # print("猪")
                    number.append("05 17 29 41 ")
                    pass
        pass
    print("number:" ,number)
    num_str="".join(number).strip(" ")
    num_list=num_str.split(" ")
    print(num_list,len(num_list))
    mMoney=num_list[-1]
    print("mMoney:",mMoney)
    num_list.pop()
    print("去除金额后:",num_list)
    value_list=[int(mMoney)]*len(num_list)
    print("value_list:",value_list)
    num_dict=dict(zip(num_list,value_list))
    print("字典内容:",num_dict)
    return num_dict
    pass

def GetNum2Str(number):
    testStr=[]
    testStr.append(number)
    print("testStr:",testStr)
    pass

def SaveFile(file_path,num_dict):
    """
    #保存数据到txt文件
    :param file_path:
    :param num_dict:
    :return:
    """
    load_file = LoadFile(file_path)
    load_dict = GetDict(load_file)
    temp = dict()
    # dict_keys类似set； | 并集
    # if num_dict.keys() & load_dict.keys():
    #     pass

    for key, value in num_dict.items():
        # str_dict=key + ':' + str(value)+"\n"
        # with open(file_path,"a+",encoding="utf-8") as wfile:
        #     wfile.write(key + ',' + str(value)+"\n")
        #     # print(test)
        #     pass
        # wfile.close()
        pass
    pass

def main(args):
    num_dict=GetInput()
    print("键值对结果:",num_dict)

    SaveFile(args.file_path,num_dict)
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str, default='./data/222.txt', help='文件地址')
    args = parser.parse_args()
    main(args)
