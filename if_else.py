# Exemplo de codigo simples que usa if e else
x= 10 
if x >= 10: 
    print("numero certo") 
else: 
    print("numero errado")


#Exemplo de codigo de if e else utilizando o input
num = int(input("Digite um numero de 0 a 100: ")) 
if num <= 50: 
    print("Você digitou um numero baixo") 
else: 
    print("Você digitou um numero alto")


#Exemplo de codigo utilizando if, elif e else
num = int(input("Qual é a temperatura atual? ")) 
if num <= 19: 
    print("Esta muito frio!") 
elif num <= 29: 
    print("Esta uma temperatura agradavel") 
else: print("Esta muito calor")


#Codigo utilizando mais que uma variavel e mais que um elif
nota1 = float(input("Digite a primeira nota")) 
nota2 = float(input("Digite a segunda nota")) 
media = (nota1 + nota2)/2 
if media <= 2: 
    print("Você esta reprovado") 
elif media <= 4: 
    print("Você esta na final") 
elif media <= 6: 
    print("Você tem direito a fazer uma prova para substituir a media") 
else: 
    print("Você esta aprovado")
