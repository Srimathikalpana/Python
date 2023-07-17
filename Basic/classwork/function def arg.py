#def name with parameters

def register(name,location,prefix='Mr/Mrs/Mrs'):
    if location == 'salem':
        print(prefix,name," has been approved in ",location)
    elif location =="chennai":
        print(prefix,name," will be shifted soon to ",location)
    else: print('business not approved')

register('srihari','salem')
register('vicky','chennai','Mr.')
register('vijay','cbe')
