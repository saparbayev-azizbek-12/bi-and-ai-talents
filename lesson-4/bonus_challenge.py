import random
user = 0
computer = 0
mylist = [1,2,3]
while True:
    user_think = input("Choose one of them: 'rock', 'paper', 'scissors'\nInput format: rock => 1, paper => 2, scissors => 3\n>>> ")
    if user_think in ['1', '2', '3']:
        user_think = int(user_think)    
        computer_think = random.randint(1,3)
        if user_think == computer_think:
            user += 1
            if user == 5:
                print("Congratulations, you won.")
                break
            print(f'Good. You found. Shoot: user {user} : {computer} computer')
            print('-'*50)
        else:
            computer += 1
            if computer == 5:
                print("Unfortunately, you lost.")
                break
            print(f'Bad news. You not found. Shoot: user {user} : {computer} computer')
            print('-'*50)

    else:
        print('Please enter only 1,2 or 3')

