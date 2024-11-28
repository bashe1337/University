def read_file(fileName):
    try:
        file = open (f'{fileName}', encoding="utf-8")
    except FileNotFoundError:
        print(f'Файл {fileName} не найден!')
    except OSError:
        print('Недопустимые символы!')
    except ValueError:
        print('Содержимое файла некорректной структуры!')
    else:
        data = file.read().split()
        if len(data) == 0:
            file.close()
            return (print('Файл пуст!'))
        for i in range(len(data)):
            if data[i].isdigit() != True:
                data = 'В файле содержатся не только числа!'
                return (print(data))
        for i in range(0, len(data)):
            data[i] = int(data[i])
        if int(data[0]) == 0:
            data = 'Число в первой строке равно нулю.\n'
        elif int(data[0]) + 1 > len(data):
            file.close()
            return (print('Число в первой строке больше, чем чисел в файле!'))
        elif int(data[0]) + 1 < len(data):
            file.close()
            return (print('Число в первой строке меньше, чем чисел в файле!'))
        file.close()
        if str(data[0]).isdigit():
            data.pop(0)
        return(print(data))
    
dataName = input('Введите имя файла, который вы желаете открыть и вывести: ')
data = read_file(dataName)