import numpy as np
import matplotlib.pyplot as plt

R = 10
L = 10
alpha = 0.5
T = 1

def input_sig(t):
    if (t % T < alpha * T):
        return 10
    else:
        return 0

def f(t, y):
  return (input_sig(t) - y*R)/L

    
    
def rk4(t0, t_end, h):
    t = np.arange(t0, t_end + h, h)
    y = np.zeros(len(t))
    y[0] = 0

    for i in range(1, len(t)):
        k1 = h * f(t[i-1], y[i-1])
        k2 = h * f(t[i-1] + h/2, y[i-1]+k1/2)
        k3 = h * f(t[i-1]+h/2, y[i-1]+k2/2)
        k4 = h * f(t[i-1]+h, y[i-1]+k3)
        y[i] = y[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6
        
    return t, y

def milne(t0, t_end, h):
    t = np.arange(t0, t_end + h, h)
    y = np.zeros(len(t))
    t00, y00 = backward(t0,t_end,h)
    y[0] = y00[0]
    y[1] = y00[1]
    y[2] = y00[2]
    y[3] = y00[3]

    for i in range(4, len(t)):
        f1 = h*f(t[i-1], y[i-1])
        f2 = h*f(t[i-2], y[i-2])
        f3 = h*f(t[i-3], y[i-3])
        y[i] = y[i-4] + 4*(2*f1 - f2 + 2*f3 )/3
        f3 = f2
        f2 = f1
        f1 = h*f(t[i], y[i])
        y[i] = y[i-2] + (f1 + 4*f2 + f3 )/3
        
    return t, y
    
def trapezoidal(t0, t_end, h):
    t = np.arange(t0, t_end + h, h)
    y = np.zeros(len(t))
    y[0] = 0

    for i in range(1, len(t)):
        y[i] = ((y[i-1]*(2*L-h*R)) + h*(input_sig(t[i])+ input_sig(t[i-1]))) / (2*L+h*R)
        
    return t, y
    
def forward(t0, t_end, h):
    t = np.arange(t0, t_end + h, h)
    y = np.zeros(len(t))
    y[0] = 0

    for i in range(1, len(t)):
        y[i] = y[i-1] + f(t[i-1], y[i-1])*h
        
    return t, y

def backward(t0,t_end, h):
    t = np.arange(t0, t_end + h, h)
    y = np.zeros(len(t))
    y[0] = 0

    for i in range(1, len(t)):
        y[i] = (y[i-1] + (h / L) * input_sig(t[i])) / (1 + (h * R / L))

    return t, y
def adam(t0,t_end, h):
    t = np.arange(t0, t_end + h, h)
    y = np.zeros(len(t))
    t00, y00 = backward(t0,t_end,h)
    
    p = np.zeros(len(t))
    y[0] = y00[0]
    y[1] = y00[1]
    y[2] = y00[2]
    y[3] = y00[3]
    for i in range(4, len(t)):
        p[i] = y[i-1] + (h/24)*( 55*f(t[i-1],y[i-1]) - 59*f(t[i-2],y[i-2]) + 37*f(t[i-3],y[i-3] - 9*f(t[i-4],y[i-4])))
        y[i] = y[i-1] + (h/24)*( 9*f(t[i],p[i]) + 19*f(t[i-1],y[i-1]) - 5*f(t[i-2],y[i-2] + f(t[i-3],y[i-3])))
    return t, y

def main():
    t0 = 0 
    y0 = 0
    t_end = 5
    h = 0.0001

    t, y = milne(t0, t_end, h)
    t1, y1 = backward(t0, t_end, h)

    with open('data.dat', 'w') as file:
        for ti, yi in zip(t, y):
            file.write(f"{ti} {yi}\n")

    plt.figure(figsize=(10, 6))
    plt.plot(t, y, label='Adam-BlahBlah')
    plt.plot(t1, y1, label='Adam-BlahBlah')
    plt.title('Adam-Blah Blah Method Simulation')
    plt.xlabel('Time')
    plt.ylabel('Solution Value')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()

