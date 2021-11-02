def is_primo(ent:int)-> str:
    re:str
    if ent==2:
        return "Es primo"
    elif ent>2:
        if ent%2!=0 and ent/ent==1:
            re="si es primo"
        else:
            re="no es primo"
        return re
    else:
        return "ingrese num mayor a 2" #""" ::-1 nos permite dar la vuelta al string """

def run():
    print(is_primo(13))


#Entry point
if __name__=='__main__':
    run()
