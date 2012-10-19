def stress(a,b):
  x = 3. * (min(a,b) + 1.)/ 2.;
  if (x*4) < 100:
    a = 10;
    while (a*4) < 10:
      b = b + 1.;
      a = a - 1.;
  else:
    a = x;
    b = x;
  a = b * a * b;
  return (a,b)

def stress2(a,b):
  if a*4 < 10:
    if a*4 < 5:
      while a < 10:
        a = a + 1;
    else:
      a = min (a,b);
      b = 2;
    b = b + 1;
  else:
    b = 100;
    a = -100;
  return (a,b)

def stress3(a,b,c,d,e):
  a = min (b, min(c,min(d, min(e, 5. + 2. * (3. + 1.)))));
  b = 1. / 2.;
  c = a * (2. + c) * d;
  d = d + 5.;
  e = d - 3. * min (2., min (a, 0.));
  return [a,b,c,d,e]
