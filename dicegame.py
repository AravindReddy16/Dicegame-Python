import random

dice={
    1:('''
          ------- 
         |       |
         |   *   |
         |       |
          ------- 
    '''),
    2:('''
          ------- 
         |       |
         |  * *  |
         |       |
          ------- 
    '''),
    3:('''
          ------- 
         |       |
         |  * *  |
         |   *   |
          ------- 
    '''),
    4:('''
          ------- 
         |  * *  |
         |       |
         |  * *  |
          ------- 
    '''),
    5:('''
          ------- 
         | *   * |
         |   *   |
         | *   * |
          ------- 
    '''),
    6:('''
          ------- 
         | *   * |
         | *   * |
         | *   * |
          ------- 
    '''),
}

person_score=0
computer_score=0

def info():
    print(f'Your Score: {person_score}')
    print(f'Computer Score: {computer_score}')
    print(f'Person : {dice[person]}')
    print(f'Computer: {dice[computer]}')

while True:
    if person_score!=5 and computer_score!=5:
        enter=input('Type [Y/N] to continue: ').lower()
        if enter=='y':
            person=random.randint(1,6)
            computer=random.randint(1,6)
            if person>computer:
                person_score+=1
                info()
            elif person==computer:
                info()
            else:
                computer_score+=1
                info()
        elif enter=='n':
            print('Exiting from Game...')
            break
        else:
            print('Invalid Input...')
    else:
        if person_score==5:
            print('You won the Game')
        elif computer_score==5:
            print('Computer won the Game')
        print('Game Over')
        break