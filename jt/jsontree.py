from asciitree import LeftAligned
from asciitree.drawing import BoxStyle, BOX_LIGHT, BOX_BLANK
from crayons import *
from collections import OrderedDict as OD


class JSONTree(object):
    ''' Implements methods for representing JSON schema as text tree. '''
  
    def __init__(self):
          self.tr = LeftAligned(draw=BoxStyle(gfx=BOX_LIGHT, horiz_len=1))
  
    def __schema__(self, d):
        ''' Generates schema for tree using a recursive algorithm. 
    
            :param list d: List containing dict to schema.
        '''
    
        if type(d) == str:
             pass
    
        else:
            for k in d.keys(): 
                r = []
        
                if type(d[k]) == dict:
                    try:
                        r.append(('{{{}}}'.format(k), self.__schema__(d[k])))
        
                    except:
                        pass
        
                elif type(d[k]) == list and len(d[k]):
                    try:
                        r.append(('[{}]'.format(k), self.__schema__(d[k][0])))
          
                    except:
                        pass
        
                else:
                    try:
                        r.append(('\'{}\''.format(k), {}))
        
                    except:
                        pass 
        
                try:
                    yield tuple(r[0])
        
                except:
                    return r
  
    def __convert__(self, g):
        ''' Convert dicts to OrderedDict recursively using a recursive algorithm.
    
            :param list g:
        '''
        r = []
    
        for i in g:
            if i[1] != {}:
                r.append((i[0], OD(self.__convert__(i[1]))))
      
            else:
                r.append(i)
      
        return r
  
    def __generate__(self, data):
        ''' Generate ASCII tree. 
    
            :param list data: data to generate.
        '''
        tree_data = {'.': OD(self.__convert__(self.__schema__(data)))}
        return self.tr(tree_data)
  
              
    def tree(self, data):
        ''' View ASCII tree. 
    
            :param list data: data to generate.
        '''
        t = self.__generate__(OD(data[0]))\
                .replace('[', str(cyan('[')))\
                .replace(']', str(cyan(']')))\
                .replace('\'', str(white('\'')))\
                .replace('{', str(yellow('{')))\
                .replace('}', str(yellow('}')))\
                .replace('.', str(yellow('.')))\
                .replace('+', str(blue('+')))\
                .replace('-', str(blue('-')))\
                .replace('|', str(blue('|')))
    
        return t
    
