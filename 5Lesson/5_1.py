#Вывести первые N цисел кратные M и больше K
n = int(input('Range'))
m = int(input('M'))
k = int(input('K'))
for i in range(1, n):
    while i % m == 0 and i > k:

        print(i)
        i += 1