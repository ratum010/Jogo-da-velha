def interface():
    print("   0   1   2")
    print("0 [{}] [{}] [{}]".format(board[0][0], board[0][1], board[0][2]))
    print("1 [{}] [{}] [{}]".format(board[1][0], board[1][1], board[1][2]))
    print("2 [{}] [{}] [{}]".format(board[2][0], board[2][1], board[2][2]))

def ValidarVitoria():
    if board[0][0] == board[0][1] == board[0][2] != " ":
        return True
    elif board[1][0] == board[1][1] == board[1][2] != " ":
        return True
    elif board[2][0] == board[2][1] == board[2][2] != " ":
        return True
    elif board[0][0] == board[1][0] == board[2][0] != " ":
        return True
    elif board[0][1] == board[1][1] == board[2][1] != " ":
        return True
    elif board[0][2] == board[1][2] == board[2][2] != " ":
        return True
    elif board[0][0] == board[1][1] == board[2][2] != " ":
        return True
    elif board[0][2] == board[1][1] == board[2][0] != " ":
        return True
    else:
        return False

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

parar = False
rodada = "X"
jogadas = 0

while parar == False:
    interface()

    linha = int(input("Selecione a linha: "))
    coluna = int(input("Selecione a coluna: "))

    if rodada == "X":
        board[linha][coluna] = "X"
        jogadas += 1
        rodada = "O"
    elif rodada == "O":
        board[linha][coluna] = "O"
        jogadas += 1
        rodada = "X"

    if ValidarVitoria():
        interface()
        parar = True
        print("Vitória!")
    elif jogadas == 9:
        interface()
        parar = True
        print("Empate!")