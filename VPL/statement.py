from base import Base
from expression import Expression
from condition import Condition

class Statement(Base):
  def __init__(self, ast_node, func):
    self.func = func
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

    if ast_node.token.text == "IF":
      cond, true_body, false_body = ast_node.children
      idnum = self.func.prog.next_loop
      self.true = ".truebranch%s" % idnum
      self.false = ".falsebranch%s" % idnum
      self.func.prog.next_loop += 1
      self.asm += IF_ASM.format(
        cond = Condition(cond, self),
        id = idnum,
        true_body = ''.join(map(str, [Statement(s, self.func) for s in true_body.children])),
        false_body = ''.join(map(str, [Statement(s, self.func) for s in false_body.children]))
      )

    if ast_node.token.text == "WHILE":
      cond, body = ast_node.children
      idnum = self.func.prog.next_loop
      self.true = ".loopbegin%s" % idnum
      self.false = ".loopexit%s" % idnum
      self.func.prog.next_loop += 1
      self.asm += WHILE_ASM.format(
        id = idnum,
        cond = Condition(cond, self),
        body = ''.join(map(str, [Statement(s, self.func) for s in body.children]))
      )

  def __str__(self):
    if not self.asm:
      return self.header()

    return self.asm

IF_ASM = """
    {cond}

    .truebranch{id}:
        {true_body}

        jmp .endif{id}
    
    .falsebranch{id}:
        {false_body}
    
    .endif{id}:
"""

WHILE_ASM = """
    jmp .loopcond{id}

    .loopbegin{id}:
        {body}

    .loopcond{id}:
        {cond}

    .loopexit{id}:
"""
