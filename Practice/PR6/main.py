with open('data.txt', encoding='utf-8') as file:
    lines = file.read().splitlines()
    for i in range(len(lines) -1, -1, -1):
        if lines[i][0] != 'Р':
            del(lines[i])
    for i in range(0, len(lines)):
        lines[i] = lines[i].split()
    with open('saved.txt', 'w+', encoding='utf-8') as f:
        for i in range(len(lines)):
            f.write(f'{lines[i][6]} - Поезд №{lines[i][1]} {lines[i][3]} {lines[i][4]} \n')
    print('Файл прочитан и сохранен!')