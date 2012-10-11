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
    self.asm += OPERATION_ASM.format(
      load_left = left.load("%rax"), load_right = right.load("%r10"),
      load_var = val.load("%r11"),
      operation = op_asm, loop = self.func.prog.next_loop,
      inc_left = INC_LEFT_ASM if left.__class__.__name__ is not "Constant" else "",
      inc_right = INC_RIGHT_ASM if right.__class__.__name__ is not "Constant" else "",
    )
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
    # load left operand
    {load_left}
    # load right operand
    {load_right}
    # load result variable
    {load_var}

    movq %rdi, %rbx                    # load vector length into counter %rbx
    shrq $2, %rbx                      # divide counter reg by 4
                                       # (per loop iteration 4 floats)
    jz .loop_end{loop:<22} # check whether number is equal to zero

    .loop_begin{loop}:
        movaps (%rax), %xmm0           # load first operand into %xmm0
        movaps (%r10), %xmm1           # load second operand into %xmm1

        {operation} %xmm1, %xmm0             # perform operation
        movaps %xmm0, (%r11)           # store result

        {inc_left:<30} # increment first operand pointer
        {inc_right:<30} # increment second operand pointer
        addq $16, %r11                 # increment result counter

        decq %rbx                      # decrement loop counter
        jnz .loop_begin{loop:<15} # jump to loop header if counter is not zero
    .loop_end{loop}:
"""

INC_LEFT_ASM = "addq $16, %rax"

INC_RIGHT_ASM = "addq $16, %r10"
