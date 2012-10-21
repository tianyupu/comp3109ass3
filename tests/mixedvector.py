a = []
b = []
c = []
for i in xrange(0,32):
    a.append(float(i))
    b.append(float(i*i))
    c.append(float(i*2))

def whileIf(a,b):
    while sum(a) < 10:
        print "hi"
        if sum(b) < 5:
            for i in xrange(len(b)):
                b[i] = b[i] * b[i]
        else:
            for i in xrange(len(b)):
                b[i] = b[i] - 1
        for i in xrange(len(a)):
            a[i] = a[i] + 1
        
def ifWhile(a,b):
    if sum(b) < 4:
        while sum(a) < 5:
            for i in xrange(len(a)):
                a[i] = a[i] + 1
                b[i] = b[i]*3
            for i in xrange(len(b)):
                b[i] = min(b[i],20)
        for i in xrange(len(a)):
            a[i] = 2
    else:
        for i in xrange(len(a)):
            a[i] = 0
            b[i] = 0

def nested(a,b,c):
    d = []
    for i in xrange(len(a)):
        d.append(min (min(a[i],b[i]),c[i]) -1)
        b[i] = 5*(1+min(a[i],b[i])/2)+2
        a[i] = d[i] + a[i] - c[i]
        c[i] = 2./4.
        
def stress(a,b):
    x = []
    for i in xrange(len(a)):
        x.append(3*(min(a[i],b[i]) +1))
    if sum(x) < 100:
        for i in xrange(len(a)):
            a[i] = 10
        while sum(a) < 10:
            for i in xrange(len(a)):
                b[i]=b[i]+1
                a[i]=a[i]-1
    else:
        for i in xrange(len(a)):
            a[i]=x[i]
            b[i]=x[i]
    for i in xrange(len(a)):
        a[i] = b[i]*a[i]*b[i]

stress(a,b)
print a
print b
