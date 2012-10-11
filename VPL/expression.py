class Expression():
  def __init__(self, ast_node, func):
    self.func = func
    self.ast_node = ast_node
    self.token = ast_node.token.text
    self.asm = ""

  def evaluate(self):
    # Base case, a number or identity
    if self.token == "FACTOR":
      # Return the variable/constant object
      var = self.ast_node.children[0].text
      factor = self.func.getVar(var)
      return factor

    # Recursively evaluate expression
    if self.token == "EXPR" or self.token == "MIN":
      # Unary operation
      if len(self.ast_node.children) == 1:
        # Recurse AST
        expr = self.ast_node.children[0]
        expr = Expression(expr, self.func)

        # Concatenate assembly operations
        self.asm = expr.asm

        return expr.evaluate()

      # Binary operation
      else:
        if self.token == "MIN":
          expr0, expr1 = self.ast_node.children
        elif self.token == "EXPR":
          expr0, op, expr1 = self.ast_node.children

        # Recurse AST
        expr0 = Expression(expr0, self.func)
        expr1 = Expression(expr1, self.func)
        # And recursively evaluate expressions
        var0 = expr0.evaluate()
        var1 = expr1.evaluate()

        # Concatenate assembly operations
        self.asm = expr0.asm + expr1.asm

        # Perform operation between expression
        if self.token == "MIN":
          val = self.min(var0, var1)
        elif self.token == "EXPR":
          val = self.op(op.text, var0, var1)

        return val

  def op(self, op, left, right):
    # Temporary variable
    val = self.func.tempVar()

    self.asm += "# Perform operation"

    return val

  def min(self, var0, var1):
    # Temporary variable
    val = self.func.tempVar()

    self.asm += "# Perform minimum"

    return val

  def __str__(self):
    return self.asm
