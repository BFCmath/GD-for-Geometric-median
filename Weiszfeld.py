import math
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def tinh_mau(X, y1,N):
    ans = 0
    size = N
    for i in range(size):
        dis = distance(y1, X[i])
        if dis == 0:
            continue
        else:
            ans += 1 / dis
    return ans

def tinh_tu(X, y1,N):
    ans = [0,0]
    size = N
    for i in range(size):
        dis = distance(y1, X[i])
        if dis == 0:
            continue
        else:
            ans[0] += X[i][0] / dis
            ans[1] += X[i][1] / dis
    return ans

def tongchieudai(X,y_init,N,iter=100):
    y = [y_init]
    for i in range(iter):
        mau = tinh_mau(X,y[-1],N)
        tu = tinh_tu(X,y[-1],N)
        if mau ==0: break 
        y.append([tu[0]/mau,tu[1]/mau])
    sum_length = 0
    print(y[-1])
    for i in range(N):
        sum_length += distance(y[-1],X[i])
    print(sum_length)
    return y


X = []
f = open("input.txt","r")
lines = f.readlines()
N = int(lines[0])
for i in range(1,N+1): 
    x,y = lines[i].strip().split()
    X.append([float(x),float(y)])
    
y = tongchieudai(X,X[-1],N)


import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
def draw_points(X, y):
    X = np.array(X)
    fig, ax = plt.subplots()
    
    # Plot all points in X
    ax.plot(X[:, 0], X[:, 1], 'bo', label='X Points')

    # Function to update the plot for animation
    def update(frame):
        if frame < len(y):
            ax.plot(y[frame][0], y[frame][1], 'ro', label='Y Point')
        else:
            ax.plot([], [], 'ro', label='Y Point')
        ax.set_title(f'Frame {frame}/{len(y)}')
        return ax
    
    # Animate the plot
    ani = FuncAnimation(fig, update, frames=len(y)+1, interval=1000)
    plt.legend()
    plt.show()
    
draw_points(X,y)
