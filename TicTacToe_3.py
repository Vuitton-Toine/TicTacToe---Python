####################
# FUNCTION SECTION #
####################
def display_board(grid):
    print(grid[7], '|', grid[8], '|', grid[9])
    print(grid[4], '|', grid[5], '|', grid[6])
    print(grid[1], '|', grid[2], '|', grid[3])

def prompt_input(char, player):
    is_taken = False
    while not is_taken:
        try:
            player_choice = int(input("Enter number between (1-9): "))
            if grid[player_choice].upper() == 'X' or grid[player_choice].upper() == 'O':
                print('Already taken! Please make another selection.')
            elif player_choice == 0:
                print('Selection out of acceptable range. Please enter valid number (1-9).')
            else:
                # This is where the player's choice gets recorded on the grid.
                grid[player_choice] = char
                if player == 'p1':
                    p1_selections.append(player_choice)
                    winner_check(player, p1_selections)
                elif player == 'p2':
                    p2_selections.append(player_choice)
                    winner_check(player, p2_selections)
                is_taken = True
        except IndexError:
            print('Selection out of acceptable range. Please enter valid number (1-9).')
        except ValueError:
            print('Enter a whole number.')


def play_game():
    turns = 0
    while turns < 9:
        if turns == 0:
            p1_char = ''
            char_select = False
            while char_select == 0:
                p1_char = (input("Player One, enter preferred character: ")).upper()
                if p1_char.upper() == 'X' or p1_char.upper() == 'O':
                    pass
                    if p1_char == 'X':
                        p2_char = 'O'
                        char_select = 1
                    if p1_char == 'O':
                        p2_char = 'X'
                        char_select = 1
                else:
                    print('Please enter "X" or "O"')
        if turns % 2 == 0:
            char = p1_char
            player = 'p1'
            print("It is player one's turn.")
        elif turns % 2 == 1:
            char = p2_char
            player = 'p2'
            print("It is player two's turn.")
        prompt_input(char, player)
        display_board(grid)

        turns += 1

    if turns == 9:
        prompt_replay = str(input('Game over! Replay? (Y/N):')).upper()
        if prompt_replay == 'Y':
            restart()
        else:
            print('Thanks for playing!')

def winner_check(player, selections):
    for winning_pattern in winning_patterns:
        # for cell in winning_pattern:
        i = 0
        three_to_win = 0
        while i < len(winning_pattern):
            if (winning_pattern[i]) in selections:
                three_to_win += 1
                if three_to_win == 3:
                    print(f'{player} is the winner!')
                else:
                    pass
            i += 1

def restart():
    for i in range(1, 10):
        grid[i] = ' '
    play_game()

p1_selections = []
p2_selections = []

winning_patterns = [
    [7,8,9],[4,5,6,],[1,2,3],
    [7,4,1],[8,5,2],[9,6,3],
    [7,5,3],[9,5,1]
]

grid = [' '] * 10

play_game()
