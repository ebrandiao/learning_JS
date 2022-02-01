# Acessando elementos da lista
bike = ['caloi', 'monark', 'peugeot']
print(bike[0])

# Usando valores individuais de uma lista
message = "Minha bicicleta favorita é", bike[1].title() + "."
print(message)

# Modificando elementos de uma lista
print(bike)
bike[1] = 'chevrolet'
print(bike)

# Inserindo elementos em uma lista
bike.insert(2, "fiat")
print(bike)

# Removendo elementos de uma lista
del bike[1]
print(bike)

# Ordanando uma lista
print(sorted(bike))

# Exibindo uma lista na ordem inversa
bike.reverse()
print(bike)