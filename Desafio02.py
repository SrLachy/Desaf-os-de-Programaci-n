'''
 Escriba un programa que pregunte al usuario la hora actual t del reloj y un número
 entero de horas h, que indique qué hora marcará el reloj dentro de h horas:
'''

def calcular_hora_futura(hora_actual, horas_pasadas):
    hora_futura = (hora_actual + horas_pasadas) % 24
    return hora_futura

try:
    hora_actual = int(input("Ingresa la hora actual (formato de 24 horas): "))
    horas_pasadas = int(input("Ingresa la cantidad de horas pasadas: "))

    hora_futura = calcular_hora_futura(hora_actual, horas_pasadas)

    print(f"En {horas_pasadas} horas, el reloj marcará las {hora_futura}.")

except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")
