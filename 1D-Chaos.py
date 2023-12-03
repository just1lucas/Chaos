#Import
import numpy as np
import random as rnd
import matplotlib.pyplot as plt

#Definition Diferentialgleichung
def det_Gleichung(x_0):
    x_1=3.95*x_0*np.sqrt((1-x_0)**2)
    return x_1

#Angabe Parameter
x0=0.1
n=100
n_p=1000

#Erstellen leerer Listen
rnd_array   =   np.empty((n+2 ,1))
rnd_array_p =   np.empty((n_p+1,1))
det_array   =   np.empty((n+2 ,1))
det_array_p =   np.empty((n_p+2,1))
N_array     =   np.empty((n+2 ,1))

det_array   [0]=[x0]
det_array_p [0]=[x0]



#Numerische Lösung Berechnen und hinzufügen in Liste
for i in range(0,n+1):

    det_array[i+1]=(det_Gleichung(det_array[i]))
    rnd_array[i+1]=rnd.uniform(0,1)
    N_array[i+1]= i+1

#Diagram 1____ Vergleich Chaos vs Zufall (ohne Titel)

plt.figure(figsize=(12,6))

plt.subplot(121)
plt.plot(N_array,rnd_array)
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(122)
plt.plot(N_array,det_array)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

#Diagram 2____ Vergleich Chaos vs Zufall (mit Titel)

plt.figure(figsize=(12,6))

plt.subplot(121)
plt.plot(N_array,rnd_array)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Random: y= rnd(x)")

plt.subplot(122)
plt.plot(N_array,det_array)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Chaos: y=3.95* x0 * sqrt((1-x0)**2)")
plt.show()



#Phasendiagramm Berechnung

for i in range(0,n_p):
    det_array_p[i+1]=(det_Gleichung(det_array_p[i]))
    rnd_array_p[i+1]=rnd.uniform(0,1)

det_list_0=det_array_p[:-1,0].tolist()
det_list_1=det_array_p[:-1,0].tolist()

rnd_list_0=rnd_array_p[:-1,0].tolist()
rnd_list_1=rnd_array_p[:-1,0].tolist()

det_list_0.pop(0)
det_list_1.pop(len(det_list_1)-1)

rnd_list_0.pop(0)
rnd_list_1.pop(len(rnd_list_1)-1)

#Diagram 2____ Phasendiagram

plt.figure(figsize=(12,6))

plt.subplot(122)
plt.plot(det_list_1,det_list_0,".")
plt.title("Diferentialgleichung")
plt.ylabel("x[n+1]")
plt.xlabel("x[n]")
plt.xlim(0,1.01)
plt.ylim(0,1.01)

plt.subplot(121)
plt.plot(rnd_list_1,rnd_list_0,".")
plt.title("Random")
plt.ylabel("x[n+1]")
plt.xlabel("x[n]")
plt.xlim(0,1.01)
plt.ylim(0,1.01)
plt.show()

print("Finish him")