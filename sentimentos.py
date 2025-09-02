# NLP Básico com Python
# Autor: Nayane
# Objetivo: Mostrar como analisar sentimentos de textos de forma simples

# Passo 1: Instalar e importar bibliotecas
# pip install textblob

from textblob import TextBlob

# Passo 2: Criar textos para análise
textos = [
    "Eu estou muito feliz hoje!",
    "Que dia horrível, estou triste...",
    "Não sei o que pensar sobre isso."
]

# Passo 3: Analisar sentimentos
for texto in textos:
    blob = TextBlob(texto)
    sentimento = blob.sentiment.polarity  # -1 (negativo) a 1 (positivo)
    
    # Passo 4: Interpretar o sentimento
    if sentimento > 0:
        status = "Positivo 😄"
    elif sentimento < 0:
        status = "Negativo 😢"
    else:
        status = "Neutro 😐"
    
    print(f"Texto: {texto}")
    print(f"Sentimento: {sentimento:.2f} → {status}")
    print("-" * 40)
