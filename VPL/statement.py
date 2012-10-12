from base import Base
from expression import Expression

class Statement(Base):
  def __init__(self, ast_node, func):
    self.ast_node = ast_node
    self.asm = ""

    # Assignment
    if ast_node.token.text == "ASSIGN":
      # Get the variable and expression
      var, expr = ast_node.children
      var = func.getVar(var.text)

      # Calculate the answer
      expr = Expression(expr, func)
      factor = expr.evaluate()
      
      # Add the calculations to the function body
      self.asm += str(expr)
      self.asm += self.header()
      self.asm += var.assign(factor, func.prog.next_loop)
      func.prog.next_loop += 1

  def __str__(self):
    if not self.asm:
      return self.header()

    return self.asm
