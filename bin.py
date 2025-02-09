import numpy as np

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
##    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

def binary_search(target):
    low = 0
    high = 100
    global count
    count=0
    while (low <= high):
        mid = (low + high) // 2
        
        if (mid > target):
            high = mid - 1
            
        elif (mid < target):
            low = mid + 1
        else:
            return count      
        count=count+1
    return None        
score_game(binary_search)        
                
            
