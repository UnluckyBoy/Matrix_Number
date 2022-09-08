# ---************************************************---
# @coding: utf-8
# @Time : 2022/9/7 0007 10:55
# @Author : Matrix
# @File : Pre_number.py
# @Software: PyCharm
# ---************************************************---
import argparse
import random

from Result_Arithmetic_Progression import Arithmetic_Progression


def Pre_Num():
    """
    #随机生成数字列表
    :return:
    """
    result = []
    for i in range(50):
        result.append(i)
        pass
    result.remove(0)#去除0
    # print("***生成列表***")
    # Show(result)
    return result
    pass

def Get_Num_List(index_list):
    """
    #随机预测
    :param index_list:
    :return:
    """
    result_list = []
    while(True):
        if(len(result_list)==7):
            break
            pass
        index_key = random.randint(0, len(index_list)-1)
        # print("预测下标:", index_key, "\t值:", index_list[index_key])
        result_list.append(index_list[index_key])
        index_list.pop(index_key)
        # print("***去除后***", "\t下标:", index_key)
        # Show(index_list)
        pass

    print("***预测结果***")
    Show(result_list)
    pass
def Show(index_list):
    result_str=''
    for i in range(len(index_list)):
        result_str+=str(index_list[i])+' '
        pass
    print("列表:", result_str)
    pass

####################################################Main方法入口#########################################################
def Get_Num_Result():
    index_list=Pre_Num()
    Get_Num_List(index_list)
    pass
####################################################Main方法入口#########################################################

def main(args):
    #Get_Num_Result()
    index_list=[31,3,1,38,25,10,46]
    Arithmetic_Progression(index_list)
    pass

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("--file_path",type=str,default='./data/work_macau_num.csv',help='文件路径')
    args=parser.parse_args()
    main(args)