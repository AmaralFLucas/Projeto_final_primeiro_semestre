import random
import os
import time
player1 = str(input("Jogador 1 informe seu nome: "))
player2 = str(input("Jogador 2 informe seu nome: "))
def tabuleiro(posicao1, posicao2):
    jogador1 = ['','','','','','','','','','','']
    jogador2 = ['','','','','','','','','','','']
    jogador1[posicao1] = "X"
    jogador2[posicao2] = "X"
    print(f"{player1}: {jogador1}")
    print(f"{player2}: {jogador2}")
    time.sleep(3)
    os.system('cls') 

def rolarDado():
    tecla = input("Pressione 'Enter' para rolar o dado.")
    if tecla == "":
        dado = random.randint(1, 3)
    os.system('cls')
    return(dado)

def vezJogador1(posicao1, dado):
    casa = posicao1+dado
    acertou = perguntas1(casa)
    if acertou == True:
        print("Você acertou.")
        posicao1 = casa
    else:
        print("Você errou!")
    time.sleep(3)
    os.system('cls')
    return(posicao1)   

def vezJogador2(posicao2, dado):
    casa = posicao2+dado
    acertou = perguntas2(casa)
    if acertou == True:
        print("Você acertou.")
        posicao2 = casa
    else:
        print("Você errou!")
    time.sleep(3)
    os.system('cls')
    return(posicao2)

def perguntas1(casa):
    acertou = False
    with open('perguntas_e_respostas.txt', 'r',  encoding='utf-8') as arquivo:
        pergunta = arquivo.readlines()
        if casa == 1:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[0]}{pergunta[1]}{pergunta[2]}{pergunta[3]}{pergunta[4]}{pergunta[5]}\nR:"))
            if resposta == "b" or resposta == "B":
                acertou = True
        elif casa == 2:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[6]}{pergunta[7]}{pergunta[8]}{pergunta[9]}{pergunta[10]}{pergunta[11]}\nR:"))
            if resposta == "c" or resposta == "C":
                acertou = True
        elif casa == 3:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[12]}{pergunta[13]}{pergunta[14]}{pergunta[15]}{pergunta[16]}{pergunta[17]}\nR:"))
            if resposta == "c" or resposta == "C":
                acertou = True
        elif casa == 4:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[18]}{pergunta[19]}{pergunta[20]}{pergunta[21]}{pergunta[22]}{pergunta[23]}\nR:"))
            if resposta == "a" or resposta == "A":
                acertou = True
        elif casa == 5:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[24]}{pergunta[25]}{pergunta[26]}{pergunta[27]}{pergunta[28]}{pergunta[29]}\nR:"))
            if resposta == "e" or resposta == "E":
                acertou = True
        elif casa == 6:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[30]}{pergunta[31]}{pergunta[32]}{pergunta[33]}{pergunta[34]}{pergunta[35]}\nR:"))
            if resposta == "b" or resposta == "B":
                acertou = True
        elif casa == 7:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[36]}{pergunta[37]}{pergunta[38]}{pergunta[39]}{pergunta[40]}{pergunta[41]}\nR:"))
            if resposta == "b" or resposta == "B":
                acertou = True
        elif casa == 8:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[42]}{pergunta[43]}{pergunta[44]}{pergunta[45]}{pergunta[46]}{pergunta[47]}\nR:"))
            if resposta == "c" or resposta == "C":
                acertou = True
        elif casa == 9:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[48]}{pergunta[49]}{pergunta[50]}{pergunta[51]}{pergunta[52]}{pergunta[53]}\nR:"))
            if resposta == "d" or resposta == "D":
                acertou = True
        elif casa == 10:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[54]}{pergunta[55]}{pergunta[56]}{pergunta[57]}{pergunta[58]}{pergunta[59]}\nR:"))
            if resposta == "a" or resposta == "A":
                acertou = True
        os.system('cls')
        return(acertou)

def perguntas2(casa):
    acertou = False
    with open('perguntas_e_respostas.txt', 'r',  encoding='utf-8') as arquivo:
        pergunta = arquivo.readlines()
        if casa == 1:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[60]}{pergunta[61]}{pergunta[62]}{pergunta[63]}{pergunta[64]}{pergunta[65]}\nR:"))
            if resposta == "d" or resposta == "D":
                acertou = True
        elif casa == 2:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[66]}{pergunta[67]}{pergunta[68]}{pergunta[69]}{pergunta[70]}{pergunta[71]}\nR:"))
            if resposta == "e" or resposta == "E":
                acertou = True
        elif casa == 3:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[72]}{pergunta[73]}{pergunta[74]}{pergunta[75]}{pergunta[76]}{pergunta[77]}\nR:"))
            if resposta == "a" or resposta == "A":
                acertou = True
        elif casa == 4:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[78]}{pergunta[79]}{pergunta[80]}{pergunta[81]}{pergunta[82]}{pergunta[83]}\nR:"))
            if resposta == "d" or resposta == "D":
                acertou = True
        elif casa == 5:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[84]}{pergunta[85]}{pergunta[86]}{pergunta[87]}{pergunta[88]}{pergunta[89]}\nR:"))
            if resposta == "e" or resposta == "E":
                acertou = True
        elif casa == 6:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[90]}{pergunta[91]}{pergunta[92]}{pergunta[93]}{pergunta[94]}{pergunta[95]}\nR:"))
            if resposta == "c" or resposta == "C":
                acertou = True
        elif casa == 7:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[96]}{pergunta[97]}{pergunta[98]}{pergunta[99]}{pergunta[100]}{pergunta[101]}\nR:"))
            if resposta == "e" or resposta == "E":
                acertou = True
        elif casa == 8:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[102]}{pergunta[103]}{pergunta[104]}{pergunta[105]}{pergunta[106]}{pergunta[107]}\nR:"))
            if resposta == "a" or resposta == "A":
                acertou = True
        elif casa == 9:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[108]}{pergunta[109]}{pergunta[110]}{pergunta[111]}{pergunta[112]}{pergunta[113]}\nR:"))
            if resposta == "e" or resposta == "E":
                acertou = True
        elif casa == 10:
            resposta = str(input(f"Responda corretamente a pergunta abaixo:\n{pergunta[114]}{pergunta[115]}{pergunta[116]}{pergunta[117]}{pergunta[118]}{pergunta[119]}\nR:"))
            if resposta == "e" or resposta == "E":
                acertou = True
        os.system('cls')    
        return(acertou)

def iniciar(): 
    print("-----------------")
    print("----BEM VINDO----")
    print("-------AO--------")
    print("----TABULEIRO----")
    print("-----------------")
    jogando()

def jogando():
    jogador = 1
    jogar = True
    posicao1 = 0
    posicao2 = 0
    tabuleiro(posicao1, posicao2)
    time.sleep(3)
    os.system('cls')
    while jogar:
        if jogador == 1:    
            print(f"\nJogador {player1}, vamos rolar o dado!")
        else:
            print(f"\nJogador {player2}, vamos rolar o dado!")
        dado = rolarDado()
        if dado != 0:
            if jogador == 1:
                posicao1 = vezJogador1(posicao1, dado)
                if posicao1 >= 10:
                    print(f"\n\nParebéns {player1} você venceu!")
                    posicao1 = 10
                    jogar = False
                else:
                    jogador = 2
            elif jogador == 2:
                posicao2 = vezJogador2(posicao2, dado)
                if posicao2 >= 10:
                    print(f"\n\nParebéns {player2} você venceu!")
                    posicao2 = 10
                    jogar = False
                else:
                    jogador = 1
            tabuleiro(posicao1, posicao2)
        else:
            print("Algo deu errado.")
        time.sleep(2)
        os.system('cls')

iniciar()