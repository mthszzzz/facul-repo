#  Começo da função dimensoesObjeto
def dimensoesObjeto():  # Função que irá lidar com as dimensões
    while True:
        try:
            comp = float(input('Digite o comprimento do objeto (Em cm): '))
            largura = float(input('Digite a largura do objeto (Em cm): '))
            altura = float(input('Digite a altura do objeto (Em cm): '))
            volume = altura * largura * comp
            global subTotal
            if volume < 1000:  # if e elifs para calcular o preço de acordo com o volume
                vol_valor = 10
                subTotal += vol_valor
                print('O volume do objeto é (Em cm³): {:.1f} (R$: {:.2f})'.format(volume, vol_valor))
                break
            elif 1000 <= volume < 10000:
                vol_valor = 20
                subTotal += vol_valor
                print('O volume do objeto é (Em cm³): {:.1f} (R$ {:.2f})'.format(volume, vol_valor))
                break
            elif 10000 <= volume < 30000:
                vol_valor = 30
                subTotal += vol_valor
                print('O volume do objeto é (Em cm³): {:.1f} (R$: {:.2f})'.format(volume, vol_valor))
                break
            elif 30000 <= volume < 100000:
                vol_valor = 50
                subTotal += vol_valor
                print('O volume do objeto é (Em cm³): {:.1f} (R$: {:.2f})'.format(volume, vol_valor))
                break
            else:  # else para valores maiores que o máximo
                print('O volume do objeto é (Em cm³): {:.1f}'.format(volume))
                print('Não aceitamos objetos com dimensões tão grandes')
                print('Entre com as dimensões desejadas novamente')
                continue  # continue para reedirecionar para as dimensões novamente
        except ValueError:  # except caso digite valor não numérico
            print('Você digitou alguma dimensão do objeto com valor não numérico')
            print('Por favor, entre com as dimensões desejadas novamente')
            continue  # continue para reedirecionar para as dimensões novamente


#  Fim da função dimensoesObjeto
#  Começo da função pesoObjeto
def pesoObjeto():  # função que irá lidar com o peso
    while True:
        try:
            peso = float(input('Digite o peso do objeto (Em kg): '))
            global pesoValor
            if peso <= 0.1:  # if e elifs que retornarão o multiplicador de casa peso
                pesoValor = 1
                break
            elif 0.1 <= peso < 1:
                pesoValor = 1.5
                break
            elif 1 <= peso < 10:
                pesoValor = 2
                break
            elif 10 <= peso < 30:
                pesoValor = 3
                break
            else:  # else para pesos maiores que o máximo
                print('Não aceitamos objetos tão pesados')
                print('Entre com o peso desejado novamente')
                continue  # continue que retornará
        except ValueError:  # except para valores não numéricos
            print('Você digitou o peso do objeto com valor não numérico')
            print('Por favor, entre com o peso desejado novamente')
            continue  # continue que retornará


#  Fim da função pesoObjeto
#  Começo da função rotaObjeto
def rotaObjeto():  # função que irá lidar com a rota
    while True:
        print('Selecione a rota: ')  # tabela de rotas
        print('RS - De Rio de Janeiro até São Paulo')
        print('SR - De São Paulo até Rio de Janeiro')
        print('BS - De Brasília até São Paulo')
        print('SB - De São Paulo até Brasília')
        print('BR - De Brasília até Rio de Janeiro')
        print('RB - Rio de Janeiro até Brasília')
        rota = input('')
        global rotaValor
        if rota == 'RS':  # if e elifs que retornarão o multiplicador de cada rota
            rotaValor = 1
            break
        elif rota == 'SR':
            rotaValor = 1
            break
        elif rota == 'BS':
            rotaValor = 1.2
            break
        elif rota == 'SB':
            rotaValor = 1.2
            break
        elif rota == 'BR':
            rotaValor = 1.5
            break
        elif rota == 'RB':
            rotaValor = 1.5
            break
        else:  # else para rotas não existentes
            print('Você digitou uma rota que não existe')
            print('Por favor, entre com a rota desejada novamente')
            continue  # continue que retornará
        #  Fim da função rotaObjeto


# Começo da função valorTotal
def valorTotal():  # função para fazer o cálculo do total à pagar
    valorTotal = subTotal * pesoValor * rotaValor
    print('Total a pagar(R$): {:.2f} (Dimensões: {} * Peso: {} * Rota: {})'.format(valorTotal, subTotal, pesoValor,
                                                                                   rotaValor))


# Fim da função valorTotal
# main
subTotal = 0
pesoValor = 0
rotaValor = 0
print('Bem vindo a companhia de Logística João Matheus Lúcio Mendes')
dimensoesObjeto()
pesoObjeto()
rotaObjeto()
valorTotal()
# main
