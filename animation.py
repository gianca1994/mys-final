import os

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dotenv import load_dotenv

load_dotenv()

alpha = float(os.getenv("DAM_BIRTH_RATE"))
beta = float(os.getenv("DAM_MORTALITY_RATE"))
gamma = float(os.getenv("PREDATOR_MORTALITY_RATE"))
delta = float(os.getenv("PREDATOR_BIRTH_RATE"))
K = int(os.getenv("TERRAIN_MAX_CAP"))

x0 = int(os.getenv("DAM_AMOUNT"))
y0 = int(os.getenv("PREDATOR_AMOUNT"))

T = int(os.getenv("WEEKS"))
dt = float(os.getenv("DELTA_T"))
steps = int(T / dt)

x = np.zeros(steps)
y = np.zeros(steps)
x[0] = x0
y[0] = y0

fig, ax = plt.subplots()
line1, = ax.plot([], [], label='Presas')
line2, = ax.plot([], [], label='Predadores')
ax.set_xlim(0, T)
ax.set_ylim(0, np.maximum(x0, y0) + 100)
ax.legend()


def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


def update(t):
    x[t] = x[t - 1] + (alpha * x[t - 1] * (1 - x[t - 1] / K) - beta * x[t - 1] * y[t - 1]) * dt
    y[t] = y[t - 1] + (delta * x[t - 1] * y[t - 1] - gamma * y[t - 1]) * dt

    line1.set_data(np.linspace(0, t * dt, t), x[:t])
    line2.set_data(np.linspace(0, t * dt, t), y[:t])
    return line1, line2


ani = FuncAnimation(fig, update, frames=range(1, steps), init_func=init, blit=True, interval=1, repeat=True)

plt.show()
