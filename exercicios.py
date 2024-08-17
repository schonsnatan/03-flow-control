print("\nAULA 03\n")

x = 2

if x < 0:
    x = 0
    print("Negative change")
elif x == 0:
    print("Zero")
elif x == 1:
    print("Single")
else:
    print("More")

print('\nExercise 1:\n')
price = float(input("Type the sales price: "))
quantity = int(input("Type the quantity: "))

if price < 0 or quantity < 0:
    print("Invalid data. Provide positive numbers.")
else:
    print("Valid data.")

print('\nExercise 2:\n')

temperature = float(input("Temperature: "))
if temperature < 18:
    print("Low")
elif temperature >=18 and temperature <= 26:
    print("Normal")
else:
    print("High")

print('\nExercise 3:\n')

log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

if log['level']=='ERROR':
    print(log['message'])

print('\nExercise 4:\n')
age = int(input("Type your age: "))
email = input("Provide an email: ")

if age >=18 and age <=65 and email.__contains__('@'):
    print("Data is valid.")
elif age < 18:
    print("You are underage.")
elif age > 65:
    print("You are too old")
elif '@' not in email:
    print("Provide a valid email")

print('\nExercise 5:\n')

transacao = {'valor': 12000, 'hora': 10}

if transacao['valor'] > 10000 or transacao['hora'] > 18 or transacao['hora'] < 9:
    print("Suspect transaction")
else:
    print("Transaction ok")


print('\nExercise 6:\n')

texto = 'o Natan é um cara muito divertido e o Natan é um cara diferenciado'
texto_split = texto.split()
repet = {}
for i in texto_split:
    if i in repet:
        repet[i] += 1
    else:
        repet[i] = 1

print(repet)

print('\nExercise 7:\n')

numeros = [10, 20, 30, 40, 50]

minimo = min(numeros)
maximo = max(numeros)
normalized = [(x - minimo) / (maximo - minimo) for x in numeros]
print(normalized)

print('\nExercise 8:\n')
usuarios = [
    {"nome": "Alice", "email": "alice@example.com"},
    {"nome": "Bob", "email": ""},
    {"nome": "Carol", "email": "carol@example.com"}
]

invalid_users = []

for i in usuarios:
    if not all(i.values()):
        invalid_users.append(i)

print(invalid_users)

print('\nExercise 9:\n')

numeros = range(1, 11)
pares = []

for i in numeros:
    if i%2==0:
        pares.append(i)
print(pares)

print('\nExercise 10:\n')

vendas = [
    {"categoria": "eletrônicos", "valor": 1200},
    {"categoria": "livros", "valor": 200},
    {"categoria": "eletrônicos", "valor": 800}
]
total_per_category = {}

for i in vendas:
    categoria = i['categoria']
    valor = i['valor']
    if categoria in total_per_category:
        total_per_category[categoria] += valor
    else:
        total_per_category[categoria] = valor

print(total_per_category)

print('\nExercise 11:\n')

word = 'test'

while word != 'sair':
    word = input("word: ")

print('\nExercise 12:\n')

numero = int(input("Digite um número entre 1 e 10: "))

while numero < 1 or numero > 10: 
    numero = int(input("Digite um número entre 1 e 10: "))

print('\nExercise 13:\n')

pagina_atual = 1
paginas_totais = 5

while pagina_atual < paginas_totais:
    print("Cosuming API!")
    pagina_atual+=1
print('\nExercise 14:\n')

tentativas_maximas = 5
tentativa = 1

while tentativa < tentativas_maximas:
    print(f"Trying to connect: try {tentativa} of {tentativas_maximas}")
    tentativa+=1
print("Failed to connect.")
'''
print('\nExercise 15:\n')

itens = [1, 2, 3, "parar", 4, 5]

for i in itens:
    if i == 'parar':
        print("Saindo...")
        break
    else:
        print(i)
