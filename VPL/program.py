from constant import Constant
from function import Function

def counter():
  i = 0
  while 1:
    yield i
    i += 1

class Program():
  def __init__(self, ast_node):
    self.consts = {}
    self.funcs = {}
    self.next_loop = counter()
    self.condnums = []

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
    string = ''.join(map(str, self.funcs.values()))
    string += ''.join(map(str, self.consts.values()))
    return string

