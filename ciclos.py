#FOR
for i in range(5):
    print(i)
    
for i in range(10):
    if i==5:
        break
    print(i)
    
cidades = ["Lisboa", "Porto", "Algarve", "Évora"]
for city in cidades:
    print(city)

mensagem = "Olá malta!"
for char in mensagem:
    print(char)
    
lanche = ("hamburguer", "sumo", "pizza", "pudim")
for c in lanche:
    print(f'Eu vou comer {c}')
print("Comi para caramba")

#WHILE
i=0
while i<=10:
    print("Não paro nunca")
    
i=0
while i<=10:
    print("Não paro nunca")
    i+=1
    
i=0
while i<=10:
    print("Não paro nunca")
    break

#IF
numeros = [1,3,6,10,5,23]
numero_digitado=int(input("Digite um número: "))
if numero_digitado in numeros:
    print(f"O número {numero_digitado} está na lista")
else:
    print(f"O número {numero_digitado} não está na lista")
    
