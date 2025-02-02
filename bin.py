import numpy as np
count=0
##Поиск числа осуществляется с помощью Бинарного поиска
def binary_search(target):
    low = 0
    high = 100
    global count
##    Сравниваем середину числового отрезка
##    с загаданным числом,отсекаем половину в которую число не попало
    while (low <= high):
        mid = (low + high) // 2
        
        if (mid > target):
            high = mid - 1
            
        elif (mid < target):
            low = mid + 1
        else:
            print('Число попыток: ',count)
            return mid
        
        count=count+1
    return None
print('Введите число X=')
x=int(input())
print('Загаданное число:',binary_search(x))
        
        
                
            
            
        
    
