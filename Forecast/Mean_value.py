# ---************************************************---
# @coding: utf-8
# @Time : 2023/3/27 0027 13:25
# @Author : Matrix
# @File : Mean_value.py
# @Software: PyCharm
# ---************************************************---
import argparse
from collections import Counter


def LoadFile(path):
    """
    #读取文件
    :param path:
    :return:
    """
    mFile=open(path,encoding="utf-8")
    mList=mFile.read().split("\n")
    # print(mList)#['1,0', '2,260', '3,290', '4,435', '5,300', '6,570', '7,355', '8,430',...]
    mList.pop()
    return mList
    pass

def GetDict(mlist):
    """
    #转换List为Dict
    :param mlist:
    :return:
    """
    ls = []
    lt = []
    for i in range(len(mlist)):
        ls.append(int(mlist[i].split(",")[0]))  # 将第一个列表元素转为键
        lt.append(int(mlist[i].split(",")[1]))  # 将第二个列表元素转为值
        pass
    dictResult = dict(zip(ls, lt))
    return dictResult
    pass

def GetGreaterDict(keyCounnt,mDict):
    """
    #获取大于keyCounnt的值
    :param keyCounnt:
    :param mDict:
    :return:
    """
    greaterDict=dict((k,v)for k,v in mDict.items() if v>=keyCounnt)
    print(greaterDict)
    # print(sum(greaterDict.values()))
    return greaterDict
    pass
def GetLessDict(keyCounnt,mDict):
    """
    #获取小于keyCounnt的值
    :param keyCounnt:
    :param mDict:
    :return:
    """
    lessDict=dict((k,v)for k,v in mDict.items() if v <= keyCounnt)
    print(lessDict)
    print(sum(lessDict.values()))
    pass

def GetThrowResult(keyCounnt,mDict):
    """
    #抛出的号与金额
    :param keyCounnt:
    :param mDict:
    :return:
    """
    listDict=[]
    # mDict = dict((k, v) for k, v in mDict.items())
    for k, v in mDict.items():
        # print(k,v-int(keyCounnt))#4 53\n6 188\n...
        listDict.append(str(k)+","+str(v-int(keyCounnt)))
        pass
    # print(dict())
    return listDict
    pass

def GetThrowResultDict(mdict_1,mdict_2):
    return dict(Counter(mdict_1)-Counter(mdict_2))
    pass

def main(args):
    file_list=LoadFile(args.file_path)
    mDict=GetDict(file_list)
    mSum_01=(sum(mDict.values())-sum(mDict.values())*0.04) / 47#(计算和均值：总金额-总金额*0.04)/47
    print("第一次和均值:",mSum_01,"\n大于第一次和均值:")
    greaterDict = GetGreaterDict(mSum_01, mDict)
    throwResult_01=GetThrowResult(mSum_01,greaterDict)
    resulrDict_01=GetDict(throwResult_01)
    print("第一次抛出结果{号码:金额}:", resulrDict_01)
    print("第一次抛出金额:",sum(GetDict(throwResult_01).values()))
    print("抛出后的剩余:", GetThrowResultDict(mDict, resulrDict_01))
    # mSum_02=(sum(mDict.values())-sum(GetDict(throwResult_01).values()))
    # mSum_02_result=(mSum_02-mSum_02*0.04)/47
    # print("第二次和均值:", mSum_02_result, "\n大于第二次和均值:")
    # greaterDict_02 = GetGreaterDict(mSum_02_result, GetThrowResultDict(mDict, resulrDict_01))
    # throwResult_02 = GetThrowResult(mSum_02_result, greaterDict_02)
    # resulrDict_02 = GetDict(throwResult_02)
    # print("第二次抛出结果{号码:金额}:", resulrDict_02)
    # print("第二次抛出金额:", sum(GetDict(resulrDict_02).values()))
    pass


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file_path', type=str,default='./data/222.txt',help='文件地址')
    args = parser.parse_args()
    main(args)