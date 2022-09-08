# ---************************************************---
# @coding: utf-8
# @Time : 2022/9/8 0008 16:10
# @Author : Matrix
# @File : Result_Arithmetic_Progression.py
# @Software: PyCharm
# ---************************************************---
def Arithmetic_Progression(index_list):
    """
    #等差数列方法:
    #规则:a[n]-a[n-1]
    :param index_list:
    :return:
    """
    result=[]
    index_list.sort()#升序；降序:index_list.sort(reverse=True)
    index_list.pop()#去除最后一个元素
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

    print("结果:", result, "\t长度:", len(result))
    pass

def Do_Subtraction(index_list):
    result_Subtraction=[]
    for i in range(len(index_list)):
        end=i+1
        if(end==len(index_list)):
            break
            pass
        result_Subtraction.append(index_list[end] - index_list[0])
        pass
    return result_Subtraction
    pass