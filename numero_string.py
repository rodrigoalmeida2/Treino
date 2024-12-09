# Dicionário para mapear palavras para números
palavras_para_numeros = {
    "zero": 0,
    "um": 1,
    "dois": 2,
    "três": 3,
    "quatro": 4,
    "cinco": 5,
    "seis": 6,
    "sete": 7,
    "oito": 8,
    "nove": 9,
    "dez": 10,
    "onze": 11,
    "doze": 12,
    "treze": 13,
    "catorze": 14,
    "quinze": 15,
    "dezesseis": 16,
    "dezessete": 17,
    "dezoito": 18,
    "dezenove": 19,
    "vinte": 20
}

# Solicita ao usuário uma palavra que representa um número
palavra = input("Digite uma palavra que represente um número (ex: 'dois', 'dez'): ").lower()

# Converte a palavra para um número inteiro
numero = palavras_para_numeros.get(palavra)
if numero is not None:
    print(f"O número convertido é: {numero}")
else:
    print("Erro: A palavra digitada não está no vocabulário suportado.")
