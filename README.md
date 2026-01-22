# 📘 Curso NumPy na Prática

Repositório com exercícios, exemplos e mini projetos desenvolvidos durante a seção **NumPy – Hands On**, organizada aula por aula, com foco em aprendizado prático, versionamento profissional e construção de portfólio para **Análise de Dados**.

---

## 🎯 Objetivo do Repositório

- Consolidar os **fundamentos do NumPy**
- Trabalhar com **arrays multidimensionais**
- Aplicar **indexação, fatiamento e funções universais**
- Entender **copy, view, reshape e iteração**
- Manipular dados com **join, split e search**
- Aplicar os conhecimentos em **mini projetos práticos**
- Utilizar **Git e commits padronizados (Conventional Commits)**

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- NumPy
- Jupyter Notebook
- VS Code
- Git & GitHub

---

## 📂 Estrutura do Projeto
````
curso-numpy/
│
├─ README.md
├─ .gitignore
├─ requirements.txt
│
├─ 1-fundamentos.ipynb
├─ 2-dimensoes.ipynb
├─ 3-indexacao.ipynb
├─ 4-fatiamento.ipynb
├─ 5-funcoes.ipynb
├─ 6-copy.ipynb
├─ 7-reshape.ipynb
├─ 8-iteracao.ipynb
├─ 9-join.ipynb
├─ 10-split.ipynb
├─ 11-search.ipynb
├─ 12-final.ipynb
│
├─ caca-tesouro.py
└─ jogo-velha.py
````

---

## 📚 Conteúdo do Curso (conforme commits)

### ✅ 1. Fundamentos do NumPy
**Arquivo:** `1-fundamentos.ipynb`

- Criação de arrays
- Tipos de dados
- Operações matemáticas básicas
- Introdução ao NumPy

---

### ✅ 2. Arrays Multidimensionais
**Arquivo:** `2-dimensoes.ipynb`

- Arrays 1D, 2D, 3D e 4D
- `ndim`, `shape`
- Aplicações práticas (listas, matrizes, imagens)

---

### ✅ 3. Indexação e Seleção
**Arquivo:** `3-indexacao.ipynb`

- Acesso por índice
- Seleção por linha e coluna
- Máscaras booleanas
- Alteração de valores

---

### ✅ 4. Fatiamento de Arrays
**Arquivo:** `4-fatiamento.ipynb`

- Subarrays
- Recortes por linha e coluna
- Modificação de regiões específicas

---

### ✅ 5. Funções Universais
**Arquivo:** `5-funcoes.ipynb`

- Operações matemáticas
- Funções trigonométricas
- Estatísticas (`mean`, `std`)
- Funções exponenciais e logarítmicas

---

### ✅ 6. Copy e View
**Arquivo:** `6-copy.ipynb`

- Diferença entre **cópia profunda** e **view**
- Impacto na memória
- Alterações compartilhadas

---

### ✅ 7. Reshape
**Arquivo:** `7-reshape.ipynb`

- Conversão de arrays 1D → 2D
- Simulação de imagens
- Transformações estruturais

---

### ✅ 8. Iteração em Arrays
**Arquivo:** `8-iteracao.ipynb`

- Loops tradicionais
- `np.nditer`
- Iteração com condição
- Iteração por índices

---

### ✅ 9. Join (Concatenação)
**Arquivo:** `9-join.ipynb`

- `concatenate`
- `vstack`, `hstack`
- `column_stack`
- Construção de tabelas de dados

---

### ✅ 10. Split
**Arquivo:** `10-split.ipynb`

- `np.split`
- Divisão de dados em partes
- Análise de médias por grupo

---

### ✅ 11. Search (Busca em Arrays)
**Arquivo:** `11-search.ipynb`

- `np.where`
- `np.argmax`
- Identificação de valores
- Casos práticos com notas

---

### ✅ 12. Consolidação Final
**Arquivo:** `12-final.ipynb`

- Combinação de todos os conceitos
- Organização de dados em tabelas
- Agrupamento e análise final

---

## 🎮 Mini Projeto 1 – Caça ao Tesouro

**Arquivo:** `caca-tesouro.py`

Jogo interativo em terminal utilizando NumPy:

- Mapa 2D gerado aleatoriamente
- Movimentação do jogador
- Pontuação por movimentos
- Validação de limites
- Lógica aplicada com arrays

### 📽️ Demonstração

![Caça ao Tesouro](caca-ao-tesouro.gif)

---

## 🎮 Mini Projeto 2 – Jogo da Velha

**Arquivo:** `jogo-velha.py`

Jogo clássico implementado com NumPy:

- Tabuleiro 3x3
- Dois jogadores (X e O)
- Verificação de vitória por linhas, colunas e diagonais
- Tratamento de empate
- Interface amigável no terminal

### 📽️ Demonstração

![Jogo da Velha](jogo-da-velha.gif)

---

## 🚀 Como Executar o Projeto

1. Clone o repositório:
```bash
git clone https://github.com/brunodutraho/curso-numpy.git
````
2. Entre na pasta do projeto:
```bash
cd curso-numpy
````
3. Ative o ambiente virtual:
```bash
python -m venv .venv
.\.venv\Scripts\activate
````
4. Instale as dependências:
```bash
pip install -r requirements.txt
````
5. Execute os notebooks ou os projetos:
```bash
jupyter notebook
python caca-tesouro.py
python jogo-velha.py
````

## 🧠 Aprendizados

Este repositório consolida minha **base sólida em NumPy**, servindo como preparação para etapas mais avançadas da área de **Análise de Dados**, incluindo:

- Uso de **Pandas** para manipulação de dados tabulares
- Análise exploratória de dados (EDA)
- Manipulação de **datasets reais**
- Construção de **dashboards e geração de insights**
