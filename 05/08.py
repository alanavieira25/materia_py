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