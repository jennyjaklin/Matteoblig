import numpy as np
import matplotlib.pyplot as plt

from matplotlib import cm
import matplotlib.colors as colors
from matplotlib import animation

#linje1 = [0, 0, 0, 0, 0]
#linje2 = [0, 1, 1, 1, 0]
#linje3 = [0, 1, 1, 1, 0]
#linje4 = [0, 1, 1, 1, 0]
#linje5 = [0, 0, 0, 0, 0]

#Første matrise:
matrise0 = [[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]

#Relevante verdier:
size = len(matrise0)
k = 0.01
h = 1/size

#Funksjon for U_t+1, neste tidssteg i ett punkt:
def TidsstegIPunkt(matrise, x, y):
    U_x = matrise[x+1][y] + matrise[x-1][y]
    U_y = matrise[x][y+1] + matrise[x][y-1]
    U_xy = 4*matrise[x][y]
    U_t1 = ((k/(h*h)) * (U_x + U_y - U_xy)) + matrise[x][y]
    return U_t1

def TidsstegIMatrise(matrise):
    tom_matrise = matrise0
    for row in range(1, size-1):
        #print(row)
        for column in range(1, size-1):
            new_element = TidsstegIPunkt(matrise, row, column)
            #print(new_element)
            tom_matrise[row][column] = new_element
    return tom_matrise

#matrise1 = TidsstegIMatrise(matrise0)

#print(matrise1)
#for row in matrise1:
    #print(row)

#matriser_tid = []
#matriser_tid.append(matrise1)

#matrise2 = matrise1

#matrise2 = TidsstegIMatrise(matrise2)
#print(matrise2)

mange_matriser = []
mange_matriser.append(matrise0)

t_points = 10

for i in range(1, t_points):
    matrise1 = TidsstegIMatrise(matrise0)
    mange_matriser.append(matrise1)
    matrise0 = matrise1
    for element in matrise0:
        print(element)

##Koden fungerer og printer ti korrekte matriser
##Verdiene jevnes ut til rundt 0,6 fra startverdien 1

Zt = mange_matriser

X0 = np.arange(0, size*h, h)
X1 = np.arange(0, size*h, h)
X0, X1 = np.meshgrid(X0, X1)
Zt = np.array(Zt)

print(Zt[9])

def animate3d():
    animation_time_s = 1
    total_frames = t_points
    fps = int(total_frames / animation_time_s)
    

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    surface = [ax.plot_surface(X0, X1, Zt[0,:], cmap=cm.coolwarm)]
    min, max = Zt.min()/2, Zt[1,:].max()/2
    
    def init():
        ax.set_zlim(min, max)
        ax.view_init(elev=50, azim=-128)
        return surface,

    def update(frame, Zt, surface):
        surface[0].remove()
        surface[0] = ax.plot_surface(X0, X1, Zt[frame-1,:], cmap=cm.coolwarm, vmin = min, vmax = max)
        #surface[0].set_zlim(min, max)
        return surface,

    animator = animation.FuncAnimation(fig, update, init_func=init,
                                       frames=np.linspace(0, t_points, total_frames).astype(int), 
                                       fargs=(Zt, surface),
                                       interval = 100/fps)
                                       
    #animator.save("bolge.gif")
    plt.show()

##På tross av de korrekte matrisene som løser varmelikningen
##fungerer dessverre ikke animasjonen som ønsket.

""" fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot_surface(X0, X1, Zt[0], cmap=cm.coolwarm) """

animate3d()
    
    