nome = input('Digite seu nome: ')
materia = input('Digite a matéria: ')

print(f'Olá, {nome}! Vamos calcular a média das suas notas e a frequência de {materia}.')


def ler_resposta(mensagem):
    while True:
        resposta = input(mensagem).strip().lower()

        if resposta in ['s', 'n']:
            return resposta
        else:
            print('Resposta inválida. Digite apenas s ou n.')


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


aula1 = ler_resposta('Você assistiu à aula 1? (s/n): ')
aula2 = ler_resposta('Você assistiu à aula 2? (s/n): ')
aula3 = ler_resposta('Você assistiu à aula 3? (s/n): ')

nota1 = ler_nota('Digite a primeira nota: ')
nota2 = ler_nota('Digite a segunda nota: ')
nota3 = ler_nota('Digite a terceira nota: ')

media = (nota1 + nota2 + nota3) / 3

aulas_assistidas = 0

if aula1 == 's':
    aulas_assistidas += 1

if aula2 == 's':
    aulas_assistidas += 1

if aula3 == 's':
    aulas_assistidas += 1

frequencia = (aulas_assistidas / 3) * 100

print('\n=== Resultado Final ===')
print(f'Aluno: {nome}')
print(f'Matéria: {materia}')
print(f'Média: {media:.2f}')
print(f'Frequência: {frequencia:.1f}%')

if media >= 7 and frequencia >= 75:
    situacao = 'Aprovado'
elif media >= 5 and frequencia >= 65:
    situacao = 'Em recuperação'
else:
    situacao = 'Reprovado'

print(f'Situação: {situacao}')

print(f'\nBom, {nome}, sua média em {materia} é {media:.2f}, sua frequência é {frequencia:.1f}% e sua situação é: {situacao}.')
