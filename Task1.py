#Представим список в виде переменной:

Season = ["Winter","Spring","Summer","Autumn"]

#Пример кода, создание дека на Python при помощи deque:
#Метод Deque(Double-Ended Queue) позволяет вставлять и удалять элементы как сначала так и с конца 

from collections import deque
d = deque() 
d.append('1')
d.append('2')
d.append('3')
print(d)




