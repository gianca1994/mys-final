#!/bin/bash

echo "Selecciona una opción:"
echo "1) Ejecutar animación"
echo "2) Ejecutar Streamlit"

read -p "Ingresa el número de la opción deseada: " opcion

case $opcion in
    1)
        echo "Ejecutando animación..."
        source env/Scripts/activate
        py animation.py
        ;;
    2)
        echo "Ejecutando Streamlit..."
        source env/Scripts/activate
        streamlit run stream.py
        ;;
    *)
        echo "Opción no válida"
        ;;
esac
