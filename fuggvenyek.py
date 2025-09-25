


def relacio(a:int,b:int):
    if a > b:
        return(">")
    elif a < b:
        return("<")
    else:
        return("=")



def eredmeny():

    a = int(input("Adj meg egy számot"))
    b = int(input("Adj meg egy számot"))
    er = relacio(a,b)
    print(f'{a}      {er}      {b}' )

eredmeny()
