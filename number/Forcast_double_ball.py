# ---************************************************---
# @coding: utf-8
# @Time : 2022/8/2 0002 22:56
# @Author : Matrix
# @File : Forcast_double_ball.py
# @Software: PyCharm
# ---************************************************---
import pandas as pd
import argparse
from Result_Arithmetic_Progression import Get_Odd_Even


def DoForecast(file_path,column):
    """获取csv文件内容并返回
    :param file_path: 文件地址,类型为str
    :param column: 要查询的列数,类型为int
    :return: 返回的list值,result为返回结果list
    """
    file = pd.read_csv(file_path, header=None, encoding='utf-8')
    index_len = len(file)
    num=file.iloc[:,column]
    result=[]
    for i in range(index_len):
        result.append(num[i])
        if i == index_len - 1:  #检测是否最后一个，是则跳过。
            break
            pass
        pass
    return result
    pass

def Get_Next_Index(mIndex,mListIndex):
    """预测下一次的值
    :param mIndex:数字下标
    :param mListIndex:数字列表
    :return:返回可能出现的list值
    """
    result=[]
    for i in range(len(mListIndex)):
        if i == len(mListIndex) - 1:  #检测是否最后一个，是则跳过。
            break
            pass

        if mListIndex[i]==mIndex:
            #print("下一次可能出现的值:"+str(mListIndex[i+1]))
            result.append(mListIndex[i+1])
            pass
        pass

    return result
    pass

def GetMin(num_01,num_02,num_03,num_04,num_05,num_06,num_07):
    """三元运算获得最小数
    :param num_01:
    :param num_02:
    :param num_03:
    :return:
    """
    return num_01 if num_01 < num_02 and num_01 < num_03 and num_01 < num_04 and num_01 < num_05 and num_01 < num_06 and num_01 < num_07\
        else num_02 if num_02 < num_03 and num_02 < num_04 and num_02 < num_05 and num_02 < num_06 and num_02 < num_07\
        else num_03 if num_03<num_04 and num_03<num_05 and num_03<num_06 and num_03<num_07 \
        else num_04 if num_04<num_05 and num_04<num_06 and num_04<num_07 \
        else num_05 if num_05 < num_06 and num_05 < num_07 \
        else num_06 if num_06 < num_07 else num_07
    #return num_01 if num_01 > num_02 and num_01 > num_03 else num_02 if num_02 > num_03 else num_03#最大数
    pass

def Get_ball_Result(list_01,list_02,list_03,list_04,list_05,list_06,list_07):
    """
    #将list_01,list_02,list_03中的单元素组合成一个list元素
    :param list_01:
    :param list_02:
    :param list_03:
    :return: 返回组合完成后且去重的list
    """
    index = GetMin(len(list_01), len(list_02), len(list_03),len(list_04), len(list_05), len(list_06),len(list_07))

    result=[]

    for i in range(index):
        str_temp=str(list_01[i])+","+ str(list_02[i]) +","+ str(list_03[i])+","+str(list_04[i])\
                 +","+str(list_05[i]) +","+str(list_06[i])+","+str(list_07[i])
        result.append("["+str(list_01[i])+","+ str(list_02[i]) +","+ str(list_03[i])+","+str(list_04[i])+","+ str(list_05[i]) +
                      ","+str(list_06[i])+","+str(list_07[i])+"]")
        pass

    result_Remove_duplicate=Get_Remove_duplicate(result)#去重方法函数

    return result_Remove_duplicate
    pass

def Get_Remove_duplicate(list):
    """
    #去重list中重复项
    :param list:
    :return:
    """
    result_Remove_duplicate=[]
    for x in list:
        if x not in result_Remove_duplicate:
            result_Remove_duplicate.append(x)
        pass

    return result_Remove_duplicate
    pass

def Show_Result(indexList,result_list):
    """
    #集成显示方法
    :param indexList:
    :param result_list:
    :return:
    """
    str_show = ''
    for i in range(len(result_list)):
        str_show += str(result_list[i]) + " "
        pass
    print(str_show)
    print("数量:", len(result_list))
    print("上一期:" + str(indexList))
    pass

def Get_Double_Ball(args,index_list):
    ############################################双色球模块################################################
    # index_list = [6,11,13,16,19,31,2]  # 上一期(双色球)
    """定义储存csv获取到三列数的数组"""
    result_num_01 = DoForecast(args.double_file_path, 0)
    result_num_02 = DoForecast(args.double_file_path, 1)
    result_num_03 = DoForecast(args.double_file_path, 2)
    result_num_04 = DoForecast(args.double_file_path, 3)
    result_num_05 = DoForecast(args.double_file_path, 4)
    result_num_06 = DoForecast(args.double_file_path, 5)
    result_num_07 = DoForecast(args.double_file_path, 6)
    #
    ###此处为方法一使用数据###
    result_index_01 = Get_Next_Index(index_list[0], result_num_01)#不去重
    result_index_02 = Get_Next_Index(index_list[1], result_num_02)
    result_index_03 = Get_Next_Index(index_list[2], result_num_03)
    result_index_04 = Get_Next_Index(index_list[3], result_num_04)
    result_index_05 = Get_Next_Index(index_list[4], result_num_05)
    result_index_06 = Get_Next_Index(index_list[5], result_num_06)
    result_index_07 = Get_Next_Index(index_list[6], result_num_07)
    # #
    # result_index_01 = Get_Remove_duplicate(Get_Next_Index(index_list[0], result_num_01))#先去重
    # result_index_02 = Get_Remove_duplicate(Get_Next_Index(index_list[1], result_num_02))
    # result_index_03 = Get_Remove_duplicate(Get_Next_Index(index_list[2], result_num_03))
    # result_index_04 = Get_Remove_duplicate(Get_Next_Index(index_list[3], result_num_04))
    # result_index_05 = Get_Remove_duplicate(Get_Next_Index(index_list[4], result_num_05))
    # result_index_06 = Get_Remove_duplicate(Get_Next_Index(index_list[5], result_num_06))
    # result_index_07 = Get_Remove_duplicate(Get_Next_Index(index_list[6], result_num_07))
    result_index_07=Get_Remove_duplicate(result_index_07)
    result_index_07.sort()
    Show_Result(index_list,result_index_07)

    # result_01 = Get_ball_Result(result_index_01, result_index_02, result_index_03,
    #                             result_index_04,result_index_05, result_index_06, result_index_07)
    # Show_Result(index_list, result_01)
    ###################################################################################################
    pass

def main(args):
    ############################################双色球模块################################################
    double_ball_index_list=[3,16,17,19,25,33,7]
    # Get_Double_Ball(args,double_ball_index_list)
    ############################################双色球模块################################################
    pass


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--double_ball_path', type=str,default='./data/double_ball.csv',help='双色球csv文件地址')
    args = parser.parse_args()
    main(args)