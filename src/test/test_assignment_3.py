import sys
import os

sys.path.append(os.path.abspath('C:/Users/andre/Desktop/repo_3/src/main'))

from assignment_3 import euler_method, runge_kutta_method

#1
def f(t, y):
    return t - y**2

def run_euler_method():
    t0 = 0
    y0 = 1
    t_end = 2
    iterations = 10
    h = (t_end - t0) / iterations

    euler_method(f, t0, y0, t_end, h, iterations)

#2
def rk_function(t, y):
    return t - y**2

def run_runge_kutta():
    t0 = 0
    y0 = 1
    t_end = 2
    n = 10

    runge_kutta_method(rk_function, t0, y0, t_end, n)

if __name__ == "__main__":
    print("Running Euler Method:")
    run_euler_method()
    
    print("\nRunning Runge-Kutta Method:")
    run_runge_kutta()