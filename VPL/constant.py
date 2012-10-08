class Constant():
  def __init__(self, val):
    self.val = val

    # Remove characters for the label
    self.label = str(val).replace('+', '').replace('-', '_')

    self.postamble = """
    .data
    .align 16
    .const%(label)s:
        .float %(val)s
        .float %(val)s
        .float %(val)s
        .float %(val)s
    """ % {'label': self.label, 'val': self.val}

  def load(self, destreg):
    s = 'movq $.const%s, %s' % (self.label, destreg)
    return s

  def __str__(self):
    return self.postamble
