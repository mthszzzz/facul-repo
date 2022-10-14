estoque = []  # estoque para uso de consulta


# Cadastrar Peça
def cadastrarPeca(cod):
    print('Você selecionou a Opção de Cadastrar Peça')
    print('Código da Peça {}'.format(cod))
    nome = input('Por favor entre com o nome da peça: ')
    fabricante = input('Por favor entre com o fabricante da peça: ')
    valor = float(input('Por favor entre com o valor(R$) da peça: '))
    global codigo  # chamada global do codigo
    estoqueCad = {'Código': codigo, 'Peça': nome, 'Fabricante': fabricante, 'Valor': valor}
    estoque.append(estoqueCad.copy())  # append (copia) do estoque pro estoque global


# Cadastrar Peça
# Consultar Peça
def consultarPeca():
    while True:
        print('Você selecionou a Opção de Consultar Peças')
        try:
            opConsultar = int(input(
                'Escolha uma opção desejada:\n1-Consultar Todas as Peças\n2-Consultar Peças por Código\n3-Consultar Peças por Fabricante\n4-Retornar\n'))
            if opConsultar == 1:
                print('Você Selecionou a Opção de Consultar Todas as Peças')
                for pecas in estoque:  # Seleciona cada canto do meu estoque
                    for key, value in pecas.items():  # Seleciona cada canto das peças
                        print('-' * 20)
                        print('{} : {}'.format(key, value))  # print dos valores
            elif opConsultar == 2:
                print('Você Selecionou a Opção de Consultar Peças por Código')
                entrada = int(input('Digite o código desejado: '))
                for pecas in estoque:  # for que procura peça no estoque
                    if (pecas['Código']) == entrada:
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 3:
                print('Você selecionou a Opção de Consultar Peças por Fabricante')
                entrada = input('Digite a turma desejada: ')
                for pecas in estoque:  # for que procura fabricante no estoque
                    if (pecas['Fabricante']) == entrada:
                        for key, value in pecas.items():
                            print('{} : {}'.format(key, value))
            elif opConsultar == 4:
                return  # return do sub-menu de volta para o menu principal
            else:
                print('Digite um número válido do menu')
                continue
        except ValueError:  # expect de valor não inteiro
            print('Não digite valores não inteiros')

        # Consultar Peça


# Remover Peça
def removerPeca():  # função que vai remover do estoque 
    entrada = int(input('Digite o código desejado: '))
    for pecas in estoque:  # for que procura peça no estoque 
        if (pecas['Código']) == entrada:
            estoque.remove(pecas)


# Remover Peça
# Main
codigo = 0  # Código antes da contagem
while True:
    try:
        print('Bem vindo ao controle de estoque da bicicletaria do João Mathes Lúcio Mendes')
        opcoes = int(
            input('Escolha uma opção desejada:\n1-Cadastrar Peças\n2-Consultar Peças\n3-Remover Peças\n4-Sair\n'))
        if opcoes == 1:
            codigo += 1  # Gerador de número
            cadastrarPeca(codigo)
        elif opcoes == 2:
            consultarPeca()
        elif opcoes == 3:
            removerPeca()
        elif opcoes == 4:
            break
        else:
            print('Digite um número válido do menu')
            continue
    except ValueError:  # expect de valor não inteiro
        print('Não digite valores não inteiros')
