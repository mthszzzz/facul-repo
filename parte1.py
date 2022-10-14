print('Bem vindo a loja do João Matheus Lúcio Mendes!')
valorProduto = float(input('Entre com o valor do produto: '))
qtdProduto = int(input('Entre com a quantidade: '))
subTotal = valorProduto * qtdProduto
if qtdProduto < 10:  # if para o valor sem desconto.
    valorFinal = subTotal
    d = ('O valor com desconto foi: R$ {:.2f} (Não houve desconto!)'.format(valorFinal))
elif qtdProduto < 100:  # elif para o desconto de 5%.
    valorFinal = subTotal - (subTotal * 0.05)
    d = ('O valor com desconto foi: R$ {:.2f} (Desconto de 5%)'.format(valorFinal))
elif qtdProduto < 999:  # elif para o desconto de 10%
    valorFinal = subTotal - (subTotal * 0.1)
    d = ('O valor com desconto foi: R$ {:.2f} (Desconto de 10%)'.format(valorFinal))
else:  # else para desconto de 15%.
    valorFinal = subTotal - (subTotal * 0.15)
    d = ('O valor com desconto foi: R$ {:.2f} (Desconto de 15%)'.format(valorFinal))
print('O Valor sem desconto foi: R$ {:.2f}'.format(subTotal))  # Mostra o valor sem desconto.
print('{}'.format(d))  # Mostra o valor com desconto e qual desconto foi utilizado.