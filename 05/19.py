# função encadeadas

#ex1
def func1 (n):
    return func2 (n * 2)
def func2 (n):
    return func3 (n + 10)
def func3 (n):
    return n // 2 
print(func1(4))

#-------------------------------------------------------------------------------

#ex2 
def func1(P):
    return func2(P + 'e python')
def func2(P):
    return func3(P.upper())
def func3(P):
    return P[::-1]
 
 #os dois :: serve para enverter

#-------------------------------------------------------------------------------

#ex3 encadeamento em lista
def adicionr(lista):
    return dobrar(lista + [10])
def dobrar(lista):
    return inverter([x * 2 for x in lista])
def inverter(lista):
    return lista[::-1]

#-------------------------------------------------------------------------------

#ex4 
dicionrio_alunos = {
    "nome": ["ana", 'laura'];
    "idade": [21, 35]; # type: ignore
    "curso": ["engenharia de sotware", 'ciencia da computacao'], # type: ignore
}

print(dicionario_alunos) # type: ignore

import pandas as pd 

dados = pd.DataFrame(dicionario_alunos) # type: ignore


####