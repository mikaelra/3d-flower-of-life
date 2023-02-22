from functions.Sphere.sphere import Sphere
from matplotlib.pyplot import *

# Here shouldcode for a plot with the 3d seed of life,
# flower of life and hopefully Star-tetrahedron/Merkabah be

# Flower of life

fig = figure()
ax = fig.add_subplot(projection='3d')
ax.text(0,0,1.5,s="Star Tetrahedron/Merkabah")

x, y, z = Sphere()
print(len(x))

for i in range(25):
    s = "$" + str(i) + "$"
    ax.scatter(x[i], y[i], z[i], marker=s)

# Points for tetrahedron 1
# 6, 14, 16, 18

# Points for tetrahedron 2
# 20, 11, 7, 9

print('x,y,z for tetrahedron 1:')
print(str(x[6]) + ', ' + str(y[6]) + ', ' + str(z[6]))
print(str(x[14]) + ', ' + str(y[14]) + ', ' + str(z[14]))
print(str(x[16]) + ', ' + str(y[16]) + ', ' + str(z[16]))
print(str(x[18]) + ', ' + str(y[18]) + ', ' + str(z[18]))

print('x,y,z for tetrahedron 2:')
print(str(x[20]) + ', ' + str(y[20]) + ', ' + str(z[20]))
print(str(x[11]) + ', ' + str(y[11]) + ', ' + str(z[11]))
print(str(x[7]) + ', ' + str(y[7]) + ', ' + str(z[7]))
print(str(x[9]) + ', ' + str(y[9]) + ', ' + str(z[9]))

xt1 = [x[6], x[14], x[16], x[6], x[18], x[6], x[18], x[14], x[16], x[18]]
yt1 = [y[6], y[14], y[16], y[6], y[18], y[6], y[18], y[14], y[16], y[18]]
zt1 = [z[6], z[14], z[16], z[6], z[18], z[6], z[18], z[14], z[16], z[18]]

xt2 = [x[20], x[11], x[7], x[20], x[9], x[20], x[9], x[11], x[7], x[9]]
yt2 = [y[20], y[11], y[7], y[20], y[9], y[20], y[9], y[11], y[7], y[9]]
zt2 = [z[20], z[11], z[7], z[20], z[9], z[20], z[9], z[11], z[7], z[9]]


plot(xt1,yt1,zt1)
plot(xt2,yt2,zt2)

show()