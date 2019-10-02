from os import system


class ValueWrong(Exception):
    """Wrong Value"""
    pass


def printBoard(gameboard):
    print("\n\n")
    print(f'  {gameboard[0][0]} |  {gameboard[0][1]}  |  {gameboard[0][2]} ')
    print('---------------')
    print(f'  {gameboard[1][0]} |  {gameboard[1][1]}  |  {gameboard[1][2]} ')
    print('---------------')
    print(f'  {gameboard[2][0]} |  {gameboard[2][1]}  |  {gameboard[2][2]} ')


def chooseSign(PlayerSign):
    PlayerSign['player1'] = input("Player1 choose O\\X: ")

    if PlayerSign['player1'] == 'X':
        PlayerSign['player2'] = 'O'
    else:
        PlayerSign['player2'] = 'X'
    print("\n\n")


def printSigns(PlayerSign):
    print("{:<8}| {:<3}\n--------------".format('Player', 'Sign'))
    for p, s in PlayerSign.items():
        print("{:<8}| {:<3}".format(p, s))


def resetGame() -> list:
    Gameboard = [[' ', ' ', ' '],
                 [' ', ' ', ' '],
                 [' ', ' ', ' ']]
    return Gameboard


def checkWin(Gameboard, x, y) -> bool:
    if Gameboard[x - 1][0] == Gameboard[x - 1][1] == Gameboard[x - 1][2]:
        return True
    elif Gameboard[0][y - 1] == Gameboard[1][y - 1] == Gameboard[2][y - 1]:
        return True
    elif x == y and Gameboard[0][0] == Gameboard[1][1] == Gameboard[2][2]:
        return True
    elif x + y - 2 == 2 and Gameboard[0][2] == Gameboard[1][1] == Gameboard[2][0]:
        return True
    return False


def pickPlace(Gameboard, sign) -> bool:
    cellx = celly = -1
    taken = True
    while taken:
        try:
            cellx = int(input("{x} Pick cell row (1-3):".format(x=sign)))
            if cellx < 1 or cellx > 3:
                raise ValueWrong
            celly = int(input("{x} Pick cell column (1-3):".format(x=sign)))
            if celly < 1 or celly > 3:
                raise ValueWrong
        except ValueError:
            print("Wrong value type")
            continue
        except ValueWrong:
            print("Wrong Values")
            continue
        else:
            if Gameboard[cellx - 1][celly - 1] == ' ':
                taken = False

    Gameboard[cellx - 1][celly - 1] = sign
    return checkWin(Gameboard, cellx, celly)


def main():
    system("cls")
    play = True
    while (play):
        Gameboard = resetGame()
        PlayerSign = {'player1': None, 'player2': None}
        chooseSign(PlayerSign)
        printSigns(PlayerSign)
        moves = 0
        while True:
            printBoard(Gameboard)
            if pickPlace(Gameboard, PlayerSign['player1']):
                print("Player 1 won! gogogo {x}".format(x=PlayerSign['player1']))
                break
            printBoard(Gameboard)
            if moves+1==9:
                print("No winnners in this game)")
                break
            if pickPlace(Gameboard, PlayerSign['player2']):
                print("Player 2 won! gogogo {y}".format(y=PlayerSign['player2']))
                break
            moves += 2
        play = False


main()
