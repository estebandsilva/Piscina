#!/bin/bash
directorio_buscado="Piscina"
ruta_especificada="/home/mequonic/Desktop"

ruta_directorio="$ruta_especificada/$directorio_buscado"

if [ -d "$ruta_directorio" ]; then
    echo "Se encontró el directorio '$directorio_buscado' en la ruta '$ruta_especificada'."
    # Haz algo si el directorio existe
    # ... añade aquí la rutina que deseas ejecutar
    cd $ruta_directorio
    #cd /home/mequonic/Desktop/Piscina
    git pull
    git checkout main
    python Prueba_piscinas.py
    read


else
    echo "No se encontró el directorio '$directorio_buscado' en la ruta '$ruta_especificada'."
    # Haz algo si el directorio no existe
    # ... añade aquí la otra rutina que deseas ejecutar
    git clone https://github.com/estebandsilva/Piscina

fi
