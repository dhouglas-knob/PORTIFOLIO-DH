import random
#Random Integer (Range): Use random.randint(a, b) to get an integer between a and b (inclusive).
print(f"Escolha o tipo de Jokenpô: \n Digite 1 - Humano x Humano \n Digite 2 - Humano x Maquina \n Digite 3 - para Maquina x Maquina")
escolha_modalidade = int(input())

player1_score = 0
player2_score = 0

while(True):

    if(escolha_modalidade == 1):
        
        print(f"Player 1 \n Digite 1 - Para pedra \n Digite 2 - Para Papel \n Digite 3 - Para Tesoura")
        escolha_player1 = int(input())

        if(escolha_player1 == 1):
            tipo_player1 = "Pedra"

        if(escolha_player1 == 2):
            tipo_player1 = "Papel"

        if(escolha_player1 == 3):
            tipo_player1 = "Tesoura"

        print(f"Player 2 \n Digite 1 - Para pedra \n Digite 2 - Para Papel \n Digite 3 - Para Tesoura")
        escolha_player2 = int(input())

        if(escolha_player2 == 1):
            tipo_player2 = "Pedra"

        if(escolha_player2 == 2):
            tipo_player2 = "Papel"

        if(escolha_player2 == 3):
            tipo_player2 = "Tesoura"

        print(f"O jogador 1 escolheu: {tipo_player1}\nO jogador 2 escolheu: {tipo_player2}")
        
        #Se escolha foi igual
        if(escolha_player1 == escolha_player2):
            print(f"Empate")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Papel = Papel win
        elif(escolha_player1 == 1  and  escolha_player2 == 2):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")

            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Tesoura = Pedra win
        elif(escolha_player1 == 1  and  escolha_player2 == 3):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Papel vs Pedra = Papel win
        elif(escolha_player1 == 2 and  escolha_player2 == 1):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Papel vs Tesoura = Tesoura win
        elif(escolha_player1 == 2 and  escolha_player2 == 3):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Tesoura = Pedra win
        elif(escolha_player1 == 3 and  escolha_player2 == 1):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Tesoura vs Papel = Tesoura win
        elif(escolha_player1 == 3 and  escolha_player2 == 2):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        else:
            print(f"Error")
            break

    elif(escolha_modalidade == 2):
        print(f"Player 1 \n Digite 1 - Para pedra \n Digite 2 - Para Papel \n Digite 3 - Para Tesoura")
        escolha_player1 = int(input())

        if(escolha_player1 == 1):
            tipo_player1 = "Pedra"

        if(escolha_player1 == 2):
            tipo_player1 = "Papel"

        if(escolha_player1 == 3):
            tipo_player1 = "Tesoura"

        escolha_player2 = random.randint(1, 3)

        if(escolha_player2 == 1):
            tipo_player2 = "Pedra"

        if(escolha_player2 == 2):
            tipo_player2 = "Papel"

        if(escolha_player2 == 3):
            tipo_player2 = "Tesoura"

        print(f"O jogador 1 escolheu: {tipo_player1}\nO jogador 2 escolheu: {tipo_player2}")
        
        #Se escolha foi igual
        if(escolha_player1 == escolha_player2):
            print(f"Empate")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Papel = Papel win
        elif(escolha_player1 == 1  and  escolha_player2 == 2):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")

            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Tesoura = Pedra win
        elif(escolha_player1 == 1  and  escolha_player2 == 3):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Papel vs Pedra = Papel win
        elif(escolha_player1 == 2 and  escolha_player2 == 1):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Papel vs Tesoura = Tesoura win
        elif(escolha_player1 == 2 and  escolha_player2 == 3):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Tesoura = Pedra win
        elif(escolha_player1 == 3 and  escolha_player2 == 1):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Tesoura vs Papel = Tesoura win
        elif(escolha_player1 == 3 and  escolha_player2 == 2):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        else:
            print(f"Error")
            break

    elif(escolha_modalidade == 3):
        escolha_player1 = random.randint(1, 3)

        if(escolha_player1 == 1):
            tipo_player1 = "Pedra"

        if(escolha_player1 == 2):
            tipo_player1 = "Papel"

        if(escolha_player1 == 3):
            tipo_player1 = "Tesoura"

        escolha_player2 = random.randint(1, 3)

        if(escolha_player2 == 1):
            tipo_player2 = "Pedra"

        if(escolha_player2 == 2):
            tipo_player2 = "Papel"

        if(escolha_player2 == 3):
            tipo_player2 = "Tesoura"

        print(f"O jogador 1 escolheu: {tipo_player1}\nO jogador 2 escolheu: {tipo_player2}")
        
        #Se escolha foi igual
        if(escolha_player1 == escolha_player2):
            print(f"Empate")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Papel = Papel win
        elif(escolha_player1 == 1  and  escolha_player2 == 2):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")

            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Tesoura = Pedra win
        elif(escolha_player1 == 1  and  escolha_player2 == 3):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Papel vs Pedra = Papel win
        elif(escolha_player1 == 2 and  escolha_player2 == 1):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Papel vs Tesoura = Tesoura win
        elif(escolha_player1 == 2 and  escolha_player2 == 3):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Pedra vs Tesoura = Pedra win
        elif(escolha_player1 == 3 and  escolha_player2 == 1):
            print(f"Player 2 Venceu")
            player2_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        #Tesoura vs Papel = Tesoura win
        elif(escolha_player1 == 3 and  escolha_player2 == 2):
            print(f"Player 1 Venceu")
            player1_score += 1
            print(f"Player 1: {player1_score} Pontos\nPlayer 2: {player2_score} Pontos")
            print(f"Se deseja continuar digite 1 - \nse Deseja parar digite 0")
            
            escolha_continua = int(input())

            if(escolha_continua == 0):
                break

            elif(escolha_continua == 1):
                continue

            else:
                print(f"Valor inválido. Digite 0 para sair ou 1 para continuar.")
                break

        else:
            print(f"Error")
            break

    else:
        print(f"Error")
        break

print(f"Jogo feito por: Dhouglas ,Leandro ,Murilo")