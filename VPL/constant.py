class Constant():
  def __init__(self, val):
    self.val = val
    self.label = repr(val)

    self.asm = CONST_ASM.format(label=self.label, val=self.val)

  def load(self, destreg): 
    # returns the string for the instruction to load the constant
    s = LOAD_ASM.format(label=self.label, destreg=destreg)
    return s

  def __str__(self):
    return self.asm

CONST_ASM = """
.data
.align 16
.const{label}:
    .float {val}
    .float {val}
    .float {val}
    .float {val}
"""

LOAD_ASM = "movq $.const{label:<10}, {destreg:<10} # load constant into {destreg}"
