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
vf23=0.4

Gf12=8.96*(10**9)
Gf23=8.27*(10**9)

Vf=np.arange(0,1.1,0.1)  #Fraccion de volumen 

#Calculo
Vm = Operaciones.restar(1,Vf)
vc = Operaciones.division(vm,Vm)
Vf1 = Operaciones.division(vf12,vc)
Vf2 = Operaciones.division(vf23,vc)

E1 = Operaciones.suma(Operaciones.multiplicar(Ef1,Vf1), Operaciones.multiplicar(Em,Vm))
E2 = Operaciones.division(1,Operaciones.suma(Operaciones.division(Vf2,Ef2,True),Operaciones.division(Vm,Em,True)))

Gf = Ef1/(2*(1+vf12))
Gm = Em/(2*(1+vm))

G12 = Operaciones.division(Gf*Gm,Operaciones.suma(Operaciones.multiplicar(Gf,Vm),Operaciones.multiplicar(Gm,Vf)))
v12 = Operaciones.suma(Operaciones.multiplicar(vf12,Vf),Operaciones.multiplicar(vm,Vm))

#Grafico 1
plt.plot(Vf,E1)
plt.plot(Vf,E2)
plt.plot(Vf,G12)
plt.legend(["E1","E2","G12"])
plt.plot(0.6,E1[6], marker="o", color="blue")
plt.plot(0.6,E2[6], marker="o", color="orange")
plt.plot(0.6,G12[6], marker="o", color="green")
plt.xlabel("Vf")
plt.title("Carlos Bustillo - Agustin Lezcano")
plt.grid()
plt.show()

#Grafico 2
plt.plot(Vf,v12)
plt.legend(["v12"])
plt.plot(0.6,v12[6], marker="o", color="blue")
plt.xlabel("Vf")
plt.title("Carlos Bustillo - Agustin Lezcano")
plt.grid()
plt.show()
