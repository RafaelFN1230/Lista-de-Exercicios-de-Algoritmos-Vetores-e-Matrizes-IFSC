'''
Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos
lados de um triângulo, e se forem, verificar se é um triângulo equilátero, isóscele
ou escaleno. Se eles não formarem um triângulo, escrever uma mensagem.
Antes da elaboração do algoritmo, torna-se necessário a revisão de algumas
propriedades e definições.
Propriedade – o comprimento de cada lado de um triângulo é menor do que a
soma dos comprimentos dos outros dois lados.
Definição 1 - chama-se de triângulo equilátero o que tem os comprimentos dos
três lados iguais;
Definição 2 - chama-se de triângulo isóscele o triângulo que tem os
comprimentos de dois lados iguais;
Definição 3 - chama-se triângulo escaleno o triângulo que tem os
comprimentos dos três lados diferentes.
'''

x=float(input("Insira o valor de X: "))
y=float(input("Insira o valor de Y: "))
z=float(input("Insira o valor de z: "))

if (x<y+z and y<x+z and z<x+y):
    if (x==y and y==z):
        print("Estes comprimentos formam um triangulo equilátero.")
    elif (x==y or y==z):
        print("Estes comprimentos formam um triangulo isócele.")
    elif (x!=y and y!=z):
         print("Estes comprimentos formam um triangulo escaleno.")
else:
    print("Estes comprimentos não formam um triangulo.")