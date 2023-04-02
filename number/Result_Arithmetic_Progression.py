# ---************************************************---
# @coding: utf-8
# @Time : 2022/9/8 0008 16:10
# @Author : Matrix
# @File : Result_Arithmetic_Progression.py
# @Software: PyCharm
# ---************************************************---
import random
from collections import Counter


def Arithmetic_Progression(index_list):
    """
    #等差数列方法:
    #规则:a[n]-a[n-1]
    :param index_list:
    :return:
    """
    index_list.pop()  # 去除最后一个元素
    result=[]
    index_list.sort()#升序；降序:index_list.sort(reverse=True)
    while(True):
        if(len(index_list)==0):
            break
            pass
        result+= Do_Subtraction(index_list)
        index_list.remove(min(index_list))  # 去除最小元素
        pass
    # print("排序后:",index_list,"\t长度:",len(index_list))
    # result=Do_Subtraction(index_list)
    # index_list.remove(min(index_list))#去除最小元素
    # print("去除最小后:",index_list,"\t长度:",len(index_list))
    # result += Do_Subtraction(index_list)

    # print("结果:", result, "\t长度:", len(result))
    result.sort()
    # print("所有结果排序后:", result, "\t长度:", len(result))
    return result
    pass

def Do_Subtraction(index_list):
    result_Subtraction=[]
    for i in range(len(index_list)):
        end=i+1
        if(end==len(index_list)):
            break
            pass
        result_Subtraction.append(abs(index_list[end] - index_list[0]))
        pass
    return result_Subtraction
    pass

def Do_Random_List(list):
    """
    #随机生成6个元素列表
    :param list:
    :return:
    """
    result_list = []
    while (True):
        if (len(result_list) == 6):
            break
            pass
        index_key = random.randint(0, len(list) - 1)
        result_list.append(list[index_key])
        list.pop(index_key)
        pass
    result_list.sort()
    return result_list
    pass

def Get_Sum_End(index_num):
    """
    #和值为计算
    :param index_num:
    :return:
    """
    return int(index_num%10)
    pass

def Get_List_Difference_set(index_list,remove_list):
    """
    #获取两个list的差集
    :param index_list:原list
    :param remove_list:被删除list
    :return:
    """
    result = [i for i in index_list if i not in remove_list]
    return result
    pass

def Get_Odd_Even(index_num):
    """
    #判断index_num是否奇偶数并返回:奇-0，偶-1
    :param index_num:
    :return:
    """
    result_key=0
    if index_num%2==0:
        result_key=1
        pass

    return result_key
    pass

#regin ***************************************************篮球模块**************************************************
def Get_Blue_Fun1(index_list,blue_list):
    """
    #17-篮尾
    :param index_list:
    :param blue_list:
    :return:
    """
    result_list=[]
    result_key=17-int(index_list[6])
    for i in range(len(blue_list)):
        if(blue_list[i]==result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list=Get_List_Difference_set(blue_list,result_list)
    # print("去除后:",result_list)
    return result_list
    pass

def Get_Blue_Fun2(index_list,blue_list):
    """
    #红3尾+篮尾
    :param index_list:
    :param blue_list:
    :return:
    """
    result_list = []
    result_key =Get_Sum_End(int(index_list[2])) + Get_Sum_End(int(index_list[6]))
    for i in range(len(blue_list)):
        if (blue_list[i] == result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list = Get_List_Difference_set(blue_list, result_list)
    # print("去除后:", result_list)
    return result_list
    pass

def Get_Blue_Fun3(index_list,blue_list):
    """
    #红5-红2
    :param index_list:
    :param blue_list:
    :return:
    """
    result_list = []
    result_key =int(index_list[4]) - int(index_list[1])
    for i in range(len(blue_list)):
        if (blue_list[i] == result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list = Get_List_Difference_set(blue_list, result_list)
    # print("去除后:", result_list)
    return result_list
    pass
def Get_Blue_Fun4(index_list,blue_list):
    """
    #红4-红1
    :param index_list:
    :param blue_list:
    :return:
    """
    result_list = []
    result_key =int(index_list[3]) - int(index_list[0])
    for i in range(len(blue_list)):
        if (blue_list[i] == result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list = Get_List_Difference_set(blue_list, result_list)
    # print("去除后:", result_list)
    return result_list
    pass
def Get_Blue_Fun5(index_list,blue_list):
    """
    #红6尾+红1尾+5,超过16时，要减16
    :param index_list:
    :param blue_list:
    :return:
    """
    result_list = []
    result_key =Get_Sum_End(index_list[5]) + Get_Sum_End(index_list[0])+5
    if(result_key>16):
        result_key=result_key-16
        pass
    for i in range(len(blue_list)):
        if (blue_list[i] == result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list = Get_List_Difference_set(blue_list, result_list)
    # print("去除后:", result_list)
    return result_list
    pass
def Get_Blue_Fun6(index_list,blue_list):
    """
    #红4尾+1
    :param index_list:
    :param blue_list:
    :return:
    """
    result_list = []
    result_key =Get_Sum_End(index_list[3])+1
    for i in range(len(blue_list)):
        if (blue_list[i] == result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list = Get_List_Difference_set(blue_list, result_list)
    # print("去除后:", result_list)
    return result_list
    pass
def Get_Blue_Fun7(index_list,blue_list):
    """
    #红1+7,超过16时，要减16
    :param index_list:
    :param blue_list:
    :return:
    """
    result_list = []
    result_key =int(index_list[0]) + 7
    if(result_key>16):
        result_key=result_key-16
        pass
    for i in range(len(blue_list)):
        if (blue_list[i] == result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list = Get_List_Difference_set(blue_list, result_list)
    # print("去除后:", result_list)
    return result_list
    pass
def Get_Blue_Fun8(index_list_01,index_list_02,blue_list):
    """
    #上两期篮尾之和
    :param index_list_01:
    :param index_list_02:
    :param blue_list:
    :return:
    """
    result_list = []
    result_key =Get_Sum_End(index_list_01[6])+Get_Sum_End(index_list_02[6])
    for i in range(len(blue_list)):
        if (blue_list[i] == result_key):
            result_list.append(blue_list[i])
            pass
        pass
    result_list = Get_List_Difference_set(blue_list, result_list)
    print("去除后:", result_list)
    return result_list
    pass

#endregin***************************************************篮球模块**************************************************

def Get_List_MaxRepeat(index_list):
    """
    #获取list中各个元素出现的次数并排列
    :param index_list:
    :return:
    """
    # result=[]
    # while(True):
    #     if (len(index_list)==0):
    #         break
    #         pass
    #     result.append(Get_list_Sorting(index_list))
    #     index_list.remove(result[-1])
    #     pass
    # return result
    return Counter(index_list)
    pass

def Get_list_Sorting(index_list):
    return max(set(index_list), key=index_list.count)
    pass