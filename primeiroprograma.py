print("Olá")
nome = input("Informe o seu nome: ")
idade = input("Informe a sua idade: ")

print(f"Bem vindo(a), {nome}. Você já tem {idade} anos, parabéns!", end="...\n")
print(nome, idade, sep="#")


nome = "Anna"
idade = 26
profissao = "estudante"
linguagem = "Python"

print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculada no curso de %s." %(nome, idade, profissao, linguagem))
