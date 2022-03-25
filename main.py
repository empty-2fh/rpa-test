#!/usr/bin/python
# *-* coding: utf-8 -*-

# Author: Ariel GA - def Empty(): return;

import argparse
from datetime import datetime, date

from modules.DenkoApi import DenkoApi
from modules.Colors import Colors
from modules.Layouts import Layouts
from modules.Banner import Banner

from modules.DataBase import DataBase

# Fecha actual (Se utilizará como fecha por defecto para el endpoint)

today = date.today();

def consoleArgs():

    global today

    # Control de argumentos por consola

    parser = argparse.ArgumentParser(); 

    parser.add_argument( '-sD', '--start-date', 
        
        type = str, 
        default = f'{today.year}-{today.month}-01',
        help = f'Fecha de inicio (default: {today.year}-{today.month}-01)' 
        
        );

    parser.add_argument( '-eD', '--end-date', 
    
        type = str, 
        default = f'{today.year}-{today.month}-{today.day}',
        help = f'Fecha final (default: {today.year}-{today.month}-{today.day})'
        
        );

    parser.add_argument( '-eP', '--endpoint', 
    
        type = str,
        help = 'Hace referencia al endpoint de la API que será consumida (FLR, GST, MPC)'
        
        );

    parser.add_argument( '-hT', '--historic', 
    
        action = 'store_true',
        default = False,
        help = 'Muestra el historial de búsquedas'

        );

    return parser;

def main():

    global today;
 
    # Colores

    c = Colors();

    # Formatos para las response de los endpoints

    layouts = Layouts();

    # Banner

    banner = Banner();

    banner.get();

    # Mostrar de color amarillo el menú de ayuda XD

    print( c.WARNING, end = '' );

    # Argumentos

    parser = consoleArgs();

    args = parser.parse_args();

    if ( ( not args.historic ) and ( not args.endpoint ) ): 

        parser.print_help();
        print();
        exit();

    # Conexión a la BD

    db = DataBase();

    denki_db = db.connect();

    # Especificar colección de la BD

    historic = denki_db[ 'Historial' ];

    # Instancia de la clase DenkiApi

    api = DenkoApi();

    # Mostrar historial de peticiones

    if ( args.historic ):

        hist_length = historic.count_documents( {} );

        if ( hist_length > 0 ):

            hist = historic.find();

            layouts.historic( hist );
                        
            print( c.OK + 'Total de peticiones realizadas: ' + c.RESET + str( hist_length ) );
            print();
            exit();

        else:

            print( c.WARNING + 'Aún no ha realizado ninguna petición!' + c.RESET );
            exit();

    # Validación de formato de fechas ( YY/MM/DD )

    try:

        datetime.strptime( args.start_date, '%Y-%m-%d' );
        datetime.strptime( args.end_date, '%Y-%m-%d' );

        if ( args.start_date > args.end_date  ): 

            print( c.WARNING + 'Por favor, verifique que la fecha inicial no sea mayor que la fecha final' + c.RESET );
            exit();

    except:

        print( c.WARNING + 'Por favor, verifique que el formato de las fechas sea el adecuado (YY/MM/DD)!' + c.RESET );
        exit();

    # Control de excepciones al momento de realizar la petición al endpoint

    try:

        # Validación del endpoint indicado

        if ( args.endpoint in [ 'FLR', 'GST', 'MPC' ]):

            response = api.standardEP( args.start_date, args.end_date, args.endpoint );

        else:

            print( c.WARNING + 'El endpoint indicado no es válido!' + c.RESET );
            exit();

        # Arreglo de datos formateados

        data_rlv = [];

        # Respuesta obtenida con éxito

        if ( response.status_code == 200 ):

            # Verificar que la respuesta no sea nula

            data_length = len( response.text );

            if ( data_length <= 0 ):

                print( c.FAIL + 'No se encontraron registros de eventos!' + c.RESET );
                exit();

            # Mostrar Layout del endpoint Solar Flare

            if ( args.endpoint == 'FLR' ):
                
                data_rlv = layouts.FLR( args.start_date, args.end_date, response.json() );

            # Mostrar Layout del endpoint Geomagnetic Storm

            elif ( args.endpoint == 'GST' ):

                data_rlv = layouts.GST( args.start_date, args.end_date, response.json() );

            # Mostrar Layout del endpoint Magnetopause Crossing

            elif ( args.endpoint == 'MPC' ):

                data_rlv = layouts.MPC( args.start_date, args.end_date, response.json() );

            else:

                print( c.WARNING +  'El endpoint no pudo ser identificado' + c.RESET );
                exit();

            print( c.OK + 'Total de eventos registrados: ' + c.RESET + str( len( response.json() )) );
            print();

            # Guardar información de la petición realizada

            try:

                historic.insert_one( { 'date' : datetime.now(), 'endpoint' : args.endpoint, 'data' : data_rlv } );

            except:

                print( c.FAIL + 'Ha ocurrido un error al guardar el historial en la BD!' + c.RESET );
                exit();

        # Límite de peticiones alcanzado

        elif ( response.status_code == 429 ):

            print( c.WARNING + 'Limite de peticiones alcanzado, inténtelo luego!' + c.RESET );

        # Algún otro error XD

        else:

            print( c.FAIL + 'Ha ocurrido un error al tratar de conectar con el endpoint!' + c.RESET );
            exit();

    except:

        print( c.FAIL + 'Ha ocurrido un error inesperado!' + c.RESET );

if( __name__ == '__main__' ) : main();