import datetime

def calcular_idade(ano_atual, data_nascimento):
    # Obtém a data atual
    data_atual = datetime.datetime.now()

    # Separa o ano, mês e dia da data de nascimento
    ano_nascimento, mes_nascimento, dia_nascimento = map(int, data_nascimento.split('-'))

    # Calcula a idade
    idade = ano_atual - ano_nascimento

    # Verifica se o aniversário deste ano já ocorreu
    if (mes_nascimento, dia_nascimento) > (data_atual.month, data_atual.day):
        idade -= 1

    return idade

# Solicita ao usuário que insira o ano atual e a data de nascimento
ano_atual = int(input("Digite o ano atual: "))
data_nascimento = input("Digite sua data de nascimento (no formato AAAA-MM-DD): ")

# Chama a função para calcular a idade
idade = calcular_idade(ano_atual, data_nascimento)

# Exibe a idade do usuário
print("Sua idade é:", idade)
