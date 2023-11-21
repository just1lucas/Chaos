import numpy as np
import random as rnd
import matplotlib.pyplot as plt
def det_Gleichung(x_0):
    x_1=3.95*x_0*np.sqrt((1-x_0)**2)
    return x_1

x0=0.1
n=100
n_p=1000

rnd_array   =   np.empty((n+2 ,1))
rnd_array_p =   np.empty((n_p+1,1))
det_array   =   np.empty((n+2 ,1))
det_array_p =   np.empty((n_p+2,1))
N_array     =   np.empty((n+2 ,1))

det_array   [0]=[x0]
det_array_p [0]=[x0]




for i in range(0,n+1):

    det_array[i+1]=(det_Gleichung(det_array[i]))
    rnd_array[i+1]=rnd.uniform(0,1)
    N_array[i+1]= i+1

plt.figure()
ax1=plt.subplot(121)
ax1.plot(N_array,rnd_array)
ax2=plt.subplot(122)
ax2.plot(N_array,det_array)
plt.show()


for i in range(0,n_p):
    det_array_p[i+1]=(det_Gleichung(det_array_p[i]))
    rnd_array_p[i+1]=rnd.uniform(0,1)

det_list_0=det_array_p[:,0].tolist()
det_list_1=det_array_p[:,0].tolist()

rnd_list_0=rnd_array_p[:,0].tolist()
rnd_list_1=rnd_array_p[:,0].tolist()

det_list_0.pop(0)
det_list_1.pop(len(det_list_1)-1)

rnd_list_0.pop(0)
rnd_list_1.pop(len(rnd_list_1)-1)

ax3=plt.subplot(122)
ax3.plot(det_list_1,det_list_0,".")
ax4=plt.subplot(121)
ax4.plot(rnd_list_1,rnd_list_0,".")
plt.show()
print("Finish him")