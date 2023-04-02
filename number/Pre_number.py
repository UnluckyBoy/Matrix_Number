# ---************************************************---
# @coding: utf-8
# @Time : 2022/9/7 0007 10:55
# @Author : Matrix
# @File : Pre_number.py
# @Software: PyCharm
# ---************************************************---
import argparse
import random

from Result_Arithmetic_Progression import Arithmetic_Progression, Do_Random_List, Get_Blue_Fun1, Get_Blue_Fun2, \
    Get_Blue_Fun3, Get_Blue_Fun4, Get_Blue_Fun5, Get_Blue_Fun6, Get_Blue_Fun7, Get_Blue_Fun8, Get_List_MaxRepeat

##########################################################数据操作模块####################################################
from Forcast_double_ball import Get_Double_Ball, DoForecast, Get_Next_Index


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

def Pre_Blue_Num():
    """
    #随机生成16个篮数
    :return:
    """
    result = []
    for i in range(17):
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
    print("显示结果列表:", result_str)
    pass

def Get_Remove_duplicate(index_list):
    """
    #去重list中重复项
    :param index_list:
    :return:
    """
    result_Remove_duplicate=[]
    for x in index_list:
        if x not in result_Remove_duplicate:
            result_Remove_duplicate.append(x)
        pass

    return result_Remove_duplicate
    pass

##########################################################数据操作模块####################################################

####################################################双色球模块#########################################################
def Get_Num_Result():
    index_list=Pre_Num()
    Get_Num_List(index_list)
    pass

def Get_Double_Num(args):
    """
    #双色球模块
    :param args:
    :return:
    """
    print("***红球预测***")
    index_list = [2,6,7,11,14,33,8]
    result_list = Arithmetic_Progression(index_list)
    result_list = Get_Remove_duplicate(result_list)  # 去重
    Show(result_list)
    # print("************随机生成************")
    # result_list=Do_Random_List(result_list)
    # Show(result_list)
    # print("************随机生成************")

    print("******篮球预测******")
    index_double_list = [2,6,7,11,14,33,8]#上一期
    index_double_list_last = [4,13,17,18,28,29,6]  # 上上一期4,5,10,13,30,31,14
    blue_list=Pre_Blue_Num()
    blue_list=Get_Blue_Fun1(index_double_list,blue_list)
    blue_list=Get_Blue_Fun2(index_double_list,blue_list)
    blue_list=Get_Blue_Fun3(index_double_list,blue_list)
    blue_list=Get_Blue_Fun4(index_double_list, blue_list)
    blue_list=Get_Blue_Fun5(index_double_list, blue_list)
    blue_list=Get_Blue_Fun6(index_double_list, blue_list)
    blue_list=Get_Blue_Fun7(index_double_list, blue_list)
    blue_list=Get_Blue_Fun8(index_double_list,index_double_list_last,blue_list)

    # Get_Double_Ball(args,index_double_list)
    pass
def Get_Highest_probability(args):
    """
    #计算每个中下一次出现的概率
    :param num:上一次的号码
    :param num_index:下标
    :return:
    """
    index_list=[8,14,26,27,30,33,1]#上一期

    result_num_01 = DoForecast(args.double_file_path, 0)
    result_num_02 = DoForecast(args.double_file_path, 1)
    result_num_03 = DoForecast(args.double_file_path, 2)
    result_num_04 = DoForecast(args.double_file_path, 3)
    result_num_05 = DoForecast(args.double_file_path, 4)
    result_num_06 = DoForecast(args.double_file_path, 5)
    result_num_07 = DoForecast(args.double_file_path, 6)

    result_index_01 = Get_List_MaxRepeat(Get_Next_Index(index_list[0], result_num_01)) # 不去重
    result_index_02 = Get_List_MaxRepeat(Get_Next_Index(index_list[1], result_num_02))
    result_index_03 = Get_List_MaxRepeat(Get_Next_Index(index_list[2], result_num_03))
    result_index_04 = Get_List_MaxRepeat(Get_Next_Index(index_list[3], result_num_04))
    result_index_05 = Get_List_MaxRepeat(Get_Next_Index(index_list[4], result_num_05))
    result_index_06 = Get_List_MaxRepeat(Get_Next_Index(index_list[5], result_num_06))
    result_index_07 = Get_List_MaxRepeat(Get_Next_Index(index_list[6], result_num_07))

    print(index_list[0],"开奖最多的是:",result_index_01)
    print(index_list[1],"开奖最多的是:",result_index_02)
    print(index_list[2],"开奖最多的是:",result_index_03)
    print(index_list[3],"开奖最多的是:",result_index_04)
    print(index_list[4],"开奖最多的是:",result_index_05)
    print(index_list[5],"开奖最多的是:",result_index_06)
    print(index_list[6], "开奖最多的是:", result_index_07)
    pass
####################################################双色球模块#########################################################

####################################################六合彩模块#########################################################
def Get_Macau_List(args):
    result_list_01 = DoForecast(args.file_path, 0)
    result_list_02 = DoForecast(args.file_path, 1)
    result_list_03 = DoForecast(args.file_path, 2)
    result_list_04 = DoForecast(args.file_path, 3)
    result_list_05 = DoForecast(args.file_path, 4)
    result_list_06 = DoForecast(args.file_path, 5)
    result_list_07 = DoForecast(args.file_path, 6)

    # print(result_list_01+result_list_02+result_list_03+result_list_04+result_list_05+result_list_06)
    result_01=Get_List_MaxRepeat(result_list_01+result_list_02+result_list_03+result_list_04+result_list_05+result_list_06)
    print(result_01)

    # print("号码:"+format(result_01.keys()),"次数:"+format(result_01.values()))
    pass
####################################################六合彩模块#########################################################

####################################################Main方法入口#########################################################
def main(args):
    Get_Double_Num(args)##双色球##
    Get_Highest_probability(args)

    # Get_Macau_List(args)##六合彩##
    pass
####################################################Main方法入口#########################################################

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("--file_path",type=str,default='./data/work_macau_num.csv',help='文件路径')
    parser.add_argument("--double_file_path", type=str, default='./data/double_ball.csv', help='文件路径')
    args=parser.parse_args()
    main(args)