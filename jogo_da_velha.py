# -----------------------------
# JOGO DA VELHA EM PYTHON
# Projeto de Extensão
# -----------------------------

def mostrar_tabuleiro(tabuleiro):
    """Exibe o tabuleiro atual na tela."""
    print("\n")
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print("\n")


def verificar_vitoria(tabuleiro):
    """Verifica se existe uma combinação vencedora."""
    combinacoes = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Linhas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colunas
        (0, 4, 8), (2, 4, 6)              # Diagonais
    ]

    for a, b, c in combinacoes:
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] and tabuleiro[a] != " ":
            return True
    return False


def jogo_da_velha():
    """Executa o jogo da velha completo."""
    tabuleiro = [" "] * 9
    jogador = "X"

    for rodada in range(9):
        mostrar_tabuleiro(tabuleiro)

        try:
            posicao = int(input(f"Jogador {jogador}, escolha uma posição (1-9): ")) - 1
        except ValueError:
            print("Entrada inválida! Digite um número de 1 a 9.")
            continue

        if posicao < 0 or posicao > 8:
            print("Posição fora do intervalo! Tente novamente.")
            continue

        if tabuleiro[posicao] != " ":
            print("Posição ocupada! Escolha outra.")
            continue

        tabuleiro[posicao] = jogador

        if verificar_vitoria(tabuleiro):
            mostrar_tabuleiro(tabuleiro)
            print(f"🎉 Jogador {jogador} venceu!")
            return

        # Troca de jogador
        jogador = "O" if jogador == "X" else "X"

    mostrar_tabuleiro(tabuleiro)
    print("🤝 Empate!")


# Início do jogo
if __name__ == "__main__":
    jogo_da_velha()
