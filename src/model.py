import numpy as np


def initialize_populations(x0, y0, T, dt):
    steps = int(T / dt)
    x = np.zeros(steps)
    y = np.zeros(steps)
    x[0] = x0
    y[0] = y0
    return x, y, steps


def lotka_volterra_equations(x, y, t, dt, alpha, beta, gamma, delta, K):
    x[t] = x[t - 1] + (alpha * x[t - 1] * (1 - x[t - 1] / K) - beta * x[t - 1] * y[t - 1]) * dt
    y[t] = y[t - 1] + (delta * x[t - 1] * y[t - 1] - gamma * y[t - 1]) * dt
    return x, y
