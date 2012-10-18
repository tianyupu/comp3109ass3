from base import Base
from expression import Expression

class Condition(Base):
  def __init__(self, ast_node, stmt):
    self.ast_node = ast_node
    expr, num = ast_node.children

    expr = Expression(expr, stmt.func)
    factor = expr.evaluate() # returns a variable with the calculated value
    num = stmt.func.getVar(num.children[0].text) # returns Constant with the given value from the condition

    self.asm = COND_ASM.format(
      src = factor.load('%rax'), loop = stmt.func.prog.next_loop,
      inc_src = INC_SRC_ASM if factor.__class__.__name__ is not "Constant" else "",
      true = stmt.true,
      false = stmt.false,
      num = num.val
    )
    stmt.func.prog.next_loop += 1

  def __str__(self):
    return self.asm

COND_ASM = """
    # load src address into %rax
    {src}

    xorps %xmm1, %xmm1
    movq %rdi, %rbx
    shrq $2, %rbx

    jz .loop_end{loop}

    .loop_begin{loop}:
        addps (%rax), %xmm1
        
        {inc_src}
        decq %rbx
        jnz .loop_begin{loop}
    .loop_end{loop}:
        xorps %xmm0, %xmm0
        addss %xmm1, %xmm0
        shufps $147, %xmm1, %xmm1
        addss %xmm1, %xmm0
        shufps $147, %xmm1, %xmm1
        addss %xmm1, %xmm0
        shufps $147, %xmm1, %xmm1
        addss %xmm1, %xmm0

        ucomiss .L{num}, %xmm0
        
        ja {true}
        jmp {false}

        .align 4

    .L{num}:
        .float {num}
"""

INC_SRC_ASM = "addq $16, %rax"
