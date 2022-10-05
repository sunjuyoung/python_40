import random


#임의 수를 생성하고 생성된 수를 맞춘다
random_number = random.randint(1,100)

print(random_number)


game_count = 1

while True:
    
    try:
        
        my_number = int(input("1~100 사이에 숫자를 입력해주세요 :"))
        if my_number > 100:
            print('100이하 숫자를 입력하세요')
        
        if my_number > random_number:
            print('다운')
        elif my_number < random_number:
            print('업')
        elif my_number == random_number:
            print(f"정답 . {game_count}만에 성공")
            break
        
        game_count = game_count +1
    
    except:
        print("숫자를 입력하세요")



