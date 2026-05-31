import os

from regular import validar_regular
from livre_contexto import validar_livre_contexto
from recursiva import validar_recursiva

# Diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TESTES_DIR = os.path.join(BASE_DIR, "testes")

# Lê o arquivo .txt de testes
# Formato esperado:
# entrada;true
# entrada;false
def carregar_testes(nome_arquivo):
    caminho = os.path.join(TESTES_DIR, nome_arquivo)

    testes = []

    with open(caminho, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()

            # Ignora linhas vazias ou comentários
            if not linha or linha.startswith("#"):
                continue

            entrada, esperado = linha.split(";")

            testes.append(
                (
                    entrada.strip(),
                    esperado.strip().lower() == "true"
                )
            )

    return testes

# Executa todos os testes de um reconhecedor e compara o resultado obtido com o esperado
def executar(nome, funcao, arquivo):
    print("\n" + "=" * 60)
    print(nome)
    print("=" * 60)

    testes = carregar_testes(arquivo)

    for entrada, esperado in testes:
        resultado, passos = funcao(entrada)

        status = "OK" if resultado == esperado else "ERRO"

        print(f"Entrada: {entrada}")
        print(f"Esperado: {esperado}")
        print(f"Obtido: {resultado}")
        print(f"Passos: {passos}")
        print(f"Resultado: {status}")
        print("-" * 60)

# Executa a bateria de testes dos 3 reconhecedores:
# regular, livre de contexto e recursivo
def main():
    executar(
        "RECONHECEDOR REGULAR",
        validar_regular,
        "testes_regular.txt"
    )

    executar(
        "RECONHECEDOR LIVRE DE CONTEXTO",
        validar_livre_contexto,
        "testes_livre_contexto.txt"
    )

    executar(
        "RECONHECEDOR RECURSIVO",
        validar_recursiva,
        "testes_recursiva.txt"
    )

if __name__ == "__main__":
    main()