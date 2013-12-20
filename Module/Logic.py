def ANDG(a=False,b=False):
    if a and b:
        return True
    else:
        return False

def ORG(a=False,b=False):
    if a or b:
        return True
    else:
        return False

def XORG(a=False,b=False):
    if a and b:
        return False
    if a or b:
        return True
    else:
        return False

def NOTG(a=False):
    if a:
        return False
    else:
        return True

def NANDG(a=False,b=False):
    return NOTG(ANDG(a,b))

def NORG(a=False,b=False):
    return NOTG(ORG(a,b))

def XNORG(a=False,b=False):
    return NOTG(XORG(a,b))


    
