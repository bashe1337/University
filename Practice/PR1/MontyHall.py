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