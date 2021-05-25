def div( a , b = 2,c =100):
    return (a / b)+c
print('div(4) =', div(4))
print('div(4) =', div(3 , 10 , 20))
print('div(4) =', div(3 ,c=50,  b=4))
print('div(6, 3) =', div(b=3,  a = 7 ))