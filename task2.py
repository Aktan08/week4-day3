# 2) Если вы были на Луне сейчас, ваш вес будет 16,5% от вашего веса земли.
# Для его расчета необходимо умножить на 0,165. Если в ближайшие 15 лет ваш вес
# будет
# увеличение на 1 кг каждый год. Какой будет ваш вес каждый год на Луне в следующем
# 15 лет?

from functools import reduce
a = float(input())*0.165
list_=[]
for num in range(15):
    a+=1
    list_.append(a)
print(list(enumerate(list_)))
    
    
