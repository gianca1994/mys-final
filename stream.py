import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

plt.style.use('dark_background')

st.title('Modelo Depredador-Presa')
st.write("Este es un modelo de depredador-presa usando ecuaciones de Lotka-Volterra.")

st.sidebar.title("Configuración del modelo")

st.sidebar.subheader("Presa")
alpha = st.sidebar.slider("Tasa de nacimiento", min_value=0.01, max_value=1.0, value=0.1, step=0.01)
beta = st.sidebar.slider("Tasa de mortalidad por depredadores", min_value=0.01, max_value=1.0, value=0.02, step=0.01)
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

steps = int(T / dt)

x = np.zeros(steps)
y = np.zeros(steps)
x[0] = x0
y[0] = y0

for t in range(1, steps):
    x[t] = x[t - 1] + (alpha * x[t - 1] * (1 - x[t - 1] / K) - beta * x[t - 1] * y[t - 1]) * dt
    y[t] = y[t - 1] + (delta * x[t - 1] * y[t - 1] - gamma * y[t - 1]) * dt

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(np.linspace(0, T, steps), x, label='Presas', color='cyan')
ax.plot(np.linspace(0, T, steps), y, label='Predadores', color='yellow')
ax.set_xlim(0, T)
ax.set_ylim(0, np.maximum(x0, y0) + 100)
ax.legend()

st.pyplot(fig)
