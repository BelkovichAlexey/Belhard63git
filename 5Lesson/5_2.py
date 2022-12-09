#Сделать калькулятор: у пользователя
#спрашивается число, потом действие и второе
#число
n1 = int(input('number1:'))
s = input('symbol:')
n2 = int(input('number2:'))
if s == '+':
    a = n1 + n2
elif s == '-':
    a = n1 - n2
elif s == '*':
    a = n1 * n2
elif s == '/':
    a = n1 / n2
print(int(a))
