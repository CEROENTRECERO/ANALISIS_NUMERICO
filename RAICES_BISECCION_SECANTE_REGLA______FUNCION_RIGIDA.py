import math

# DEFINICIÓN DE FUNCIÓNES:
def f(x):
    return math.exp(x)-3*x

def cambia_cotas_b(inferior,superior):
    nuevo_valor = (inferior + superior)/2
    if f(nuevo_valor) == 0:
        return nuevo_valor, 'RAIZ'
    elif f(nuevo_valor) < 0:
        if f(inferior) < 0:
            inferior = nuevo_valor
        else:
            superior = nuevo_valor
        return inferior, superior
    else:
        if f(inferior) < 0:
            superior = nuevo_valor
        else:
            inferior = nuevo_valor
        return inferior, superior

def cambia_cotas_rf(penultimo, ultimo):
    nuevo_valor = ultimo - (f(ultimo)*((penultimo-ultimo)/(f(penultimo)-f(ultimo))))

    if f(nuevo_valor) < 0:
        if f(penultimo) > 0:
            ultimo = penultimo
    else:
        if f(ultimo) > 0:
            ultimo = penultimo
    primera = False

    return ultimo, nuevo_valor

def cambia_cotas_s(penultimo, ultimo, primera):
    nuevo_valor = ultimo - (f(ultimo)*((penultimo-ultimo)/(f(penultimo)-f(ultimo))))

    if primera:
        if f(nuevo_valor) < 0:
            if f(penultimo) > 0:
                ultimo = penultimo
        else:
            if f(ultimo) > 0:
                ultimo = penultimo
        primera = False

    return ultimo, nuevo_valor, primera


# Tabla incial
print('{:-^60}'.format('TABLA'))
for x in [t*0.1 for t in range(0,21)]:
     print('{:.1f}'.format(x) + '\t' + '{:5.2f}'.format(math.exp(x)-3*x))


#TOLERANCIA Y COTAS PARA EL PRIMER MÉTODO
tol = 0.001
cotas = (0.6,0.7)

print('{:-^60}'.format('BISECCIÓN') + '\n')
print('{:^10}'.format('INFERIOR') + '\t' + '{:^10}'.format('SUPERIOR') + '\t' +
    '{:^10}'.format('f(i)') + '\t' + '{:^10}'.format('f(s)') + '\t' +
    '{:^10}'.format('ERROR A') + '\n')

while True:
    print('{:8.4f}'.format(cotas[0]) + '\t' +'{:8.4f}'.format(cotas[1]) + '\t' +'{:8.4f}'.format(f(cotas[0])) + '\t' + '{:8.4f}'.format(f(cotas[1])) + '\t' +
          '{:8.4f}'.format(math.fabs(cotas[0]-cotas[1])) + '\n')
    if math.fabs(cotas[0]-cotas[1]) <= tol:
        break
    cotas = cambia_cotas_b(cotas[0],cotas[1])




#TOLERANCIA Y COTAS PARA EL SEGUNDO MÉTODO
tol = 0.006
cotas = (0.6,0.7)

print('\n\n')
print('{:-^60}'.format('REGLA FALSA') + '\n')
print('{:^10}'.format('PENULTIMO') + '\t' + '{:^10}'.format('ULTIMO') + '\t' +
    '{:^10}'.format('f(P)') + '\t' + '{:^10}'.format('f(U)') + '\t' +
    '{:^10}'.format('ERROR A') + '\n')

while True:
    print('{:10.7f}'.format(cotas[0]) + '\t' +'{:10.7f}'.format(cotas[1]) + '\t' +'{:10.7f}'.format(f(cotas[0])) + '\t' + '{:10.7f}'.format(f(cotas[1])) + '\t' +
          '{:10.7f}'.format(math.fabs(cotas[0]-cotas[1])) + '\n')
    if math.fabs(cotas[0]-cotas[1]) <= tol:
        break
    cotas = cambia_cotas_rf(cotas[0],cotas[1])




#TOLERANCIA Y COTAS PARA EL TERCER MÉTODO
tol = 0.006
cotas = (0.6,0.7,True)

print('\n\n')
print('{:-^60}'.format('SECANTE') + '\n')
print('{:^10}'.format('PENULTIMO') + '\t' + '{:^10}'.format('ULTIMO') + '\t' +
    '{:^10}'.format('f(P)') + '\t' + '{:^10}'.format('f(U)') + '\t' +
    '{:^10}'.format('ERROR A') + '\n')

while True:
    print('{:10.7f}'.format(cotas[0]) + '\t' +'{:10.7f}'.format(cotas[1]) + '\t' +'{:10.7f}'.format(f(cotas[0])) + '\t' + '{:10.7f}'.format(f(cotas[1])) + '\t' +
          '{:10.7f}'.format(math.fabs(cotas[0]-cotas[1])) + '\n')
    if math.fabs(cotas[0]-cotas[1]) <= tol:
        break
    cotas = cambia_cotas_s(cotas[0],cotas[1],cotas[2])
