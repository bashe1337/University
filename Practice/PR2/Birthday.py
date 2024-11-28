import random

def birthday(people, repeats):
    answer = 0 
    for i in range(0, repeats):
        unique_days = set()
        for j in range(0, people):
            unique_days.add(random.randint(1,365))
        if len(unique_days) != people:
            answer += 1
    return(f'кол-во групп, в которых были как минимум два человека с одинаковыми днями рождения:'
           f'\n{answer}\nпроцент групп, в которых были как минимум два человека с одинаковыми днями рождения:\n{format((100/(repeats/answer)), ".2f")}%')

if __name__ == '__main__':
	group = int((input('Введите кол-во человек в группе: ')))
	iterations = int((input('Введите кол-во итераций: ')))
	print(birthday(group, iterations))