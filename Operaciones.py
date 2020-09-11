#Division miembro a miembro
def division(numerador,denominador,op = False):
    resultado=list()
    if (op==False):
        for i in range(len(denominador)):
            resultado.append(numerador/denominador[i])
    if (op==True):
        for i in range(len(numerador)):
            resultado.append(numerador[i]/denominador)
    return resultado

#Restar/Sumar punto a punto
def restar(minuendo,sustraendo):
    resultado=list()
    for i in range(len(sustraendo)):
        resultado.append(minuendo-sustraendo[i])
    return resultado

#Multiplicar miembro a miembro
def multiplicar(multiplicando,multiplicador):
    resultado=list()
    for i in range(len(multiplicador)):
        resultado.append(multiplicando*multiplicador[i])
    return resultado

#Suma miembro a miembro
def suma(aux1,aux2):
    resultado = list()
    for i in range(len(aux1)):
        resultado.append(aux1[i]+aux2[i])
    return resultado
 
