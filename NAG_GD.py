import numpy as np 

X = []
# read input from input.txt 
# the first line is N - the number of coordinates line
# each line in the next N lines is "x y" without the quotes
f = open("input.txt","r")
lines = f.readlines()
N = int(lines[0])
for i in range(1,N+1): 
    x,y = lines[i].strip().split()
    X.append([float(x),float(y)])

X = np.asarray(X)
y_init = X[-1]
N,d = X.shape

# calculate gradicent of function f 

def g_funct(y, x_i):
    b = y - x_i
    return np.linalg.norm(b, 2)

def f_funct(y,X):
    ans =0 
    for i in range(N):
        x_i = X[i,:]
        ans += g_funct(y,x_i)
    return ans 

def grad_g(y,x_i):
    ans = [0,0]
    g = g_funct(y,x_i)
    if(g==0): return np.asarray(ans)
    ans[0] = (y[0]-x_i[0])/g
    ans[1] = (y[1]-x_i[1])/g
    return np.asarray(ans)

def grad_f(y,X):
    ans = np.asarray([0,0]).astype(float)
    for i in range(N):
        x_i = X[i,:]
        ans += grad_g(y,x_i)
    return ans

def gradient_decent(y_init,X,iter = 100,iter_print = 10,eta=0.5,gamma=1):
    y = [y_init]
    v = [np.zeros_like(y[-1])]
    i = 0
    for i in range(iter):
        # use NAG gradient decent 
        v_new = gamma*v[-1] + eta*grad_f(y[-1]-gamma*v[-1],X)
        y_new = y[-1] - v_new
        y.append(y_new)    
        v.append(v_new)    
        if (i+1)%iter_print==0:
            print(f"iter: {i+1} loss: {f_funct(y_new,X)}")
        if np.linalg.norm(grad_f(y_new,X))<1e-6: break
    return (y,i+1)
            
(y,iter) = gradient_decent(y_init,X,iter_print=1,eta=0.1,gamma=1)
print(y[-1])
print(f"after {iter}")

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def draw_points(X, y):
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
        

        