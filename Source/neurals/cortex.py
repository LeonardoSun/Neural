# encoding:utf-8
'''
Created on 2014年12月11日

@author: leonardo
'''

class Cortex(object):
    def __init__(self, shape):
        self.shape = shape
#     
#     @property
#     def shape(self):
#         return self._set.shape
    
    def load(self, indexable):
        if indexable.shape != self.shape:
            raise ValueError("The shape of parameter doesn't match with cortex's.")
        self._set = indexable
    
    def get(self, x_index, y_index = 0):
        return self._set.get(x_index, y_index)
    
class NeuralRelationL(object):
    def __init__(self, cortex, index):
        self._cortex = cortex
        self._index = index
    
    @property
    def value(self):
        self._get_conect_value(self._index)
    
    def _get_conect_value(self, index):
        self._cortex.get(index)
    
    @property
    def left(self):
        x_index = self._index - 1
        return self._get_conect_value(x_index) - self.value
    
    @property
    def right(self):
        x_index = self._index + 1
        return self._get_conect_value(x_index) - self.value
        
class NeuralRelationXY(object):
    def __init__(self, cortex, ix, iy):
        self._cortex = cortex
        self._ix = ix
        self._iy = iy
        
    @property
    def value(self):
        return self._get_conect_value(self._ix, self._iy)
    
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
    