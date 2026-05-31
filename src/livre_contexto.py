import sys

# Reconhecedor de Linguagem Livre de Contexto (PDA)
# Verifica se os parênteses da entrada estão balanceados
class PDA:
    def __init__(self):
        self.passos = 0

    # Usa uma pilha para armazenar os parênteses abertos
    # Cada ')' encontrado precisa corresponder a um '(' anterior
    def reconhecer(self, entrada):
        pilha = []
        self.passos = 0

        for simbolo in entrada:
            self.passos += 1

            if simbolo == "(":
                pilha.append(simbolo)

            elif simbolo == ")":
                if not pilha:
                    return False, self.passos
                pilha.pop()

        # A cadeia só é aceita se a pilha terminar vazia
        return len(pilha) == 0, self.passos

# Função usada pelo testes.py
def validar_livre_contexto(entrada):
    pda = PDA()
    return pda.reconhecer(entrada)

if __name__ == "__main__":
    entrada = sys.argv[1]

    pda = PDA()
    aceito, passos = pda.reconhecer(entrada)

    print(f"Entrada: {entrada}")
    print("ACEITA" if aceito else "REJEITADA")
    print(f"Passos: {passos}")