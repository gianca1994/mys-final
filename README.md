# Modelo Depredador-Presa con Lotka-Volterra

## Descripción

Este proyecto simula la interacción entre depredadores y sus presas a través del tiempo, utilizando las conocidas ecuaciones de Lotka-Volterra. Estas ecuaciones representan un modelo matemático de la dinámica biológica de dos especies interactivas, una como presa y la otra como depredador. El modelo ilustra cómo las poblaciones de cada especie cambian con el tiempo, influenciadas por las tasas naturales de nacimiento y muerte, así como por la capacidad del entorno para sostener a la población de presas.

## Variables de Entorno

El modelo utiliza una serie de variables de entorno que permiten personalizar la simulación:

### Presa
- `DAM_BIRTH_RATE`: Tasa de nacimiento de las presas (`0.1`). Representa la rapidez con que la población de presas puede aumentar en ausencia de depredadores.
- `DAM_MORTALITY_RATE`: Tasa de mortalidad de las presas debido a la depredación (`0.02`). Indica cuántas presas son capturadas y consumidas por los depredadores.
- `DAM_AMOUNT`: Cantidad inicial de presas en el modelo (`40`). Es el punto de partida para la población de presas.

### Depredador
- `PREDATOR_BIRTH_RATE`: Tasa de nacimiento de los depredadores (`0.01`). Esta tasa está ligada al éxito de los depredadores en la captura de las presas.
- `PREDATOR_MORTALITY_RATE`: Tasa de mortalidad natural de los depredadores (`0.1`). Refleja las pérdidas en la población de depredadores debido a muertes naturales.
- `PREDATOR_AMOUNT`: Cantidad inicial de depredadores (`9`). Es la cantidad de depredadores con la que comienza la simulación.

### Condiciones Físicas
- `TERRAIN_MAX_CAP`: Capacidad máxima del terreno (`1500`). Se refiere al límite de la población de presas que el entorno puede soportar.
- `WEEKS`: Duración de la simulación en semanas (`1000`). Define el período de tiempo sobre el cual se extiende la simulación.
- `DELTA_T`: Incremento de tiempo para cada paso de la simulación (`0.1`). Determina la granularidad de la simulación temporal.

## Instalación

Para instalar y configurar el entorno necesario para ejecutar las simulaciones, sigue estos pasos:

1. Descarga o clona el repositorio en tu máquina local.
2. Navega al directorio del proyecto desde tu terminal.
3. Ejecuta el script `install.sh` con el siguiente comando:

    ```
    ./install.sh
    ```

    Este script realizará los siguientes pasos:
    - Creará un entorno virtual de Python.
    - Activará el entorno virtual.
    - Instalará todas las dependencias requeridas que se enumeran en `requirements.txt`.

Una vez finalizada la instalación, estarás listo para ejecutar las simulaciones.


## Ejecución

Una vez que hayas instalado todas las dependencias y configurado tu entorno, puedes ejecutar el proyecto de dos maneras:

1. Como una animación gráfica que muestra la dinámica entre depredadores y presas.
2. A través de una aplicación interactiva con Streamlit que permite ajustar parámetros y visualizar resultados en tiempo real.

Para facilitar la ejecución, utiliza el script `run.sh` con el siguiente comando:

```
./run.sh
```

Sigue las instrucciones en pantalla para seleccionar la simulación deseada:

* Elige 1 para ejecutar la animación.
* Elige 2 para lanzar la aplicación Streamlit.
* 
Debes asegurarte de que run.sh tenga permisos de ejecución antes de intentar usarlo. Puedes conceder permisos de ejecución con el comando `chmod +x run.sh`.