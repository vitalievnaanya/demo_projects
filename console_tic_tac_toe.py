def read_first_player_sign(first_player_name):
    while True:
        first_player_sign = input(f'{first_player_name} would you like to play with X or O? ').upper()
        if first_player_sign in ['X', 'O']:
            return  first_player_sign


def read_players_info():
    first_player_name = input(f'Player one name: ')
    second_player_name = input(F'Player two name: ')

    first_player_sign = read_first_player_sign(first_player_name)
    second_player_sign = 'O' if first_player_sign == 'X' else 'X'
    return [first_player_name, first_player_sign], [second_player_name, second_player_sign]


def print_board_numeration():
    print(f'This is the numeration of the board:')
    print('|  1  ||  2  ||  3  |')
    print('|  4  ||  5  ||  6  |')

    print('|  7  ||  8  ||  9  |')


def get_cords_by_pos(position):
    if position == 1:
        return 0, 0
    if position == 2:
        return 0, 1
    if position == 3:
        return 0, 2
    if position == 4:
        return 1, 0
    if position == 5:
        return 1, 1
    if position == 6:
        return 1, 2
    if position == 7:
        return 2, 0
    if position == 8:
        return 2, 1
    if position == 9:
        return 2, 2
    raise IndexError(f'Position is invalid. Please provide a valid position  in range [1-9]!')


def display_board(matrix):
    for row in matrix:
        print('|  ', end='')
        print('  |  '.join(row), end='')
        print('  |')


def is_board_full(matrix):
    for row in matrix:
        is_row_full = all([el != ' ' for el in row])
        if not is_row_full:
            return False
    return True


def has_player_won(matrix, player_sign):
    for row in matrix:
        if all([el == player_sign for el in row]):
            return True

    for col in range(len(matrix)):
        won = True
        for row in range(len(matrix)):
            if matrix[row][col] != player_sign:
                won = False
                break
        if won:
            return True

    won = True
    for idx in range(len(matrix)):
        if matrix[idx][idx] != player_sign:
            won = False
            break
    if won:
        return True

    won = True
    for idx in range(len(matrix)):
        if matrix[idx][len(matrix) - 1 - idx] != player_sign:
            won = False
            break
    return won




def play(matrix, p1, p2):
    turn = 1
    players_turn = {0: p2, 1: p1}
    while True:
        name, sign = players_turn[turn % 2]

        try:
            position = int(input(f'{name} choose a free position [1-9]: '))
            row, col = get_cords_by_pos(position)

            if matrix[row][col] != ' ':
                raise IndexError(f'Position is already taken. Please choose a free position!')

            matrix[row][col] = sign
            turn += 1

            display_board(matrix)

            if has_player_won(matrix, sign):
                print(f'{name} has won!')
                break

            if is_board_full(matrix):
                print('Draw!')
                break

        except ValueError:
            print('Please provide a valid position in range [1-9]!')
        except IndexError as error:
            print(error)


player1, player2 = read_players_info()

print_board_numeration()

print(f'{player1[0]} starts first')

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

play(board, player1, player2)