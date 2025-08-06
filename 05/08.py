lista_idades = []
lista_sexo = []

for i in range(2):
    nome = input("digite seu nome:")
    lista_nomes.append(nome)
    
    idade = int(input("digite sua idade:"))
    lista_idades.append(idade)
    
    sexo = input("digite M para maculino e F para feminino:")
    lista_sexo.append(sexo)
    
    print(lista_nomes)
    print(lista_idades)
    print(lista_sexo)
    

#meu ex
lista_nomes = []
lista_idades = []
lista_sexo = []

for i in range(2):
    nome = input("digite seu nome:")
    lista_nomes.append(nome)
    
    idade = int(input("digite sua idade:"))
    lista_idades.append(idade)
    
    sexo = input("digite M para maculino e F para feminino:")
    lista_sexo.append(sexo)
    
    print(lista_nomes)
    print(lista_idades)
    print(lista_sexo)
    
    lista_todas = lista_nomes + lista_idades + lista_sexo
    print(lista_todas)
    

#ex2

dados = [[], [], []]
i = 0

while i < 2:
    nome = input("digite deu nome:")
    dados[0].append(nome)
    
idade = int(input("digite sua idade:"))
dados[1].append(idade)
   
sexo = input("digite M para maculino e F para feminino:")
dados[2].append(sexo)
i += 1
    
print(dados)
   
   

#ex3

dados = [[], [], []]
i = 0

while i < 2:
    nome = input("digite seu nome")
    idade =  int(input("digite seua idde:"))
    sexo = input("digite M para masculino e F pr feminino:")
    
    dados.append([nome, idade, sexo])
    i += 1 
    
print(dados) 

# exemplos com listas

lista = [4, 5, 6]
print(lista)

# estrutura com tuplas 

#tupla = 4, 5, 6
#print(tupla)

#1
tupla = (4, 5, 6)
print(tupla)

#----------------------------------------------------

#2
tupla_tupla = (4, 5, 6), (7, 8, 9)
print(tupla_tupla)

#----------------------------------------------------

#3
tupla_tupla = (4, 5, 6), (7, 8, 9)
print(tupla_tupla[0][0])

#-----------------------------------------------------

#4
tupla_caracteres = tupla('string')
print(tupla_caracteres)

#----------------------------------------------------

#5
tupla1 = tuple(['fiap',[1, 2], True])
print(tupla1)

tupla1[2] = False

#----------------------------------------------------

#6
tupla1 = tuple(['fiap',[1, 2], True])
tupla1[1].append(2)
tupla1[1].append(100)

print(tupla1)

#----------------------------------------------------

#7
tupla2 = tuple(['fiap', [1, 2], True])
lista_nova = list(tupla2)

lista_nova.insert(0, 'engenharia de software')

nova_tupla = tuple(lista_nova)

#----------------------------------------------------

#8
tupla3 = tuple(['fip', [1, 2], True])
lista_nova3 = list(tupla3)

posicao_insercao = lista_nova3.index('fiap') + 1

lista_nova3(posicao_insercao, 'hoje')

nova_tupla = tuple(lista_nova3)
print(nova_tupla)

#----------------------------------------------------

#9
(4, None, 'foo fighters') + (6, 0) + ('bar', 1)

(4, 'foo fighters') * 3

#----------------------------------------------------

tupla = (4, 8, 12, 20)

for numero in tupla:
    novo_numero = numero * 2
    print(novo_numero) 