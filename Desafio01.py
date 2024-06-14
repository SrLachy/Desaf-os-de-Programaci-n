'''
Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el
número con los dígitos en orden inverso:
'''

numero = int(input('Ingrese un número entero de 3 dígitos: '))

if 100 <= numero <= 999:
    tercer_digito = numero % 10
    segundo_digito = (numero // 10) % 10
    primer_digito = numero // 100
    numero_inverso = tercer_digito * 100 + segundo_digito * 10 + primer_digito
    print (f'El número con los dígitos invertidos es: {numero_inverso}')
else:
    print ('Por favor, ingrese un número de 3 dígitos válido.')
