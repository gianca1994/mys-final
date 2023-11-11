import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from dotenv import load_dotenv
from src.model import initialize_populations, lotka_volterra_equations


def load_environment_variables():
    load_dotenv()
    environment_variables = {
        "alpha": float(os.getenv("DAM_BIRTH_RATE")),
        "beta": float(os.getenv("DAM_MORTALITY_RATE")),
        "gamma": float(os.getenv("PREDATOR_MORTALITY_RATE")),
        "delta": float(os.getenv("PREDATOR_BIRTH_RATE")),
        "K": int(os.getenv("TERRAIN_MAX_CAP")),
        "x0": int(os.getenv("DAM_AMOUNT")),
        "y0": int(os.getenv("PREDATOR_AMOUNT")),
        "T": int(os.getenv("WEEKS")),
        "dt": float(os.getenv("DELTA_T"))
    }
    return environment_variables


def setup_figure(x0, y0, T):
    fig, ax = plt.subplots()
    ax.set_xlim(0, T)
    ax.set_ylim(0, np.maximum(x0, y0) + 100)
    return fig, ax


def init(line1, line2):
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2


def update_animation(t, lines, populations, params, step_size):
    x, y = lotka_volterra_equations(populations["x"], populations["y"], t, params["dt"], params["alpha"],
                                    params["beta"], params["gamma"], params["delta"], params["K"])

    populations["x"], populations["y"] = x, y
    lines["line1"].set_data(np.linspace(0, t * step_size, t + 1), x[:t + 1])
    lines["line2"].set_data(np.linspace(0, t * step_size, t + 1), y[:t + 1])
    return lines["line1"], lines["line2"]


def main():
    params = load_environment_variables()

    x, y, steps = initialize_populations(params["x0"], params["y0"], params["T"], params["dt"])

    fig, ax = setup_figure(params["x0"], params["y0"], params["T"])

    line1, = ax.plot([], [], label='Presas')
    line2, = ax.plot([], [], label='Predadores')

    ax.legend()

    lines = {"line1": line1, "line2": line2}

    FuncAnimation(fig, update_animation, fargs=(lines, {"x": x, "y": y}, params, params["dt"]), frames=range(1, steps),
                  init_func=lambda: init(line1, line2), blit=True, interval=1, repeat=True)

    plt.show()


if __name__ == "__main__":
    main()
