--------------------Function--------------------
将训练集改为Sklearn所需的训练格式

Example:
将test.txt改为modify.csv(modify.csv满足modifySklearn的训练格式)


-------------------操作说明-----------------------------
step1. 合并所有训练样本的txt到一个txt中
操作如下：
（1）	将所有训练样本的txt文件存放到
F:\Code\libsvm\Data\【CLMake3DFeature的输出-txt】outputTXTonly
（PS：win7如何选中文件夹中的所有txt文件？
参考https://zhidao.baidu.com/question/263763323.html ）
（2）	合并所有txt文件到F:\Code\libsvm\Data\trainData\rawtrain.txt
（参考：http://jingyan.baidu.com/article/d3b74d64a7cf671f77e609b5.html ）

step2. 运行 modifySklearn.py


--------------------OS--------------------
win7 64bit， Python3.4.3
win10 64bit， Python3.5