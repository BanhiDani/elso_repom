
hossz = 30
def diszsor(kar:str='*'):
    print(kar*hossz)

def szoveg(felirat:str):
    print(f"*{felirat:^{hossz-2}}*")

def nyugta():
    diszsor()
    szoveg('NYUGTA')
    diszsor()
    er = osszeg(1234,234,234.2)    
    oldalt('alma', 1234,)
    oldalt('körte', 234)
    oldalt('banán', 234.2)
    diszsor("=")
    oldalt('Összesen:', er)
    oldalt('Szervízdíj:',151.17)
    diszsor('=')
    oldalt('Fizetendő:',1853.37)
    diszsor()
    szoveg('CÉG')
    diszsor()

def oldalt(tetel,ar:str,penznem:str='Ft'):
    hossz2 = hossz-len(tetel)-1-len(penznem)
    print(f"{tetel}{ar:>{hossz2}.2f}{penznem}")

def osszeg(ar1:float,ar2:float,ar3:float,):
    eredmeny = ar1+ar2+ar3
    return eredmeny
