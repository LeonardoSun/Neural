# encoding:utf-8
'''
Created on 2014年12月11日

@author: leonardo
'''
from Source.neurals.node import serialize
from Source.neurals.node import Node
from Source.neurals.cortex import Cortex, NeuralRelationL
from Source.neurals import indexable

n1 = Node()
print n1.id
n2 = Node()
print n2.id

ln = serialize('aabb')
print ln.id
n = ln['next']
while n:
    print n.id, n.value
    n = n['next']
    
def and_opr():
    input_r = [{0:0, 1:0, 'r':0}, {0:0, 1:1, 'r':0}, {0:1, 1:0, 'r':0}, {0:1, 1:1, 'r':1}]
    level_1 = Cortex(2,)
    level_1.load(indexable.ListIndexable([0,0]))
    outer_signal = 0
    row = []
    for x in range(level_1.shape):
        row.append(NeuralRelationL(level_1, x))
    level_2 = Cortex(2,)
    level_2.load(indexable.ListIndexable(row))
    
    
