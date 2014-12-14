# encoding:utf-8
'''
Created on 2014年12月11日

@author: leonardo
'''
from Source.neurals.node import serialize
from Source.neurals.node import Node

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