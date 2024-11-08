# Entrada da idade do nadador
idade = int(input("Digite a idade do nadador: "))

# Classificação por categoria
if 5 <= idade <= 7:
    categoria = "Infantil A"
elif 8 <= idade <= 10:
    categoria = "Infantil B"
elif 11 <= idade <= 13:
    categoria = "Juvenil A"
elif 14 <= idade <= 17:
    categoria = "Juvenil B"
elif idade >= 18:
    categoria = "Adulto"
else:
    categoria = "Idade fora das categorias classificáveis"

# Exibindo a categoria
print(f"A categoria do nadador é: {categoria}")
