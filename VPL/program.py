from constant import Constant
from function import Function

class Program():
  def __init__(self):
    self.consts = {}
    self.funcs = {}
    self.next_loop = 0

  def addConst(self, val):
    if val not in self.consts:
      self.consts[val] = Constant(val)
    return self.consts[val]

  def addFunc(self, name, params, vars):
    if name in self.funcs:
      raise Exception('Function %s is already defined' % name)
    else:
      self.funcs[name] = Function(name, params, vars)
    return self.funcs[name]

  def __str__(self):
    string = '\n'.join(map(str, self.funcs.values()))
    string += '\n'.join(map(str, self.consts.values()))
    return string

