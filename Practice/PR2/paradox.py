import random

def montyHall(iterations):

    guest = 0 
    master = 0 

    for i in range(0, iterations):
        prize = random.randint(1, 3) 
        choose = random.randint(1, 3) 
        if prize == choose:
            guest += 1
        else:
            master += 1
    return(f'если участник оставит свой выбор, то выигрышь составит: \n{guest} ({format((100 / (iterations / guest)), ".2f")}%)'
          f' \nиначе: \n{master}({format((100 / (iterations / master)), ".2f")}%)')


if __name__ == '__main__':
	iterations = int((input('Введите кол-во итераций: ')))
	print(montyHall(iterations))

def birthday(people, repeats):
    answer = 0 
    for i in range(0, repeats):
        unique_days = set()
        for j in range(0, people):
            unique_days.add(random.randint(1,365))
        if len(unique_days) != people:
            answer += 1
    return(f'\tкол-во групп, в которых были как минимум два человека с одинаковыми днями рождения:'
           f'\n{answer}\n\tпроцент групп, в которых были как минимум два человека с одинаковыми днями рождения:\n{format((100/(repeats/answer)), ".2f")}%')

if __name__ == '__main__':
	group = int((input('Введите кол-во человек в группе: ')))
	iterations = int((input('Введите кол-во итераций: ')))
	print(birthday(group, iterations))