nome = input('Digite seu nome: ')
materia = input('Digite a matéria: ')

print(f'Olá, {nome}! Vamos calcular a média das suas notas e a frequência de {materia}.')


def ler_resposta(mensagem):
    while True:
        resposta = input(mensagem).lower()
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

aula = 0

if aula1 == 's':
    aula += 1
if aula2 == 's':
    aula += 1
if aula3 == 's':
    aula += 1

frequencia = (aula / 3) * 100

print(f'Média: {media:.2f}')
print(f'Frequência: {frequencia:.1f}%')

if media >= 7 and frequencia >= 75:
    print('Aluno aprovado')
elif media >= 5 and media < 7 and frequencia >= 65 and frequencia < 75:
    print('Aluno em recuperação')
else:
    print('Aluno reprovado')

print(f'Bom {nome}, sua média de {materia} é {media:.2f} e sua frequência é {frequencia:.1f}%.')
