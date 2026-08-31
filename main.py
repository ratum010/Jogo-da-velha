def interface():
    print("   A   B   C")
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

    
    try:
        linha = int(input("Selecione a linha(0, 1, 2): "))
        if linha < 0 or linha > 2:
            print("Linha inválida!")
            continue
    except ValueError:
        print("Entrada inválida! Por favor, insira um número.")
        continue

    coluna = input("Selecione a coluna(A, B, C): ").upper()
    try:
        if coluna == "A":
            coluna = 0
        elif coluna == "B":
            coluna = 1
        elif coluna == "C":
            coluna = 2
        else:
            raise ValueError("Coluna inválida!")

    except ValueError:
        print("Entrada inválida! Por favor, insira uma letra válida.")
        continue


    if rodada == "X":
        if board[linha][coluna] != " ":
            print("Posição já ocupada!")
            continue
        board[linha][coluna] = "X"
        jogadas += 1
        rodada = "O"
    elif rodada == "O":
        if board[linha][coluna] != " ":
            print("Posição já ocupada!")
            continue
        board[linha][coluna] = "O"
        jogadas += 1
        rodada = "X"

    if ValidarVitoria():
        interface()
        parar = True
        print("Vitória do jogador {}!".format(rodada))
    elif jogadas == 9:
        interface()
        parar = True
        print("Empate!")