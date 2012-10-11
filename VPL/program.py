from constant import Constant
from function import Function

class Program():
  def __init__(self, ast_node):
    self.consts = {}
    self.funcs = {}
    self.next_loop = 0

    for child in ast_node.children:
      self.addFunc(child)

  def addConst(self, val):
    if val not in self.consts:
      self.consts[val] = Constant(val)
    return self.consts[val]

  def addFunc(self, ast_node):
    func = Function(ast_node, self)
    if func.name in self.funcs:
      raise Exception('Function %s is already defined' % name)
    else:
      self.funcs[func.name] = func
    return func

  def __str__(self):
    string = '\n'.join(map(str, self.funcs.values()))
    string += '\n'.join(map(str, self.consts.values()))
    return string

