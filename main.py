from functions.Sphere.sphere import Sphere
from matplotlib.pyplot import *

# Here shouldcode for a plot with the 3d seed of life,
# flower of life and hopefully Star-tetrahedron/Merkabah be

# Flower of life

fig = figure()
ax = fig.add_subplot(projection='3d')
ax.text(0,0,1.5,s="Sphere1")

x, y, z = Sphere()

for i in range(len(x)):
    ax.scatter(x[i], y[i], z[i])

show()

fig = figure()
ax = fig.add_subplot(projection='3d')
ax.text(0,0,2.5,s="SeedSpheres")

x, y, z = Sphere()

for i in range(len(x)):
    ax.scatter(x[i], y[i], z[i])
    xi, yi, zi = Sphere(x0 = x[i], y0 = y[i], z0 = z[i], r=1,n=6)
    for j in range(len(xi)):
        ax.scatter(xi[j], yi[j], zi[j])

show()