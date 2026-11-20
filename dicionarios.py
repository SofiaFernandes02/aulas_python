#1
pessoa = {
    "nome":"António",
    "idade":"51",
    "cidade":"Lisboa",
    "função":"enfermeiro"}

#2
print(pessoa["nome"],pessoa["idade"])

#3
pessoa["idade"] = "41"
print(pessoa)

#4
pessoa["email"] = "antonio@kmail.com"
pessoa["telefone"] = "912732634"

#5
pessoa.pop("telefone")
print(pessoa)

#6
amigo = str(input("Insira o nome do amigo "))
if amigo in pessoa.values():
    print("Existe")
else:
    print("Não existe")