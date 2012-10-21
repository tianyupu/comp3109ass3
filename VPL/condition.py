from base import Base
from expression import Expression

class Condition(Base):
  def __init__(self, ast_node, stmt):
    self.ast_node = ast_node
    expr, num = ast_node.children

    factor = stmt.func.getVar(expr.children[0].text)
    num = float(num.children[0].text)

    self.asm = COND_ASM.format(
      src = factor.load('%rax'), loop = stmt.func.prog.next_loop.next(),
      inc_src = INC_SRC_ASM if factor.__class__.__name__ is not "Constant" else "",
      true = stmt.true,
      false = stmt.false,
      num = num,
      numlabel = "" if num in stmt.func.prog.condnums else INC_NUM_ASM.format(number=num)
    )
    stmt.func.prog.condnums.append(num)

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
        
        jb {true}
        jmp {false}

    {numlabel}
"""

INC_SRC_ASM = "addq $16, %rax"

INC_NUM_ASM = """
        .align 4
    .L{number}:
        .float {number}
"""
