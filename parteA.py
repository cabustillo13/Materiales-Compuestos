"""
PARTE A: Una  lamina de compuesto de  polimero  reforzado  con  grafito 
"""
import numpy as np
import Operaciones
import matplotlib.pyplot as plt

#Inicializacion datos 
Em= 4.62*(10**9)
Ef1=233*(10**9)
Ef2=23.1*(10**9)    
vm=0.36             #Coeficiente de Poisson
vf12=0.2
Gf12=8.96*(10**9)
Vf=np.arange(0,1.1,0.1)  #Fraccion de volumen 

#Calculo
Vm = Operaciones.restar(1,Vf)
vc = Operaciones.division(vm,Vm)
E1 = Operaciones.suma(Operaciones.multiplicar(Ef1,Vf), Operaciones.multiplicar(Em,Vm))
E2 = Operaciones.division(Ef2*Em,Operaciones.suma(Operaciones.multiplicar(Em,Vf),Operaciones.multiplicar(Ef2,Vm)))
Gm = Em/(2*(1+vm))
G12 = Operaciones.division(Gf12*Gm,Operaciones.suma(Operaciones.multiplicar(Gf12,Vm),Operaciones.multiplicar(Gm,Vf)))
v12 = Operaciones.suma(Operaciones.multiplicar(vf12,Vf),Operaciones.multiplicar(vm,Vm))

#Grafico 1
plt.plot(Vf,E1)
plt.legend(["E1"])
plt.plot(0.6,E1[6], marker="o", color="blue")
plt.xlabel("Vf")
plt.title("Carlos Bustillo - Agustin Lezcano")
plt.grid()
plt.show()

#Grafico 2
plt.plot(Vf,E2)
plt.plot(Vf,G12)
plt.legend(["E2","G12"])
plt.plot(0.6,E2[6], marker="o", color="blue")
plt.plot(0.6,G12[6], marker="o", color="orange")
plt.xlabel("Vf")
plt.title("Carlos Bustillo - Agustin Lezcano")
plt.grid()
plt.show()

#Grafico 3
plt.plot(Vf,v12)
plt.legend(["v12"])
plt.plot(0.6,v12[6], marker="o", color="blue")
plt.xlabel("Vf")
plt.title("Carlos Bustillo - Agustin Lezcano")
plt.grid()
plt.show()
