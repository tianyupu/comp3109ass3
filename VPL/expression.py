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

        # Get operation type 
        if self.token == "MIN":
          op = "min"
        elif self.token == "EXPR":
          op = op.text

        # Perform operation between expressions
        val = self.op(op, var0, var1)

        return val

  def op(self, op, left, right):
    # ASM command for the given Operation
    op_asm = OPS[op]

    # Temporary variable
    val = self.func.tempVar()

    # ASM to perform operation
    self.asm += left.load("%rax")
    self.asm += right.load("%r10")
    self.asm += val.load("%r11")
    self.asm += OPERATION_ASM % {
        'operation': op_asm, 'loop': self.func.prog.next_loop,
        'inc_left': INC_LEFT_ASM if left.__class__ is "Constant" else "",
        'inc_right': INC_RIGHT_ASM if right.__class__ is "Constant" else "",
    }
    self.func.prog.next_loop += 1

    return val

  def __str__(self):
    return self.asm

OPS = {
  "+": "addps",
  "-": "subps",
  "*": "mulps",
  "/": "divps",
  "min": "minps",
}

OPERATION_ASM = """
       movq %%rdi, %%rbx        # load vector length into counter %%rbx
       shrq $2, %%rbx           # divide counter reg by 4
                                # (per loop iteration 4 floats)
       jz .loop_end%(loop)s     # check whether number is equal to zero
   .loop_begin%(loop)s:         # loop header
       movaps (%%rax), %%xmm0   # load first operand into %%xmm0
       movaps (%%r10), %%xmm1   # load second operand into %%xmm1

       # perform operation
       %(operation)s %%xmm1, %%xmm0
       movaps %%xmm0, (%%r11)   # store result

       # increment pointers
       %(inc_left)s
       %(inc_right)s
       addq $16, %%r11
       decq %%rbx               # decrement counter
       jnz .loop_begin%(loop)s  # jump to loop header if counter is not zero
   .loop_end%(loop)s:
"""

INC_LEFT_ASM = """
       # IMPORTANT: remove following line if %rax is pointing to a constant
       addq $16, %rax
"""

INC_RIGHT_ASM = """
       # IMPORTANT: remove following line if %%r10 is pointing to a constant
       addq $16, %r10
"""
