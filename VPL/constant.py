class Constant():
  def __init__(self, val):
    self.val = val
    self.label = repr(val)

    self.asm = CONST_ASM % {'label': self.label, 'val': self.val}

  def load(self, destreg):
    s = LOAD_ASM % (self.label, destreg)
    return s

  def __str__(self):
    return self.asm

CONST_ASM = """
.data
.align 16
.const%(label)s:
    .float %(val)r
    .float %(val)r
    .float %(val)r
    .float %(val)r
"""

LOAD_ASM = "movq $.const%s, %s"
