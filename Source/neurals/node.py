# encoding:utf-8
'''
Created on 2014年12月11日

@author: leonardo
'''

def serialize(strlist):
    if strlist and (isinstance(strlist, list) or isinstance(strlist, str)):
        root = Node(pvalue=strlist[0])
        last = root
        for s in strlist[1:]:
            nextn = Node(pvalue=s, prefid_dic={'last':last})
            last.refid_dic['next'] = nextn
            last = nextn
        return root
    else:
        return None

class Node(object):
    new_id = 0
    node_pool = {}
    def __init__(self, pid = None, pvalue = None, prefid_dic= {}):
        
        # ----    id    ----
        if pid:
            self.id = pid
        else:
            self.id = Node.new_id
            Node.new_id += 1
            
        # ----    value    ----
        if pvalue:
            self.value = pvalue
        else:
            self.value = None
            
        # ----    refid_dic    ----
        if prefid_dic:
            self.refid_dic = prefid_dic
        else:
            self.refid_dic = {}
        
        # ----    add to pool    ----
        Node.node_pool[self.id] = self
            
    def __getitem__(self, key):
        return self.refid_dic.get(key)