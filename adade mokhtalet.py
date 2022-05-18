# adad mokhtalet
# 5 + 3i

#complex = {'real': 5 , 'i':3}   # i = ghesmat mohomi

#(a+bi) + (c+di) = (a+c) + (b+d)i
#(a+bi) - (c+di) = (a-c) + (b-d)i
#(a+bi)(c+di) = ac + bci + adi + bdi**2 = (ac - bd) + (bc+ad)i
def sum( a, b):
	return a + b
a = complex(2, 3)
b = complex(1, 2)
print(sum(a, b))
#------------------------------#
def sub( a, b):
	return a - b
a = complex(2, 3)
b = complex(1, 2)
print(sub(a, b))
#------------------------------#
def mul( a, b):
	return a * b
a = complex(2, 3)
b = complex(1, 2)
print(mul(a, b))