# Sistema de Média e Frequência Escolar em Python

Este projeto foi desenvolvido em **Python** com o objetivo de praticar lógica de programação, funções, validação de dados, cálculo de média escolar e cálculo de frequência.

O sistema recebe o nome do aluno, a matéria, a quantidade de aulas assistidas, a quantidade de aulas não assistidas e as notas dos quatro bimestres. Ao final, calcula a média, a frequência e informa a situação final do aluno.

## Funcionalidades

- Recebe o nome do aluno
- Recebe o nome da matéria
- Recebe a quantidade de aulas assistidas
- Recebe a quantidade de aulas não assistidas
- Valida se a quantidade de aulas é um número inteiro positivo
- Recebe quatro notas bimestrais
- Valida se as notas estão entre 0 e 10
- Calcula a média final do aluno
- Calcula a frequência com base no total de aulas
- Informa a situação final:
  - Aprovado
  - Em recuperação
  - Reprovado

## Tecnologias utilizadas

- Python

## Regras do sistema

O aluno será considerado:

- **Aprovado**: média maior ou igual a 7 e frequência maior ou igual a 70%
- **Em recuperação**: média maior ou igual a 5 e frequência maior ou igual a 50%
- **Reprovado**: caso não atinja os critérios anteriores

## Como executar o projeto

1. Clone este repositório:

```bash
git clone https://github.com/reelmalaquias/calculadora-media-python.git
```

2. Acesse a pasta do projeto:

```bash
cd calculadora-media-python
```

3. Execute o arquivo principal:

```bash
python main.py
```

## Exemplo de uso

```text
Digite o nome do aluno: Rafael
Digite a matéria: Matemática

Olá, Rafael! Vamos calcular a média e frequência de Matemática.

Digite o número de aulas assistidas: 18
Digite o número de aulas não assistidas: 2

Digite a nota do 1º bimestre: 8
Digite a nota do 2º bimestre: 7
Digite a nota do 3º bimestre: 6
Digite a nota do 4º bimestre: 7

=== Resultado Final ===
Aluno: Rafael
Matéria: Matemática
Média: 7.0
Frequência: 90.0%
Situação: Aprovado
```

## Conceitos praticados

Neste projeto foram praticados os seguintes conceitos:

- Entrada de dados com `input`
- Conversão de valores com `int` e `float`
- Estruturas condicionais `if`, `elif` e `else`
- Laços de repetição com `while`
- Criação e uso de funções
- Validação de dados
- Tratamento de erros com `try` e `except`
- Cálculo de média
- Cálculo de porcentagem
- Uso de f-strings
- Operadores lógicos como `and`

## Estrutura do projeto

```text
calculadora-media-python/
│
├── main.py
├── README.md
└── .gitignore
```

## Objetivo de aprendizado

Este projeto faz parte dos meus estudos iniciais em programação com Python.

O objetivo é reforçar a lógica de programação, praticar validação de dados e criar meus primeiros projetos para portfólio no GitHub, visando minha evolução para a área de desenvolvimento Back-End.

## Autor

Desenvolvido por **Rafael Alves Malaquias**.

- GitHub: [reelmalaquias](https://github.com/reelmalaquias)
- LinkedIn: [Rafael Malaquias](https://www.linkedin.com/in/rafael-malaquias-7a819214b/)