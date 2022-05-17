# kasr
def mul(x,y): # zarb do kasr
    result = {}
    result['s'] = x['s'] * y ['s'] 
    result['m']= x['m'] * y ['m']
    return result
#-------------------#
def sum(x , y): # jam do kasr
    result = {}
    result['s'] = x['s'] * y['m'] + x['m'] * y['s']
    result['m']= x['m'] * y['m']    
    return result
#-------------------#
def sub(x , y):
    result = {}
    result['s'] = x['s'] * y['m'] - x['m'] * y['s']
    result['m']= x['m'] * y['m']  
    return result  
#-------------------#
def div(x , y):
    result = {}
    result['s'] = x['s'] / y ['m'] 
    result['m']= x['m'] / y ['s']
    return result
#-------------------#
def show(x):
    print(x['s'],'/',x['m'])
#-------------------#
a= {'s': 2, 'm': 3}
b= {'s':5 , 'm':4}

#------------------------------------------#
c= mul(a,b)
show(c)

d = sum(a , b)
show(d)

e = sub(a,b)
show(e)

f = div(a,b)
show(f)