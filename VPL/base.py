class Base():
  def __init__(self, ast_node):
    self.ast_node = ast_node

  def header(self):
    return HEADER_ASM.format(
      name = self.ast_node.text+" : line "+str(self.ast_node.line),
      tree = self.ast_node.toStringTree(),
    )


HEADER_ASM = """
    ###########################################################################
    #
    #{name:^75}
    #{tree:^75}
    #
    ###########################################################################
"""
