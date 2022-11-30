z = float(input('Number1:'))        #float ,так как думаю int не подходит, если ввести дробное число
x = float(input('Number2:'))
c = float(input('Number3:'))
q = (z > 0) + (x > 0) + (c > 0)     #True,False
print('Положительное', q)
w = (z < 0) + (x < 0) + (c < 0)
print('Отрицательное', w)