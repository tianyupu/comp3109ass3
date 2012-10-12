class Base():
  def __init__(self, ast_node):
    self.ast_node = ast_node

  def header(self):
    return HEADER_ASM.format(
      name = self.ast_node.text+" : line "+str(self.ast_node.line),
      tree = self.format_tree(self.ast_node.toStringTree()),
    )

  def format_tree(self, tree):
    new_tree = ""
    level = 0
    for c in tree:
      if c == "(":
        level += 1
        new_tree.rstrip()
        new_tree += "\n    #"+"\t"*level

      elif c == ")":
        level -= 1
      
      new_tree += c
    
    return new_tree


HEADER_ASM = """
    ###########################################################################
    #
    #{name:^75}
    #{tree}
    #
    ###########################################################################
"""
