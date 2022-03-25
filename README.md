# RPA Test

## Descripción

Proyecto RPA Test, consiste en consumir endpoints de una API tomada del sitio https://api.nasa.gov.

## API

* DONKI

> The Space Weather Database Of Notifications, Knowledge, Information (DONKI) is a comprehensive on-line tool for space weather forecasters, scientists, and the general space science community. DONKI chronicles the daily interpretations of space weather observations, analysis, models, forecasts, and notifications provided by the Space Weather Research Center (SWRC), comprehensive knowledge-base search functionality to support anomaly resolution and space science research, intelligent linkages, relationships, cause-and-effects between space weather activities and comprehensive webservice API access to information stored in DONKI. 

## Endpoints

* Solar Flare (FLR) - https://api.nasa.gov/DONKI/FLR 
* Geomagnetic Storm (GST) - https://api.nasa.gov/DONKI/GST
* Magnetopause Crossing (MPC) - https://api.nasa.gov/DONKI/MPC

## Plataformas

* Windows (Windows 10 - powershell)
* Linux (Debian 11)

## Requerimentos

* Python 3 (última versión)
* Python 3 pip (última versión)

## Instalación

```
pip3 install -r requirements.txt
```

## Uso

```
usage: main.py [-h] [-sD START_DATE] [-eD END_DATE] [-eP ENDPOINT] [-hT]

optional arguments:
  -h, --help            show this help message and exit
  -sD START_DATE, --start-date START_DATE
                        Fecha de inicio (default: 2022-3-01)
  -eD END_DATE, --end-date END_DATE
                        Fecha final (default: 2022-3-25)
  -eP ENDPOINT, --endpoint ENDPOINT
                        Hace referencia al endpoint de la API que será
                        consumida (FLR, GST, MPC)
  -hT, --historic       Muestra el historial de búsquedas

```

## Ejemplos

* Obtener eventos de bola de fuego del mes actual

    ```
    python3 main.py --endpoint 'FLR'
    ```

* Obtener eventos de tormentas geomagnéticas en un rango de fechas especificado

    ```
    python3 main.py -eP 'GST' -sD '2022-01-01' -eD '2022-02-25'
    ```

* Mostrar historial de peticiones

    ```
    python3 main.py --historic
    ```