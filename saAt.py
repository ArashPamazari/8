# saAt
def sum(x,y): #jam
    result = {}
    result["s"] = x['s']+y['s']
    result["m"] = x['m']+y['m']
    result["h"] = x['h']+y['h']

    if result['s'] >= 60:
        result['s'] -= 60
        result["m"] += 1  

    if result['m'] >= 60:
        result['m'] -= 60
        result["h"] += 1      

    return result
#------------------------------------------#
def sub(x,y): # tafrigh
    result = {}
    result["s"] = x['s'] - y['s']
    result["m"] = x['m'] - y['m']
    result["h"] = x['h'] - y['h']

    if result['s'] <= 60:
        result['s'] += 60
        result["m"] -= 1  

    if result['m'] <= 60:
        result['m'] += 60
        result["h"] -= 1      

    return result
#------------------------------------------#
def seconds(): #sanie be zaman        # 1 MIN = 60 SEC ---- # 1 HOUR = 60 MIN 
    sec = int(input())

    hour = sec // 3600
    sec %= 3600
    minutes = sec // 60
    sec %= 60
    

    print( hour ,':' ,minutes ,':', sec)

#------------------------------------------#
def Time(): # zaman be sanie
    hour = int(input('saAt ra vared konid: '))
    min = int(input('Daqiqe ra vared konid: '))
    sec = int(input('sanie ra vared konid: '))

    sanie = hour * 60 + min * 60 + sec * 60

    print(sanie)

#------------------------------------------#
def show(x) : 
    print(x['h'],":",x["m"],":",x['s'])
#------------------------------------------#
t1 = {'h':2 , 'm': 30 , "s":45}
t2 = {'h':3 , 'm': 17 , "s":40}
sec = 3600 
#------------------------------------------#
t3 = sum(t1 , t2)   #agar baAd az return def ro toie variable narizi az bein mire
show(t3)

t4 = sub(t2 , t1)
show(t4)