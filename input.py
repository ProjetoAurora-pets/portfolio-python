#input é uma funcão que permite a interacão entre o programa e o usuario

#exemplo:

nome = input("por favor escreva seu nome")

#o input pedira para o usuario colocar o seu nome

#o input pode ser utilizado junto de diversas outras funcões de python como:

data = int(input("ensira uma hora de 0 a 23"))
if data < 12:
    print("manha")
elif data >= 12:
    print("tarde")
elif data >= 18:
    print("noite")
else data = 0:
    print("meia-noite")

#o programa pedira para usuario informar uma data e dependendo da horario ele ira mostrar uma mensagem diferente
                
