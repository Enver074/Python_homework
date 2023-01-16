
board = list(range(1,10))
def draw_board(board):
    print ("─" * 13)
    for i in range(3):
        print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
        print("─" * 13)
def players_move(token):
    valid = False
    while not valid:
        players_turn = int(input(f"Ходит {token}: "))
        if players_turn >= 1 and players_turn <= 9:
            if (str(board[players_turn-1]) not in "XO"):
                board[players_turn - 1] = token
                valid = True
            else:
                print("Эта клетка занята")
        else:
            print("Некорректный ввод, введите число от 1 до 9")

def check_win(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_coord:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            players_move("X")
        else:
            players_move("0")
        counter += 1
        if counter > 4:
            tmp = check_win(board)
            if tmp:
                print (tmp, "выиграл!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    draw_board(board)

main(board)