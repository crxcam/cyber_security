
# item represente la fucntion decoré
def premier_decorateur(item:callable):
    print('premiere decorator: ',item)
    def my_function():
        print ('avant  execution de la function decoré ')
        item()
        print ('apres execution de la function decoré ')
    return item

def second_decorateur(fn:callable):
    print('second_decorateur: ',fn())
    return fn()



@premier_decorateur
def dire_bonjour():#
    print('bonjour')



#dire_bonjour()

@second_decorateur
def somme(a,b):
    return a+b

somme(4,5)