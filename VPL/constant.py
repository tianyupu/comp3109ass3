class Constant():
  def __init__(self, val):
    self.val = val
    self.label = repr(val)

    self.postamble = """
    .data
    .align 16
    .const%(label)s:
        .float %(val)r
        .float %(val)r
        .float %(val)r
        .float %(val)r
    """ % {'label': self.label, 'val': self.val}

  def load(self, destreg):
    s = '\nmovq $.const%s, %s\n' % (self.label, destreg)
    return s

  def __str__(self):
    return self.postamble
