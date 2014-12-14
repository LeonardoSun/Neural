# encoding:utf-8
'''
Created on 2014年12月11日

@author: leonardo
'''

class Cortex(object):
    def __init__(self, indexable):
        self._set = indexable
    
    @property
    def shape(self):
        return self._set.shape
    
    def get(self, x_index, y_index):
        return self._set.get(x_index, y_index)
        
class NeuralRelation(object):
    def __init__(self, cortex, ix, iy):
        self._cortex = cortex
        self._ix = ix
        self._iy = iy
        
    @property
    def value(self):
        return self._get_conect_value(self.ix, self.iy)
    
    def _get_conect_value(self, x_index, y_index):
        self._cortex.get(x_index, y_index)
    
    @property
    def up(self):
        x_index = self._ix
        y_index = self._iy - 1
        return self._get_conect_value(x_index, y_index) - self.value
    
    @property
    def down(self):
        x_index = self._ix
        y_index = self._iy + 1
        return self._get_conect_value(x_index, y_index) - self.value
    
    @property
    def left(self):
        x_index = self._ix - 1
        y_index = self._iy
        return self._get_conect_value(x_index, y_index) - self.value
    
    @property
    def right(self):
        x_index = self._ix + 1
        y_index = self._iy
        return self._get_conect_value(x_index, y_index) - self.value
    
    @property
    def up_left(self):
        x_index = self._ix - 1
        y_index = self._iy - 1
        return self._get_conect_value(x_index, y_index) - self.value
    
    @property
    def up_right(self):
        x_index = self._ix + 1
        y_index = self._iy - 1
        return self._get_conect_value(x_index, y_index) - self.value
    
    @property
    def down_left(self):
        x_index = self._ix - 1
        y_index = self._iy + 1
        return self._get_conect_value(x_index, y_index) - self.value
    
    @property
    def down_right(self):
        x_index = self._ix + 1
        y_index = self._iy + 1
        return self._get_conect_value(x_index, y_index) - self.value
    