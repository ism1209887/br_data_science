'''Угадай Число'''

import numpy as np

number = np.random.randint(1,100)

count = 0 

while True:
    count+=1
    predict_number = int(input('Угадай число'))
    
    if predict_number < number:
        print('Число Больше')
    elif predict_number > number:
        print('Число Меньше')
    else:
        print(f'Угадал!!! {number} Попытка{count}')
        break 


