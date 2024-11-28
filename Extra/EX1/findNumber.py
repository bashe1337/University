import random

computerNum = random.randint(0, 100)
userNum = input('Компьютер загадал число!\nВведите ваш ответ: ')
tryes = 0
exit = 0

while True:
    if userNum.lower() == 'выход':
        print('Выходим!')
        exit = 1
        break
    elif int(userNum) > computerNum:
        print('Ваше число больше!')
        tryes += 1
    elif int(userNum) < computerNum:
        print('Ваше число меньше')
        tryes += 1
    else:
        tryes += 1
        break
    userNum = input('Попробуйте еще!\nВведите ваш ответ: ')
if exit == 0:
    print(f'Поздравляем! Вы угадали число {computerNum} за {tryes} попытки!')
