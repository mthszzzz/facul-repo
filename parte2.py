subTotal = 0  # Valor inicial
print('Bem vindo a lanchonete do João Matheus Lúcio Mendes')
print('********** Cardápio **********')  # Cardápio que apresentará as informações.
print('| Código | Descrição | Valor |')
print('| 100 | Cachorro-Quente | 9.00 |')
print('| 101 | Cachorro-Quente Duplo | 11.00 |')
print('| 102 | X-Egg | 12.00 |')
print('| 103 | X-Salada | 13.00 |')
print('| 104 | X-Bacon | 14.00 |')
print('| 105 | X-Tudo | 17.00 |')
print('| 200 | Refrigerante Lata | 5.00 |')
print('| 201 | Chá Gelado | 4.00 |')
while True:  # Loop infinito que findará quando o cliente acabar seu pedido.
    codigo = int(input('Entre com o código desejado: '))
    if codigo == 100:  # if que adicionará o preço no subTotal e exibirá o print.
        subTotal += 9.00  # Preço adcionado ao subTotal.
        print('Você pediu um Cachorro-Quente no valor de 9.00')  # print do pedido.
    elif codigo == 101:
        subTotal += 11.00
        print('Você pediu um Cachorro-Quente Duplo no valor de 11.00')
    elif codigo == 102:
        subTotal += 12.00
        print('Você pediu um X-Egg no valor de 12.00')
    elif codigo == 103:
        subTotal += 13.00
        print('Você pediu um X-Salada no valor de 13.00')
    elif codigo == 104:
        subTotal += 14.00
        print('Você pediu um X-Bacon no valor de 14.00')
    elif codigo == 105:
        subTotal += 17.00
        print('Você pediu um X-Tudo no valor de 17.00')
    elif codigo == 200:
        subTotal += 5.00
        print('Você pediu um Refrigerante (Lata) no valor de 5.00')
    elif codigo == 201:
        subTotal += 4.00
        print('Você pediu um Chá Gelado no valor de 4.00')
    else:  #  else que vai invalidar qualquer código inexistente no cardápio.
        print('Código inválido!')
        continue  # continue que faz o usuário poder escolher outra opção caso erre o código.
    resp = int(input('Deseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n'))
    if resp == 1:
        continue  # Volta para o começo do laço.
    else:
        print('O total a ser pago: R${:.2f}'.format(subTotal))  # print do total a ser pago armazenado no subTotal.
        break  # Sair do laço.
