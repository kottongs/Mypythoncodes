import random
min = 1
max = 6
while True:
    roll = random.randint(min,max)
    print(roll)
    ask = input('will you like to roll again ? ').lower()
    if ask == 'yes':
        continue
    elif ask == 'no':
        break
    else:
        print("i dont understand you oooo")


