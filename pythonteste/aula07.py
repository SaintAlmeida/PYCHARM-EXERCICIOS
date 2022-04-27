n1 = int(input('Um valor:'))
n2 = int(input('Segundo Valor:'))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma vale {}, A multiplicação vale {}, a Divisão Vale {:.3f} '.format(s,m,d), end=' ')
print('Divisão Inteira {} e a potência {}'.format(di,e))