import list
import re

lives = 0
score = 0
used = []
choose = (input(f'Выберите уровень сложности:'
              f'\n 1. Легко  - 7 жизней'
              f'\n 2. Средне - 5 жизней'
              f'\n 3. Сложно - 3 жизни\n')).lower()
game = True
while game == True:
    end = False
    match choose:
        case '1' | 'легко':
            lives = 7
        case '2' | 'средне':
            lives = 5
        case '3' | 'сложно':
            lives = 3
    used.clear()
    word = (list.whatWord())
    if word == 'stop':
        print('Все слова закончились, победа!')
        break
    print(f'Загаданное слово состоит из {len(word)} букв')
    answer = '\u25a0' * len(word)
    while lives != 0 and answer != word:
        print('\n\n'+answer)
        guess = (input('Введите одну букву или слово целиком: '))
        if guess in (used) and len(guess) == 1:
            print('Вы уже вводили эту букву!')
        elif guess in (used) and len(guess) != 1:
            print('Вы уже вводили это слово!')
        else:
            used.append(guess)
            if guess not in word and len(guess)==1:
                lives -= 1
                print(f'Вы ошиблись\n\nУ вас осталось {lives} жизней')
            elif guess not in word and len(guess) != 1:
                lives == 0
                print(f'Вы проиграли!\n\n')
            elif guess == word:
                print(f'Вы угадали слово {word}\n')
                answer = guess
            elif guess in word and len(guess) == 1:
                print('Вы угадали букву!\n')
                for i in range(0, len(word)):
                    if word[i] == guess:
                        answered = answer[:i]+guess+answer[i+1:]
                        answer = answered
        if answer == word:
            score += 1
            end = True
        elif lives == 0:
            end = True
        if end == True:
            new_game = (input(f'\n\nБыло загадано слово {word}\nХотите сыграть еще?' f'\n1.Да' f'\n2.Нет\n')).lower()
            match new_game:
                case '1'|'да':
                    game = True
                case _:
                    game = False