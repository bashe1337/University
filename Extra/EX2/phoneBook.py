users = {}

while True:
    print('Телефонная книга\n\n1.Добавить новый контакт\n2.Удалить существующий контакт (по имени)\n3.Посмотреть список контактов\n4.Изменить номер контакта (по имени)\n5. Выход.')
    action = input('Введите номер функции: ')

    if action == '1':
        name = input('Введите название для контакта: ').title()
        if name in users.keys():
            input('Контакт уже существует!')
        else:
            phone = input('Введите номер: ')
            phone = phone.replace(' ','')
            if len(phone) <= 12 and len(phone) >= 10 and not(any(c.isalpha() for c in phone)):
                if phone[0] == '8':
                    phone = phone.replace('8','+7', 1)
                elif phone[0] == '9':
                    phone = phone.replace('9','+79', 1)
                users[name] = phone
                print('Контакт успешно добавлен!')
            else:
                input('Недопустимый номер!')

    elif action == '2':
        name = input('Введите имя контакта, который желаете удалить: ').title()
        del users[name]


    elif action == '3':
        for key, data in users.items():
            print(key, data)
        continue


    elif action == '4':
        name = input('Введите название для контакта: ').title()
        phone = input('Введите номер телефона: ')
        phone = phone.replace(' ','')
        if len(phone) <= 12 and len(phone)>=10 and not(any(c.isalpha() for c in phone)):
            if phone[0] == '8':
                phone = phone.replace('8','+7',1)
            elif phone[0] == '9':
                phone = phone.replace('9','+79',1)
            users[name] = phone
            print('Контакт успешно изменен!')
        else:
            input('Недопустимый номер!')
            
    elif action == '5':
        break