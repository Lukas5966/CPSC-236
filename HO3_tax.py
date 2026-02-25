tRate = 0.06

def sTax(t):
    return round(float(t*tRate),2)

def afterTax(t):
    num = t + sTax(t)
    return num