## Welcome to Predator vs Dam


For the execution you must first read the file "INSTALL.md", once you have installed the libraries you must execute the file "main.py": ```python3 main.py```

- If desired, you can use the parameters ``-d or --dam``, to delimit the number of prey the model will have, ``-p or --predator`` for the number of predators, ``-c or --capcity``, for the size of the terrain and ``-w or --week`` to define the number of weeks the model will be simulated. Example:

1. ``python3 main.py -d 500 -p 10 -c 5000 -w 5``, generates a simulation of 500 prey, 10 predators, in a 5000-space terrain and for 5 weeks.
2. ``python3 main.py``, will generate a default simulation of: 500 prey, 10 predators, 5000 terrain slots and 1 week.

- Once the program is executed, it will generate a jpg file called "PredatorVsDam-Model.jpg" in the root of the directory "predator-dam" which will contain a graph detailing the simulation performed. 


Por supuesto, aquí te describo cada uno de los parámetros y condiciones iniciales en tu modelo de predador-presa mejorado con la ecuación de Lotka-Volterra:

### Parámetros:

1. **`alpha = 0.1`**: Este es el parámetro que define la tasa de nacimiento de las presas. Un valor más alto implicaría que la población de presas crece más rápidamente en ausencia de predadores.

2. **`beta = 0.02`**: Este es el parámetro que indica la tasa de mortalidad de las presas debido a la predación. Un valor más alto significa que más presas son comidas por los predadores.

3. **`gamma = 0.1`**: Este es el parámetro que define la tasa de mortalidad de los predadores. Un valor más alto significaría que los predadores mueren más rápidamente.

4. **`delta = 0.01`**: Este parámetro representa la tasa de nacimiento de nuevos predadores. Esencialmente, cuántos nuevos predadores se generan por cada presa comida. Un valor más alto aumentaría el número de predadores más rápidamente.

5. **`K = 1000`**: Este es el parámetro de la capacidad de carga del ambiente. Es el número máximo de individuos (presas, en este caso) que el ambiente puede soportar. Una vez que la población de presas se acerca a este número, su tasa de crecimiento disminuye.

### Condiciones iniciales:

1. **`x0 = 40`**: Este es el número inicial de presas en el sistema. Comienzas la simulación con 40 presas.

2. **`y0 = 9`**: Este es el número inicial de predadores en el sistema. Comienzas la simulación con 9 predadores.

### Tiempo:

1. **`T = 1000`**: Este es el tiempo total de la simulación. Estás corriendo la simulación para un total de 1000 unidades de tiempo.

2. **`dt = 0.15`**: Este es el tamaño del paso de tiempo en la simulación. Un `dt` más pequeño hará que la simulación sea más precisa pero requerirá más tiempo de cómputo. Un `dt` más grande acelerará la simulación pero podría afectar la precisión.

Espero que esta explicación aclare cada uno de los parámetros y condiciones iniciales de tu modelo. ¿Hay algo más en lo que pueda ayudarte?
