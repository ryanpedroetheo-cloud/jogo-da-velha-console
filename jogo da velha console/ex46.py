def criar_tabuleiro():
    """Cria o tabuleiro 3x3 vazio"""
    return [[" " for _ in range(3)] for _ in range(3)]


def mostrar_tabuleiro(tabuleiro):
    """Mostra o tabuleiro formatado"""
    print("\n   0   1   2")
    for i, linha in enumerate(tabuleiro):
        print(f"{i}  {' | '.join(linha)}")
        if i < 2:
            print("  ---+---+---")


def realizar_jogada(tabuleiro, jogador):
    """Pede linha e coluna e realiza a jogada"""
    while True:
        try:
            linha = int(input(f"{jogador['nome']}, escolha a linha (0, 1, 2): "))
            coluna = int(input(f"{jogador['nome']}, escolha a coluna (0, 1, 2): "))

            if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
                print("Posição inválida! Escolha entre 0, 1 e 2.")
            elif tabuleiro[linha][coluna] != " ":
                print("Essa posição já está ocupada!")
            else:
                tabuleiro[linha][coluna] = jogador["simbolo"]
                break
        except ValueError:
            print("Digite apenas números!")


def verificar_vitoria(tabuleiro, simbolo):
    """Verifica se o jogador venceu"""
    # Linhas
    for linha in tabuleiro:
        if all(casa == simbolo for casa in linha):
            return True

    # Colunas
    for col in range(3):
        if all(tabuleiro[linha][col] == simbolo for linha in range(3)):
            return True

    # Diagonais
    if all(tabuleiro[i][i] == simbolo for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == simbolo for i in range(3)):
        return True

    return False


def verificar_empate(tabuleiro):
    """Verifica se o jogo empatou"""
    return all(casa != " " for linha in tabuleiro for casa in linha)


def alternar_jogador(jogador_atual, jogador1, jogador2):
    """Alterna o jogador da vez"""
    return jogador2 if jogador_atual == jogador1 else jogador1


def main():
    print("  JOGO DA VELHA  ")

    # Cadastro dos jogadores
    jogador1 = {"nome": input("Nome do Jogador 1 (X): "), "simbolo": "X", "pontos": 0}
    jogador2 = {"nome": input("Nome do Jogador 2 (O): "), "simbolo": "O", "pontos": 0}

    while True:
        tabuleiro = criar_tabuleiro()
        jogador_atual = jogador1
        vencedor = None

        print("\nNovo Jogo!")
        mostrar_tabuleiro(tabuleiro)

        # Loop das jogadas
        while True:
            realizar_jogada(tabuleiro, jogador_atual)
            mostrar_tabuleiro(tabuleiro)

            # Verificar vitória
            if verificar_vitoria(tabuleiro, jogador_atual["simbolo"]):
                print(f"🎉 {jogador_atual['nome']} venceu!")
                jogador_atual["pontos"] += 1
                vencedor = jogador_atual
                break

            # Verificar empate
            if verificar_empate(tabuleiro):
                print("🤝 Empate!")
                break

            # Alternar jogador
            jogador_atual = alternar_jogador(jogador_atual, jogador1, jogador2)

        # Mostrar pontuação
        print("\n===== PLACAR =====")
        print(f"{jogador1['nome']}: {jogador1['pontos']} ponto(s)")
        print(f"{jogador2['nome']}: {jogador2['pontos']} ponto(s)")

        # Perguntar se querem jogar novamente
        continuar = input("\nDesejam jogar novamente? (s/n): ").lower()
        if continuar != "s":
            print("\n🏁 Jogo encerrado!")
            print("Placar final:")
            print(f"{jogador1['nome']}: {jogador1['pontos']} ponto(s)")
            print(f"{jogador2['nome']}: {jogador2['pontos']} ponto(s)")
            break


# Executar o jogo
if __name__ == "__main__":
    main()
