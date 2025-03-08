import numpy as np

#1
def f(t, y):
  return t - y**2

def euler_method(f, t0, y0, t_end, h, iterations):
  t = t0
  y = y0
  t_values = [t]
  y_values = [y]

  print(f"Initial: t = {t:.2f}, y = {y:.4f}")

  for i in range(iterations):
      slope = f(t, y)
      y = y + h * slope
      t = t + h
      t_values.append(t)
      y_values.append(y)
    
      print(f"Iteration {i+1}: t = {t:.2f}, y = {y:.4f}")

  return t_values, y_values

#2
def runge_kutta_method(f, t0, y0, t_end, n):
  h = (t_end - t0) / n

  t_values = [t0]
  y_values = [y0]
  
  print(f"Initial: t = {t0:.2f}, y = {y0:.4f}")

  for i in range(n):
      t = t_values[-1]
      y = y_values[-1]

      k1 = h * f(t, y)
      k2 = h * f(t + h / 2, y + k1 / 2)
      k3 = h * f(t + h / 2, y + k2 / 2)
      k4 = h * f(t + h, y + k3)

      y_new = y + (k1 + 2*k2 + 2*k3 + k4) / 6

      t_values.append(t + h)
      y_values.append(y_new)

      print(f"Iteration {i+1}: t = {t + h:.2f}, y = {y_new:.4f}")