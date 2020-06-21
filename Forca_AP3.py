from random import choice
import random, string
#Dicas: [Palavras]
palavras = ['saude', 'pandemia', 'virus', 'contagio', 'prevenção']
palavras = choice(palavras)

print('''====================================
       JOGO DA FORCA 2020
====================================''')
print("\n")

print('''====================================
    Pronto para Começar...?
====================================''')
print("\n")

  
  
  def forca(x=0):
  if x==0:
    print("------------")
    print("|          |")
    print("|          ") 
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==1:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==2:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==3:
    print("------------")
    print("|          |")
    print("|          0")
    print("|         -|")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==4:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|               ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==5:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         /      ")
    print("|               ")
    print("|               ")
    print("|")

  elif x==6:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         / \   ")
    print("|               ")
    print("|    Lamento! Perdeu! ")
    print("|")

erros=0

#CAPTURA PALAVRA INICIAL
inicio= int(input("Digite 1 para iniciar a partida: "
nome = input("Nome do Jogador(a):")
word=input('Informe a palavra: ');
temp=[]
for letra in word:
  temp.append('_')

while True:
  print('\n'*20) # limpa a tela
  forca(erros) # imprime desenho da forca

  #imprime a adivinhacao
  print('\n\nAdivinhe: ', end='')

  for let in temp:
    print(let, end=' ')
  print('\n'*2)

  #Verifica se perdeu
  if erros==6:
    break #sai do jogo (sai do while)

  #Verificar se o jogador ganhou
  ganhouJogo=True
  for let in temp:
    if let=='_':
      ganhouJogo=False
  if ganhouJogo:
    print('\nPARABÉNS VENCEDOR!!!')
    break
                  from random import choice
import random, string
#Dicas: [Palavras]
palavras = ['saude', 'pandemia', 'virus', 'contagio', 'prevenção']
palavras = choice(palavras)

print('''====================================
       JOGO DA FORCA 2020
====================================''')
print("\n")

print('''====================================
    Pronto para Começar...?
====================================''')
print("\n")

def forca(x=0):
  if x==0:
    print("------------")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==1:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==2:
    print("------------")
    print("|          |")
    print("|          0")
    print("|          |")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==3:
    print("------------")
    print("|          |")
    print("|          0")
    print("|         -|")
    print("|          ")
    print("|          ")
    print("|          ")
    print("|")
  elif x==4:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|               ")
    print("|               ")
    print("|               ")
    print("|")
  elif x==5:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         /      ")
    print("|               ")
    print("|               ")
    print("|")

  elif x==6:
    print("------------    ")
    print("|          |    ")
    print("|          0    ")
    print("|         -|-   ")
    print("|         / \   ")
    print("|               ")
    print("|               ")
    print("|               ")
    
erros=0

#CAPTURA PALAVRA INICIAL
inicio= int(input("Digite 1 para iniciar a partida: "
nome=input('Informe o Nome do Jogador:')
word=input('Informe a palavra:');
temp=[]
for letra in word:
  temp.append('_')

while True:
  print('\n'*20) # limpa a tela
  forca(erros) # imprime desenho da forca

  #imprime o chute
  print('\n\nLetra: ', end='')

  for let in temp:
    print(let, end=' ')
  print('\n'*2)

  #Verifica se perdeu
  if erros==6:
    break #sai do jogo (sai do while)

  #Verificar se o jogador ganhou
  ganhouJogo=True
  for let in temp:
    if let=='_':
      ganhouJogo=False
  if ganhouJogo:
    print('\nPARABÉNS VENCEDOR!!!')
    break

  while True:
        resp = str(input('Deseja continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('Responda apenas S ou N.')
    if resp == 'N':
            break
   
  #captura a letra do usuario
  letraDig=input("Informe uma letra: ")

  #verifica se acertou alguma letra
  errouLetra=True
  for i, let in enumerate(word):
    if word[i]==letraDig:
      temp[i]=word[i]
      errouLetra=False
  if errouLetra:
    erros=erros+1
    






  #captura a letra do usuario
  letraDig=input("Informe uma letra: ")

  #verifica se acertou alguma letra
  errouLetra=True
  for i, let in enumerate(word):
    if word[i]==letraDig:
      temp[i]=word[i]
      errouLetra=False
  if errouLetra:
    erros=erros+1
