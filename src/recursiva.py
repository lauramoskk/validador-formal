import sys

# Simulação de Máquina de Turing
# Verifica se a entrada está no formato w#w, ou seja, se o lado esquerdo é igual ao lado direito
class TuringMachine:
    def __init__(self):
        self.passos = 0

    # Reconhece cadeias separadas por '#'
    # Exemplo aceito: abc#abc
    def reconhecer(self, entrada):
        self.passos = 0

        # A entrada precisa conter exatamente um separador '#'
        if entrada.count("#") != 1:
            return False, self.passos

        esquerda, direita = entrada.split("#")

        # Conta a leitura completa da entrada como número de passos
        self.passos += len(entrada)

        # Aceita somente se os dois lados forem iguais
        if esquerda == direita:
            return True, self.passos

        return False, self.passos

# Função usada pelo testes.py
def validar_recursiva(entrada):
    mt = TuringMachine()
    return mt.reconhecer(entrada)

if __name__ == "__main__":
    entrada = sys.argv[1]

    mt = TuringMachine()

    aceito, passos = mt.reconhecer(entrada)

    print(f"Entrada: {entrada}")
    print("ACEITA" if aceito else "REJEITADA")
    print(f"Passos: {passos}")