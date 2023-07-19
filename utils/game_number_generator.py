import random
import sys

def generate_numbers(game_name,games):
    if game_name == 'lot':
        unique_gen_nums = 6
        max_num = 45
        for game in range(games):
                numbers = [random.randint(1,45) for x in range(unique_gen_nums)]
                print("{}  {} {} {} {} {} {}".format(game+1, numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5]))
    elif game_name == 'sfl':
        unique_gen_nums = 7
        for game in range(games):
            numbers = [random.randint(1,44) for x in range(unique_gen_nums)]
            print("{}  {} {} {} {} {} {} {}".format(game+1, numbers[0],numbers[1],numbers[2],numbers[3],numbers[4],numbers[5],numbers[6]))
    else:
        print("\nUnknown Game of {}\n".format(game_name))
        #sys.exit()

if __name__ == '__main__':
    while True:
        try:
            gameName = input('Enter Name of the Game: ')
            if gameName == 'quit' or gameName == 'exit':
                break
            gameNumber = int(input('Enter Number of Games: '))
            generate_numbers(gameName, gameNumber)
        except ValueError:
            print('Thats an error, pal!  Try again\n')
            next
        
        