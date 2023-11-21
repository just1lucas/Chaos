import matplotlib.pyplot as plt
import numpy as np

def Lorenzgleichung(xyz,*,s=10,r=28,b=2.667):
    X,Y,Z=xyz
    x_1 = s*(Y-X)
    y_1 = r*X-Y-X*Z
    z_1 = X*Y-b*Z
    return np.array([x_1,y_1,z_1])



dt = 0.001
n = 50000 #s

X_0 = 0.
Y_0 = 1
Z_0_a = 1.5
Z_0_b = 1.50003

xyz_list_1 = np.empty((n + 1, 3))
xyz_list_2 = np.empty((n+1,3))
xyz_list_1[0]=[X_0,Y_0,Z_0_a]
xyz_list_2[0]=[X_0,Y_0,Z_0_b]

N_list= np.empty((n+1,1))

for i in range(0,n):
    #print(xyz_list [i])

    xyz_list_1[i + 1] = xyz_list_1[i] + Lorenzgleichung(xyz_list_1[i]) * dt
    xyz_list_2[i + 1] = xyz_list_2[i] + Lorenzgleichung(xyz_list_2[i]) * dt

    N_list[i + 1]=i + 1

x_1=xyz_list_1[:,0]
x_2=xyz_list_2[:,0]

x=(x_2-x_1)
plt.figure()
#plt.plot(N_list/3600,x_1)
plt.plot(N_list/3600,x)
plt.ylabel("X(t)")
plt.xlabel("t[h]")
plt.show()

ax = plt.figure().add_subplot(projection='3d')

ax.plot(*xyz_list_1.T, lw=0.5)
ax.plot(*xyz_list_2.T, lw=0.5)
ax.set_xlabel("X(t)")
ax.set_ylabel("Y(t)")
ax.set_zlabel("Z(t)")
ax.set_title("Lorenz Attractor")
plt.show()

