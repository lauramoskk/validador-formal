# Validador Formal

Projeto desenvolvido em Python para validação de linguagens formais utilizando três reconhecedores:

* **Linguagem Regular (DFA)**
* **Linguagem Livre de Contexto (PDA)**
* **Linguagem Recursiva (Máquina de Turing simulada)**

---

## Como executar

Abra o terminal dentro da pasta do projeto e rode:

```bash
python src/testes.py
```

Esse comando executa todos os testes automaticamente.

---

## Executar arquivos individualmente

### 1. Reconhecedor Regular

```bash
python src/regular.py 123.456.789-00
```

---

### 2. Reconhecedor Livre de Contexto

```bash
python src/livre_contexto.py "(())"
```

---

### 3. Reconhecedor Recursivo

```bash
python src/recursiva.py "abc#abc"
```

---

## Executar os testes

Os arquivos de teste ficam na pasta:

```bash
/testes
```

Para rodar todos os testes:

```bash
python src/testes.py
```

A saída mostrará:

* entrada testada
* resultado esperado
* resultado obtido
* quantidade de passos
* status (`OK` ou `ERRO`)

---

## Requisito

Python 3 instalado.

Verificar versão:

```bash
python --version
```
