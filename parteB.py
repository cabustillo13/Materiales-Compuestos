#python 3.8 src 

import matplotlib.pyplot as plt
import numpy as np
if __name__ == "__main__":

    #Definicion de constantes
    x=200                       #x:largo    [mm]
    y=100                       #y:ancho    [mm]
    z=0.2                       #z: espesor [mm]
    E1=155                      #GPa = 1 kN/mm^2
    E2=12.1                     #GPa = 1 kN/mm^2
    E3=12.1                     #GPa = 1 kN/mm^2
    v23=0.458
    v12=0.248
    v13=0.248
    G23=3.2                     #GPa = 1 kN/mm^2
    G12=4.4                     #GPa = 1 kN/mm^2
    G13=4.4                     #GPa = 1 kN/mm^2

    sigma = [4/(y*z), 0, 0]     #sigma 1, 2 y 3

    # Inciso a)
    epsylon3 = (-v13/E1)* sigma[0] + (-v23/E2)*sigma[1]
    print("Cálculo de epsylon3: ", epsylon3)

    #Inciso b)
    #Matriz de flexibilidad reducida

    S11=1/E1
    S12=-v12/E1
    S22=1/E2
    S66=1/G12

    S = [[S11, S12, 0],
        [S12, S22, 0],
        [0, 0, S66]]

    #Restricciones de coef. de Poisson
    v21=(v12/E1)*E2
    v31=(v13/E1)*E3

    #Matriz de rigidez reducida
    Q = [[E1/(1-v12*v21), (v12*E2)/(1-v21*v12), 0],
        [(v12*E2)/(1-v21*v12), E2/(1-v21*v12), 0],
        [0, 0, G12]]

    INV=np.linalg.inv(S)

    print("Matrices S: ", S, "\ny Q:\n", Q)

    # Inciso c)Comparacion entre S y Q
    if (np.all(Q)==np.all(INV)):
        print("Las matrices son iguales")

    #Inciso d)
    dominio = np.arange(-np.pi/2,np.pi/2,(np.pi/100))

    S11n=[]
    S12n=[]
    S22n=[]
    S16n=[]
    S26n=[]
    S66n=[]




    for i in dominio:
        S11n.append( S11 * np.power(np.cos(i),4) + (2*S12+S66) * np.power((np.cos(i)*np.sin(i)),2) + S22 * np.power(np.sin(i),4))
        S12n.append( S12 * (np.power(np.sin(i),4) + np.power(np.cos(i),4))+(S11+S22-S66)*np.power((np.sin(i)*np.cos(i)),2))
        S22n.append(S11*np.power(np.sin(i),4)+(2*S12+S66)*np.power((np.sin(i)*np.cos(i)),2)+S22*np.power(np.cos(i),4))
        S16n.append((2*S11-2*S12-S66)* np.sin(i)*np.power(np.cos(i),3) - (2*S22-2*S12-S66)* np.cos(i)*np.power(np.sin(i),3))
        S26n.append((2*S11-2*S12-S66)* np.cos(i)*np.power(np.sin(i),3) - (2*S22-2*S12-S66)* np.sin(i)*np.power(np.cos(i),3))
        S66n.append(2* (2*S11+2*S22-4*S12-S66)* np.power((np.sin(i)*np.cos(i)),2)+S66*(np.power(np.sin(i),4)+np.power(np.cos(i),4)))  

    #Gráficos
    plt.figure()
    plt.subplot(2,3,1)
    plt.plot(dominio,S11n)
    plt.subplot(2,3,2)
    plt.plot(dominio,S12n)
    plt.subplot(2,3,3)
    plt.plot(dominio,S22n)
    plt.subplot(2,3,4)
    plt.plot(dominio,S16n)
    plt.subplot(2,3,5)
    plt.plot(dominio,S26n)
    plt.subplot(2,3,6)
    plt.plot(dominio,S66n)
    plt.show()

