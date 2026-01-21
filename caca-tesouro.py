import numpy as np

# Mapa 5x5
mapa = np.random.randint(1, 10, size=(5, 5))

# Posiciona o tesouro em uma posição aleatória diferente da inicial
while True:
    tesouro_linha, tesouro_coluna = np.random.randint(0, 5, size=2)
    if (tesouro_linha, tesouro_coluna) != (0, 0):
        break

posicao_jogador = (0, 0)
pontuacao = 0

def mostrar_mapa(mapa, posicao_jogador):
    mapa_com_jogador = mapa.copy()
    l, c = posicao_jogador
    mapa_com_jogador[l, c] = -1  # jogador

    print("\nMapa Atual:")
    for linha in mapa_com_jogador:
        print(" ".join(" P" if v == -1 else f"{v:2d}" for v in linha))

# Loop principal
while True:
    mostrar_mapa(mapa, posicao_jogador)
    print("🧭 Mova-se: cima (c), baixo (b), esquerda (e), direita (d)")
    print("📍 Posição atual:", posicao_jogador)
    print("🎯 Pontuação:", pontuacao)

    direcao = input(
        "👉 Para onde deseja ir? (cima/baixo/esquerda/direita ou c/b/e/d): "
    ).strip().lower()

    movimentos = {
        "cima": (-1, 0), "c": (-1, 0),
        "baixo": (1, 0), "b": (1, 0),
        "esquerda": (0, -1), "e": (0, -1),
        "direita": (0, 1), "d": (0, 1)
    }

    if direcao not in movimentos:
        print("Direção inválida! Tente novamente.")
        continue

    nova_posicao = (
        posicao_jogador[0] + movimentos[direcao][0],
        posicao_jogador[1] + movimentos[direcao][1]
    )

    if not (0 <= nova_posicao[0] < mapa.shape[0] and
            0 <= nova_posicao[1] < mapa.shape[1]):
        print("Movimento fora dos limites!")
        continue

    posicao_jogador = nova_posicao
    pontuacao += 1

    if posicao_jogador == (tesouro_linha, tesouro_coluna):
        mostrar_mapa(mapa, posicao_jogador)
        print("\n🎉 Parabéns! Você encontrou o tesouro!")
        print(f"Pontuação final: {pontuacao}")
        print(f"Tesouro estava em: {(tesouro_linha, tesouro_coluna)}")
        break
