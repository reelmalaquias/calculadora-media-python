nome = input('Digite o nome do aluno: ')
materia = input('Digite a matéria: ')

print(f'Olá, {nome}! Vamos calcular a média e frequência de {materia}.')


def ler_aula(mensagem):
    while True:
        try:
            aula = int(input(mensagem))

            if aula >= 0:
                return aula
            else:
                print('Número de aulas inválido. Digite um valor positivo.')

        except ValueError:
            print('Entrada inválida. Digite apenas números inteiros.')


def ler_nota(mensagem):
    while True:
        try:
            nota = float(input(mensagem))

            if 0 <= nota <= 10:
                return nota
            else:
                print('Nota inválida. Digite um valor entre 0 e 10.')

        except ValueError:
            print('Entrada inválida. Digite apenas números.')


while True:
    aulas_assistidas = ler_aula('Digite o número de aulas assistidas: ')
    aulas_nao_assistidas = ler_aula('Digite o número de aulas não assistidas: ')

    total_aulas = aulas_assistidas + aulas_nao_assistidas

    if total_aulas > 0:
        break
    else:
        print('O total de aulas não pode ser zero. Digite novamente.')


nota1 = ler_nota('Digite a nota do 1º bimestre: ')
nota2 = ler_nota('Digite a nota do 2º bimestre: ')
nota3 = ler_nota('Digite a nota do 3º bimestre: ')
nota4 = ler_nota('Digite a nota do 4º bimestre: ')

frequencia = (aulas_assistidas / total_aulas) * 100
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7 and frequencia >= 70:
    situacao = 'Aprovado'
elif media >= 5 and frequencia >= 50:
    situacao = 'Em recuperação'
else:
    situacao = 'Reprovado'

print('\n=== Resultado Final ===')
print(f'Aluno: {nome}')
print(f'Matéria: {materia}')
print(f'Média: {media:.1f}')
print(f'Frequência: {frequencia:.1f}%')
print(f'Situação: {situacao}')

print(f'\nBom, {nome}, sua média em {materia} é {media:.1f}, sua frequência é {frequencia:.1f}% e sua situação é: {situacao}.')