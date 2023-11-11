import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

from src.model import initialize_populations, lotka_volterra_equations


def setup_sliders():
    st.sidebar.title("Configuración del modelo")

    st.sidebar.subheader("Presa")
    alpha = st.sidebar.slider("Tasa de nacimiento", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
    beta = st.sidebar.slider("Tasa de mortalidad por depredadores", min_value=0.01, max_value=1.0, value=0.02,
                             step=0.01)
    x0 = st.sidebar.number_input("Cantidad inicial", min_value=0, max_value=1000, value=40, step=1)

    st.sidebar.subheader("Depredador")
    delta = st.sidebar.slider("Tasa de nacimiento por presa consumida", min_value=0.01, max_value=1.0, value=0.01,
                              step=0.01)
    gamma = st.sidebar.slider("Tasa de mortalidad natural", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
    y0 = st.sidebar.number_input("Cantidad inicial", min_value=0, max_value=1000, value=9, step=1)

    st.sidebar.subheader("Condiciones Físicas")
    K = st.sidebar.number_input("Capacidad máxima del terreno", min_value=100, max_value=5000, value=1500, step=10)
    T = st.sidebar.number_input("Semanas", min_value=100, max_value=5000, value=1000, step=10)
    dt = st.sidebar.slider("Delta t", min_value=0.01, max_value=1.0, value=0.1, step=0.01)

    return alpha, beta, gamma, delta, x0, y0, K, T, dt


def run_simulation(alpha, beta, gamma, delta, x0, y0, K, T, dt):
    x, y, steps = initialize_populations(x0, y0, T, dt)
    for t in range(1, steps):
        x, y = lotka_volterra_equations(x, y, t, dt, alpha, beta, gamma, delta, K)
    return x, y, steps


def plot_results(x, y, T, steps, x0, y0):
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(np.linspace(0, T, steps), x, label='Presas', color='cyan')
    ax.plot(np.linspace(0, T, steps), y, label='Predadores', color='yellow')
    ax.set_xlim(0, T)
    ax.set_ylim(0, np.maximum(x0, y0) + 100)
    ax.legend()
    st.pyplot(fig)


def main():
    plt.style.use('dark_background')
    st.title('Modelo Depredador-Presa')
    st.write("Este es un modelo de depredador-presa usando ecuaciones de Lotka-Volterra.")

    alpha, beta, gamma, delta, x0, y0, K, T, dt = setup_sliders()
    x, y, steps = run_simulation(alpha, beta, gamma, delta, x0, y0, K, T, dt)
    plot_results(x, y, T, steps, x0, y0)


if __name__ == "__main__":
    main()
