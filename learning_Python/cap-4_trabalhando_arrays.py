# Trabalhando com o for
nomes = ['eduardo', 'ana', 'helena', 'dete']
for nome in nomes:
    print(nome.title() + ", que nome bonito")

# Trabalhando com range
for value in range(1,5):
    print(value)

numbers = list(range(1,10))
print(numbers)

squares = []
for value in range(1,11):
    square = value * 2
    squares.append(square)

print(squares)