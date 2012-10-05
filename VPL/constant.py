class Constant():
  def __init__(self, val):
    self.val = val

    self.postamble = """
    .data
    .align 16
    .const%(val)s:
        .float %(val)s
        .float %(val)s
        .float %(val)s
        .float %(val)s
    """ % {'val': val}

  def load(self, destreg):
    s = 'movq $.cont%s, %s' % (self.val, destreg)
    return s

  def __str__(self):
    return self.postamble
