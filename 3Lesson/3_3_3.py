z = input('Name:')
x = int(input('Age:'))   # int пришлось вставить, %d воспринимал как строку а это число, ошибку писал
c = input('City:')
q = 'My name is %s. I am %d years old. I am from %s, Thanks!' % (z, x, c)
print(q)
