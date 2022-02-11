def partida():
 f=1   
 while f!=0:
  n=int(input("Quantas peças? "))
  m=int(input("Limite de peças por jogada? "))
  if n>m:
   f=0       
   if n%(m+1)==0:
     print("Você começa!\n")
     l=1
   else:
     print("O computador começa!\n")
     l=0
   while l!=2: 
     while l ==1:
      l=0
      jp = usuario_escolhe_jogada(n,m)
      n-= jp
      print("Você tirou ",jp," peças.")
      print("Agora restam ",n," peças no tabuleiro.\n")
      if n==0:
        print("Fim do jogo! O Jogador ganhou!")
        l=2
     while l ==0:
      l=1
      jp = computador_escolhe_jogada(n,m)
      n-= jp
      print("o Computador tirou ",jp," peças.")
      print("Agora restam ",n," peças no tabuleiro.\n")
      if n==0:
        print("Fim do jogo! O computador ganhou!")
        l=2
  else:
   print("Estes numeros não são validos. ")   
 ()

def usuario_escolhe_jogada(n,m):
 f=1
 while f!=0:
  jp = int(input("Quantas peças você vai tirar? "))   
  if jp<= m and jp>0 :
   f=0
   return jp
  else:
   print("Oops! Jogada inválida! Tente de novo.") 
 ()  


def computador_escolhe_jogada(n,m): 
 n1=n
 m1=m
 while m1!=0:
  r= n1-m1  
  if r%(m+1)==0:
   jp= m1
   return jp
  else:
   m1-=1 
   if m1==0:
    if m>n:
     jp= m-(m-n)
     return jp 
    else: 
     jp=m
 return(jp)
 ()

i= int(input("Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada  \n2 - para jogar um campeonato\n\n"))
if i==1:
 print("Voce escolheu uma partida!\n")
 partida()
if i==2:
 print("2 - para jogar um campeonato 2")
 print("**** Rodada 1 ****")
 partida()
 brand = 1
 print("**** Rodada 2 ****")
 partida()
 brand+=1
 print("**** Rodada 3 ****")
 partida()
 brand+=1
 print("*** Final do campeonato! ****\n")
 print("Placar: Você 0 X 3 Computador")
 


    

    
      
      
      
      

      
     
         




        
     
       
