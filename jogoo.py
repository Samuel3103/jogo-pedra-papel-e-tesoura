#Esse é um jogo pedra, papel e tisora
import random

print("jogo Pedra, Papel e Tesoura")

JOGO = int(input("escrava numero 1 para pedra, 2 para papel e 3 para tesoura    "))

BotEscolha= random.randint(1 , 3)

if JOGO == 1 and BotEscolha== 1 : 
 print("empate")
 print("jogador pedra bot pedra")

elif JOGO== 2 and BotEscolha== 1:
 print("Vitória")
 print("jogador papel bot pedra")

elif JOGO== 3 and BotEscolha== 1:
 print("Perdeu")
 print("jogador tesoura bot pedra")

if JOGO == 1 and BotEscolha== 2:
 print("Bot Venceu")
 print("jogador pedra bot papel")

elif JOGO == 2 and BotEscolha== 2:
 print("Empate")
 print("jogador papel bot papel")

elif JOGO ==3 and BotEscolha== 2:
 print("Jogador venceu")
 print("jogador tesoura bot papel")

if JOGO == 1 and BotEscolha== 3:
 print("Jogador Venceu")
 print("jogador pedra bot tesoura")

elif JOGO == 2 and BotEscolha == 3:
 print("Bot Venceu")
 print("jogador papel bot tesoura")

elif JOGO == 3 and BotEscolha == 3:
 print("Empate")
 print("jogador tesoura bot tesoura")

else: print("Não foi possivel executar a operação")