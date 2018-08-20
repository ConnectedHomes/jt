import re
from asciitree import LeftAligned
from crayons import *
from collections import OrderedDict as OD


class JSONTree(object):

  def __init__(self):
    self.tr = LeftAligned()

  def __convert__(self, d):
    if type(d) == str:
      pass

    else:
      for k in d.keys(): 
        r = []

        if type(d[k]) == dict:
          try:
            r.append(('{{{}}}'.format(k), self.__convert__(d[k])))

          except:
            pass

        elif type(d[k]) == list and len(d[k]):
          try:
            r.append(('[{}]'.format(k), self.__convert__(d[k][0])))

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

  def __unpack__(self, g):
    r = []

    for i in g:
      if i[1] != {}:
        r.append((i[0], OD(self.__unpack__(i[1]))))

      else:
        r.append(i)

    return r

  def __generate__(self, data):
    tree_data = {'.': OD(self.__unpack__(self.__convert__(data)))}
    return self.tr(tree_data)

            
  def tree(self, data):
    t = self.__generate__(OD(data[0]))\
            .replace('[', str(cyan('[')))\
            .replace(']', str(cyan(']')))\
            .replace('\'', str(green('\'')))\
            .replace('{', str(magenta('{')))\
            .replace('}', str(magenta('}')))\
            .replace('.', str(blue('.')))\
            .replace('+', str(blue('+')))\
            .replace('-', str(blue('-')))\
            .replace('|', str(blue('|')))

    print(t)
