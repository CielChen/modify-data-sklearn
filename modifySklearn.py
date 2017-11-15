'''
Function：将原始训练集改为sklearn所需的训练集格式，最终为.csv文件
Date: 08/10/2017
Author: Ciel
'''

import csv

##############################新建格式满足libsvm的训练集,写表头##############################
#step1. 写表头：ID（训练样本编号），Type（是不是光源）,feature1，feature2 ··· feature342，
headTitle=['ID','Type']
for i in range(2,344):
    headTitle.append('feature'+str(i-1))
#step2. 写入csv文件
newtrainFile=open("C:\CIEL\code\modify-data-sklearn\data\\20171114-rawtrain.csv","w", newline='')
#newtrainFile=open("F:\Code\modify-data-sklearn\\modify.csv", "w", newline='')  #测试文件
csv_writer=csv.writer(newtrainFile, dialect='excel')
csv_writer.writerow(headTitle)

#打开原始训练集rawtrain.txt
rawtrainFile=open("C:\CIEL\code\modify-data-sklearn\data\\20171114-rawtrain.txt","r")
#rawtrainFile=open("F:\Code\modify-data-sklearn\\test.txt","r")  #测试文件

#逐行读取
fileEnd=0  #fileEnd：读到txt文件结尾的标志。0表示没有到结尾，1到了结尾
rowNum=0  #rowNum：txt的行数
while not fileEnd:
    lineContent=rawtrainFile.readline()  #lineContent：每行内容

    if(lineContent != ''):
        rowNum=rowNum+1

        #默认分隔符为空格（不管有几个空格），进行分割字符串lineContent，存入splitLine中
        splitLine=lineContent.split()
        colNum=len(splitLine)  #colNum=列数，下标0~n-1
        #print(colNum)
        '''
        修改格式为sklearn的训练集，即
        第2行（具体的值）：ID（=1） type，feature1 feature2···feature342，
        第3行：ID（=2） ，type feature1 feature2···feature342，
        ...
        第rowNum+1行：ID（=rowNum） type，feature1 feature2···feature342，
        rawtrain.txt中，每行有344列
        第2列为type，第3-344列为342个特征的value
        '''
        trainSample=[str(rowNum)]
        for i in range(1, colNum):
            if(i==1): #type
                trainSample.append(splitLine[i])
            else:  #feature(i)
                trainSample.append(splitLine[i])
        # print(trainSample)
        csv_writer=csv.writer(newtrainFile, dialect='excel')
        csv_writer.writerow(trainSample)
            
    else:
        fileEnd=1

print(rowNum)

rawtrainFile.close()
newtrainFile.close()


