import numpy as np

def colocar_peca(tabuleiro, linha, coluna, peca):
    """Coloca a peça do jogador na posição escolhida 🎯"""
    tabuleiro[linha][coluna] = peca

def verifica_vitoria(tabuleiro, peca):
    """ Verifica se o jogador venceu o jogo 🏆"""
    linhas = np.any(np.all(tabuleiro == peca, axis=1))
    colunas = np.any(np.all(tabuleiro == peca, axis=0))
    diagonais = (
        np.all(np.diag(tabuleiro) == peca) or
        np.all(np.diag(np.fliplr(tabuleiro)) == peca)
    )
    return linhas or colunas or diagonais

def imprimir_tabuleiro(tabuleiro):
    """Imprime o tabuleiro de forma organizada 📋"""
    print("\n🧩 Tabuleiro Atual:\n")
    simbolos = {
        0: " ",
        1: "X",
        2: "O"
    }
    for linha in tabuleiro:
        print(" | ".join(simbolos[x] for x in linha))
        print("-" * 9)

def jogo():
    """🎮 Função principal do Jogo da Velha"""
    tabuleiro = np.zeros((3, 3), dtype=int)

    peca_atual = 1
    vencedor = False
    empate = False

    print("\n🎲 Bem-vindo ao Jogo da Velha!\n")
    print("👉 Jogador 1 = X | Jogador 2 = O\n")

    while not vencedor and not empate:
        imprimir_tabuleiro(tabuleiro)

        while True:
            try:
                print(f"\n🕹️\t Jogador {peca_atual}, é a sua vez!")
                linha = int(input("➡ Escolha a linha (0, 1, 2): "))
                coluna = int(input("➡ Escolha a coluna (0, 1, 2): "))

                # Validação de limites
                if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
                    print("\n⚠️ Escolha linhas e colunas válidas (0 a 2)!\n")
                    continue

                # Verifica se posição está ocupada
                if tabuleiro[linha][coluna] != 0:
                    print("\n⛔ Posição ocupada! Escolha outra.\n")
                    continue

                colocar_peca(tabuleiro, linha, coluna, peca_atual)
                vencedor = verifica_vitoria(tabuleiro, peca_atual)

                if np.all(tabuleiro != 0) and not vencedor:
                    empate = True

                break

            except ValueError:
                print("\n❌ Entrada inválida! Digite apenas números de 0 a 2.\n")

        # Troca de jogador
        if not vencedor and not empate:
            peca_atual = 2 if peca_atual == 1 else 1

    imprimir_tabuleiro(tabuleiro)

    if vencedor:
        print(f"\n🎉🏆 Parabéns! Jogador {peca_atual} venceu o jogo!")
    else:
        print("\n🤝😄 Empate! O jogo terminou sem vencedor.")

jogo()
