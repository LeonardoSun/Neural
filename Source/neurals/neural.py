# encoding:utf-8
'''
Created on 2014年12月8日

@author: sunqinghao
'''
'''
# 第一层（第一列）为原始数据
# 从第二层开始为隐含层
# 每层隐含层都有与上一层所有数据相连的节点，这些链接由权值控制
# 隐含层即为归纳出来的特征，最后通常经过若干隐含层之后得出只有一个节点的最终结果层
# 即为形成了恒定表征
'''

'''
联想存在于每一个节点之中
确切的说，是每个节点都可以动态连接新的节点，以进行联想等操作
联想是将某个模式于某个模式相关联，而不是直接将数据进行关联
而模式可以是恒定表征，也可以是中间隐藏层得出的初步结论
'''