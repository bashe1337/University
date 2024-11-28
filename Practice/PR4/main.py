def read_file(fileName):
    with open (f'{fileName}', encoding="utf-8") as f:
        data = (f.read()).lower().split()
        return(sorted(data))

def save_file(fileName, data):
    with open (f'{fileName}', 'w+', encoding="utf-8") as file:
        file.write(f'# Содержимое файла {fileName} \n' + 'Всего уникальных символов: ' + str(len(set(data))) + '\n' + '=' * 15 + '\n')
        for i in range(0, len(data)):
            file.write(data[i] + '\n')
    return 'Data saved'

fileName = input('Введите имя файла: ')
data = read_file(fileName)
save = input("Введите имя файла для сохранения: ")
print(f'{save_file(save, data)}')