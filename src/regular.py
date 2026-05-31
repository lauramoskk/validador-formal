import sys

# Reconhecedor de Linguagem Regular (DFA)
# Valida entradas no formato XXX.XXX.XXX-XX
class DFA:
    def __init__(self):
        self.estado_inicial = "q0"
        self.estados_finais = {"q14"}
        self.passos = 0

        # Dicionário que armazena as transições do autômato
        self.transicoes = {}

        # Primeiros 3 dígitos
        for i in [0, 1, 2]:
            self.transicoes[(f"q{i}", "d")] = f"q{i+1}"

        # Primeiro ponto
        self.transicoes[("q3", ".")] = "q4"

        # Segunda sequência de 3 dígitos
        for i in [4, 5, 6]:
            self.transicoes[(f"q{i}", "d")] = f"q{i+1}"

        # Segundo ponto
        self.transicoes[("q7", ".")] = "q8"

        # Terceira sequência de 3 dígitos
        for i in [8, 9, 10]:
            self.transicoes[(f"q{i}", "d")] = f"q{i+1}"

        # Hífen
        self.transicoes[("q11", "-")] = "q12"

        # Dois dígitos finais
        self.transicoes[("q12", "d")] = "q13"
        self.transicoes[("q13", "d")] = "q14"

    # Agrupa qualquer número como símbolo "d" e mantém "." e "-" como estão
    def tipo_simbolo(self, c):
        if c.isdigit():
            return "d"
        return c

    # Percorre a entrada caractere por caractere verificando se existe transição válida no autômato
    def reconhecer(self, entrada):
        estado = self.estado_inicial
        self.passos = 0

        for c in entrada:
            simbolo = self.tipo_simbolo(c)

            if (estado, simbolo) not in self.transicoes:
                return False, self.passos

            estado = self.transicoes[(estado, simbolo)]
            self.passos += 1

        # Aceita somente se terminar em estado final
        return estado in self.estados_finais, self.passos

# Função usada pelo testes.py
def validar_regular(entrada):
    dfa = DFA()
    return dfa.reconhecer(entrada)

if __name__ == "__main__":
    entrada = sys.argv[1]
    dfa = DFA()

    aceito, passos = dfa.reconhecer(entrada)

    print(f"Entrada: {entrada}")
    print("ACEITA" if aceito else "REJEITADA")
    print(f"Passos: {passos}")