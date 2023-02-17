# imports
import math
from matplotlib.pyplot import *

# functions
def Sphere (x0 = 0, y0 = 0, z0 = 0, r = 1, n = 6):
    # Returns x,y,z coordinates for a sphere with radius (r)
    # from point (x0,y0,z0)

    x = [x0]
    y = [y0]
    z = [z0]

    # Math from
    # https://math.stackexchange.com/questions/805665/n-points-in-a-circle-around-a-point-on-a-sphere
    for i in range(n):
        thetai = 2*i*math.pi/n
        for j in range(n):
            thetaj = 2*j*math.pi/n
            x.append(x0 + r*math.sin(thetai)*math.cos(thetaj))
            y.append(y0 + r*math.sin(thetai)*math.sin(thetaj))
            z.append(z0 + r*math.cos(thetai))
            
    
    return [x, y, z]

# main
if __name__ == "__main__":

    fig = figure()
    ax = fig.add_subplot(projection='3d')
    ax.text(0,0,1.5,s="Sphere1")

    x, y, z = Sphere()

    for i in range(len(x)):
        ax.scatter(x[i], y[i], z[i])
    show()