from random import randint

player = 50

while player != 100 and player != 0:
    coin = randint(1, 2)
    guess = int(input("숫자 1 또는 2: "))

    if guess == coin:
        player += 9
        print("coin:", player)
    else:
        player -= 10
        print("coin:", player)


print("게임 종료")