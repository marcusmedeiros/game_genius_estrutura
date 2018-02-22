#**********************************************#
# Trabalho de Estrutura de Dados - Jogo Genius #
# FADERGS - 2ª SEMESTRE                        #
# Programadores: Marcus Medeiros               #
#                Felipe Santos                 #
#                Filipe Cemim                  #
#                Rene Danni                    #
# Data de Criacao: 14/06/2017                  #
# Versao: 1.6                                  #
# Versao do python: 2.7                        #
#**********************************************#

from random import randint
from threading import Timer
import time
import os
import sys

#Cria listas de cores do jogo e do jogador
gameList = []
playerList = []
#Cria listas de ranking e ranking ordenado de jogadores
rankingList = []
rankingOrderList = []

#Cria dicionario de cores
cores = {
    1: 'vermelho',
    2: 'azul',
    3: 'amarelo',
    4: 'verde'
}

#Cria dicionario de elogios
elogio = {
    1: 'Sweet!',
    2: 'Tasty!',
    3: 'Delicious!',
    4: 'Divine!',
    5: 'Sugar Crush!',
    6: 'Moon Struck!',
    7: 'Frogastic!'
}

#Funcao de limpar tela com teste de sistema operacional (Em windows 'cls' em unix 'clear)
def limpa():
    #os.system('cls' if os.name == 'nt' else 'clear')
    os.system('cls' if sys.platform.startswith('win') else 'clear')

#Funcao que gera um numero randomico de 1 a 4 e insere na lista de cores do jogo com o uso do dicionario
def geraCor():
    del playerList[:] #Limpa lista de cores do jogo
    geniusCor = randint(1,4) #Gerado numero randomico de 1 a 4 para a variavel geniusCor
    gameList.append(cores[geniusCor]) #Faz append na lista de cores do jogo utlizando a variavel geniusCor e o dicionario de cores


#Funcao que grava cor e insere na lista de cores do usuario com o uso da funcao TIMER da biblioteca
#Treading. Ao final do tempo inserido como parametro 'x', se o jogador nao iseriu a cor, ele perde a jogada
def geraCorUsr(x):
    def time_up():
        usercor = None
        print ('...o tempo acabou :( ...')

    t = Timer(x, time_up) #Configura timer de resposta com funcao a ser executada no termino
    t.start() #Inicia timer de resposta

    try:
        usercor = raw_input("\nDigite a cor: ")
    except Exception:
        pass
        usercor = None

    if usercor != True: #Verifica se a variavel usercor foi preenchida
        t.cancel() #Cancela o timer
        playerList.append(usercor.lower()) #Faz append da cor digitada na lista de cores do usuario


#Funcao para mostrar a sequencia de cores do jogo armazenada na lista gameList
def mostraLista():
    for cor in gameList:
        limpa()
        time.sleep(0.5)
        print (cor)
        time.sleep(1)
        limpa()


#Mostra elogio para caso de acerto
def mostraElogio():
    print elogio[randint(1,7)]  #Imprimime elogio baseado em uma escolha randomica no dicionario de elogios
    time.sleep(1)
    limpa()

#Grava Ranking
#Funcao recebe o nome do jogador e a pontuacao de rounds e faz append na lista de ranking
def gravaRanking(player, score):
    rankingList.append([player, score])

#Ordena Bolha
#Funcao que ordena o ranking no metodo bolha
def ordena_bolha(lista):
    if len(lista) > 1:
        for i in range(len(lista)): #Percorre lista
            for j in range(len(lista) - 1 - i): #Percorre lista excluindo a ultima posicao e posicao atual
                if lista[j][1] < lista[j+1][1]: #Compara o valor do ranking com a proxima posicao
                    lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Troca posicao
    return lista[0:5]


def jogo():

    while (True):

        limpa()

        print "///////////////////////////////////////////////////Genius Master////"
        print "                                        _                       ___ "
        print " _   ______ _____ ___  ____  _____     (_)___  ____ _____ _____/__ \\"
        print "| | / / __ `/ __ `__ \/ __ \/ ___/    / / __ \/ __ `/ __ `/ ___// _/"
        print "| |/ / /_/ / / / / / / /_/ (__  )    / / /_/ / /_/ / /_/ / /   /_/  "
        print "|___/\__,_/_/ /_/ /_/\____/____/  __/ /\____/\__, /\__,_/_/   (_)   "
        print "                                 /___/      /____/                  "

        vamos = raw_input("\n(s/n):")

        # Limpa a lista de cores do genius
        del gameList[:]

        #Inicializa a variavel de rounds e saida
        rounds = 0
        saida = 0

        if vamos.lower() == 'n':
            print "Ok! Tchau!"
            break

        if vamos.lower() == 's':

            jogador = raw_input("\nDigite seu nome:")

            while (True): #Inicia o ciclo de jogadas
                geraCor()
                mostraLista()

                for idx, val in enumerate(gameList): #Inicia captura de cores do usuario e compara com a lista de cores do jogo
                    geraCorUsr(9.0) #Chamada de funcao para inserir cor de jogador com 9 segundos para resposta
                    if gameList[idx] == playerList[idx]: #Compara posicao da lista de cores do jogador com a do jogo
                        mostraElogio()
                    else:
                        print "Perdeu!"
                        saida = 1
                        break
                if saida == 1:
                    break
                rounds = rounds + 1

            #Imprime lista do jogo e do jogador
            print "\nGenius: \n"
            print gameList
            print "\n\nJogador: \n"
            print playerList

            #Grava o resultado da partida
            gravaRanking(jogador, rounds)

            print "Seu score nesta partida: " + str(rounds)
            print "\n_______________________________"
            print "\nTOP 5:\n"

            #A Lista de ranking e ordenada e gravada em uma nova lista rankingOrderList

            #rankingOrderList = sorted(rankingList, key=lambda k: k[1], reverse=True) #Funcao de ordenacao em parametro lambda

            rankingOrderList = ordena_bolha(rankingList)

            #Imprime os 5 maiores resultados do ranking
            for x in rankingOrderList[0:5]:
                print x[0]+("." * (30 - len(x[0])))+str(x[1])


            raw_input()

jogo()
