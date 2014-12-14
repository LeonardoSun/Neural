# encoding:utf-8
'''
Created on 2014年12月14日

@author: leonardo
'''

class Indexable(object):
    def __init__(self):
        self.shape = (0, 0)
        
    def get(self, x_index, y_index):
        return None
    
class NestingArrayIndexable(Indexable):
    def __init__(self, array, shape):
        self._array = array
        self.shape = shape
        
    def get(self, x_index, y_index):
        if 0 <= x_index < self.shape[0] and 0 <= y_index < self.shape[1]:
            return self._array[y_index][x_index]
        else:
            return None