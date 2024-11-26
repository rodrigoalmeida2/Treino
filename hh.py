import spacy

def analisar_frase(frase):
    # Carregar o modelo de linguagem do spaCy
    nlp = spacy.load("pt_core_news_sm")  # Modelo para português
    doc = nlp(frase)

    # Dicionário para organizar os elementos
    elementos = {
        "Sujeito": [],
        "Verbos": [],
        "Objetos": [],
        "Artigos": [],
        "Outros": []
    }

    # Percorrer os tokens na frase
    for token in doc:
        if token.dep_ == "nsubj":  # Sujeito
            elementos["Sujeito"].append(token.text)
        elif token.pos_ == "VERB":  # Verbos
            elementos["Verbos"].append(token.text)
        elif token.dep_ in ["dobj", "obj"]:  # Objetos diretos/indiretos
            elementos["Objetos"].append(token.text)
        elif token.pos_ == "DET":  # Artigos
            elementos["Artigos"].append(token.text)
        else:  # Outros elementos
            elementos["Outros"].append(token.text)

    # Imprimir os resultados
    for categoria, palavras in elementos.items():
        print(f"{categoria}: {', '.join(palavras) if palavras else 'Nenhum'}")

# Teste
frase = "O cachorro comeu a comida do gato."
analisar_frase(frase)
