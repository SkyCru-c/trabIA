def obter_resposta(pergunta, opcoes):
    print(pergunta)
    for numero, opcao in enumerate(opcoes, start=1):
        print(f"({numero}) {opcao}")
    resposta = int(input("Escolha uma opção: "))
    return resposta

def encontrar_combinacao(respostas):
    combinacoes = {
        (1, 1, 1, 1, 1): ("Pizza", "Vinho tinto", "Restaurante italiano"),
        (1, 1, 1, 1, 2): ("Pizza", "Vinho tinto", "Restaurante italiano"),
        (1, 1, 1, 1, 3): ("Pizza", "Vinho tinto", "Restaurante italiano"),
        (1, 1, 1, 2, 1): ("Pizza", "Cerveja", "Restaurante italiano"),
        (1, 1, 1, 2, 2): ("Pizza", "Cerveja", "Restaurante italiano"),
        (1, 1, 1, 2, 3): ("Pizza", "Cerveja", "Restaurante italiano"),
        (1, 1, 1, 3, 1): ("Pizza", "Coquetéis", "Restaurante italiano"),
        (1, 1, 1, 3, 2): ("Pizza", "Coquetéis", "Restaurante italiano"),
        (1, 1, 1, 3, 3): ("Pizza", "Coquetéis", "Restaurante italiano"),
        (1, 1, 2, 1, 1): ("Sushi", "Sake", "Restaurante japonês"),
        (1, 1, 2, 1, 2): ("Sushi", "Sake", "Restaurante japonês"),
        (1, 1, 2, 1, 3): ("Sushi", "Sake", "Restaurante japonês"),
        (1, 1, 2, 2, 1): ("Sushi", "Cerveja", "Restaurante japonês"),
        (1, 1, 2, 2, 2): ("Sushi", "Cerveja", "Restaurante japonês"),
        (1, 1, 2, 2, 3): ("Sushi", "Cerveja", "Restaurante japonês"),
        (1, 1, 2, 3, 1): ("Sushi", "Coquetéis", "Restaurante japonês"),
        (1, 1, 2, 3, 2): ("Sushi", "Coquetéis", "Restaurante japonês"),
        (1, 1, 2, 3, 3): ("Sushi", "Coquetéis", "Restaurante japonês"),
        (1, 1, 3, 1, 1): ("Churrasco", "Caipirinha", "Churrascaria"),
        (1, 1, 3, 1, 2): ("Churrasco", "Caipirinha", "Churrascaria"),
        (1, 1, 3, 1, 3): ("Churrasco", "Caipirinha", "Churrascaria"),
        (1, 1, 3, 2, 1): ("Churrasco", "Cerveja", "Churrascaria"),
        (1, 1, 3, 2, 2): ("Churrasco", "Cerveja", "Churrascaria"),
        (1, 1, 3, 2, 3): ("Churrasco", "Cerveja", "Churrascaria"),
        (1, 1, 3, 3, 1): ("Churrasco", "Coquetéis", "Churrascaria"),
        (1, 1, 3, 3, 2): ("Churrasco", "Coquetéis", "Churrascaria"),
        (1, 1, 3, 3, 3): ("Churrasco", "Coquetéis", "Churrascaria"),
        (2, 2, 2, 2, 2): ("Sushi", "Cerveja", "Restaurante Japonês"),
        (1, 2, 2, 2, 2): ("Sushi", "Cerveja", "Restaurante Japonês"),
        
        
    }
    return combinacoes.get(tuple(respostas[:5]), ("Comida variada", "Bebida mista", "Local genérico"))

def main():
    perguntas = [
        ("Qual é o seu nível de fome?", ["Estou morrendo de fome!", "Estou com um pouco de fome.", "Estou com pouca fome."]),
        ("Qual é o seu tipo de comida preferido?", ["Italiana", "Japonesa", "Brasileira"]),
        ("Qual é o seu tipo de bebida preferido?", ["Vinho", "Cerveja", "Coquetéis"]),
        ("Qual é a ocasião do encontro?", ["Jantar romântico", "Encontro casual", "Comemoração"]),
        ("Qual é o seu orçamento?", ["Até R$ 100", "Até R$ 200", "Acima de R$ 200"]),
        ("Você tem alguma restrição alimentar?", ["Sim", "Não"]),
        ("Se sim, quais são suas restrições alimentares?", ["Alergias", "Intolerâncias", "Preferências"]),
        ("Você prefere um ambiente formal ou informal?", ["Formal", "Informal"]),
        ("Qual é a sua faixa etária?", ["18-25", "26-35", "36-45"]),
        ("Você prefere um prato principal ou petiscos?", ["Prato principal", "Petiscos"]),
        ("Qual é o seu nível de tolerância ao álcool?", ["Baixo", "Médio", "Alto"]),
        ("Você prefere uma bebida doce ou seca?", ["Doce", "Seca"]),
        ("Qual é a sua estação preferida do ano?", ["Primavera", "Verão", "Outono"]),
        ("Você prefere um local ao ar livre ou fechado?", ["Ao ar livre", "Fechado"]),
        ("Qual é a sua música preferida?", ["Música clássica", "Pop", "Rock"]),
    ]

    respostas = []
    for pergunta, opcoes in perguntas:
        respostas.append(obter_resposta(pergunta, opcoes))

    comida, bebida, local = encontrar_combinacao(respostas)
    print(f"\nCom base nas suas respostas, a melhor combinação de comida e bebida para o seu encontro é:")
    print(f"Comida: {comida}")
    print(f"Bebida: {bebida}")
    print(f"Local: {local}")

if __name__ == "__main__":
    main()