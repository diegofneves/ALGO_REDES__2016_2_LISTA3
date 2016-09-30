numeros = []
par = []
impar = []

for i in range (20):
    numero = int(input('Digite um numero inteiro: '))
    numeros.append(numero)

    if numero % 2 == 0:
        par.append(numero)
    else:
        impar.append(numero)

print('Numeros pares: ', par)
print('Numeros impares: ', impar)
print('Todos os numeros digitados: ', numeros)
