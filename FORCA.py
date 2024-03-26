def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca Ana!***")
    print("*********************************")
    
    palavra_secreta = "Beatriz".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    letras_acertadas = []
    
    for letra in (palavra_secreta):
        letras_acertadas2.append("_")
        
        enforcou = False
        acertou = False
        erros =0
        
        print(letras_acertadas)
        
        while (not enforcou and not acertou):
            
           chute = input("Qual letra? ") 
           chute = chute.strip().upper()
          
          if (chute in palavra_secreta):
              index = 0
              for letra in palavra_secreta:
                  if (chute == letra):
                     letras_acertadas[index] = letra
                     index +=1
                     else:
                         erros +=1
                         
                         enforcou = erros == 6
                         acertou = "_" not in letras_acertadas
