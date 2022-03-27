#!/usr/bin/python
# *-* coding: utf-8 -*-

# Author: Ariel GA - def Empty(): return;

if ( __name__ == '__main__' ): exit();

from .Colors import Colors

class Layouts:

    def __init__( self ):

        self.c = Colors();

    # Formato para la response del endpoint Solar Flame (FLR)

    def FLR( self, start_date, end_date, response ):

        print( self.c.OK + f'Bolas de fuego - Listado de eventos({ self.c.RESET }{ start_date } - { end_date }{ self.c.OK })' + self.c.RESET );
        print();

        obj_arr = [];

        for obj in response: 

            print( self.c.OK + 'ID: ' + self.c.RESET + str( obj[ 'flrID' ] ) );
            print( self.c.OK + 'Instrumentos utilizados: ' + self.c.RESET + str( obj[ 'instruments' ][ 0 ][ 'displayName' ] ) );
            print( self.c.OK + 'Hora de inicio: ' + self.c.RESET + str( obj[ 'beginTime' ] ) );
            print( self.c.OK + 'Hora pico: ' + self.c.RESET + str( obj[ 'peakTime' ] ) );
            print( self.c.OK + 'Hora de finalización: ' + self.c.RESET + str( obj[ 'endTime' ] ) );
            print( self.c.OK + 'Más detalles: ' + self.c.RESET + str( obj[ 'link' ] ) );
            print();

            obj_arr.append( 
                
                { 
                    
                    'flrID' : obj[ 'flrID' ], 
                    'instruments' : obj[ 'instruments' ][ 0 ][ 'displayName' ],
                    'beginTime' : obj[ 'beginTime' ],    
                    'peakTime' : obj[ 'peakTime' ],
                    'endTime' : obj[ 'endTime' ],
                    'link' : obj[ 'link' ]

                } );

        return obj_arr;


    # Formato para la response del endpoint Geomagnetic Storm (GST)

    def GST( self, start_date, end_date, response ):

        print( self.c.OK + f'Tormentas geomagnéticas - Listado de eventos({ self.c.RESET }{ start_date } - { end_date }{ self.c.OK })' + self.c.RESET );
        print();

        obj_arr = [];

        for obj in response:

            print( self.c.OK + 'Id: ' + self.c.RESET + str( obj[ 'gstID' ] ) );
            print( self.c.OK + 'Hora de inicio: ' + self.c.RESET + str( obj[ 'startTime' ] ) );
            print( self.c.OK + 'Hora de observación: ' + self.c.RESET + str( obj[ 'allKpIndex' ][ 0 ][ 'observedTime' ] ) );
            print( self.c.OK + 'Más detalles: ' + self.c.RESET + str( obj[ 'link' ] ) );
            print();

            obj_arr.append( 
                    
                { 
                    
                    'gstID' : obj[ 'gstID' ], 
                    'startTime' : obj[ 'startTime' ],
                    'observedTime' : obj[ 'allKpIndex' ][ 0 ][ 'observedTime' ],
                    'link' : obj[ 'link' ]

                } );

        return obj_arr;


    # Formato para la response del endpoint Magnetopause Crossing (MPC)

    def MPC( self, start_date, end_date, response ):

        print( self.c.OK + f'Cruce de Magnetopausas - Listado de eventos({ self.c.RESET }{ start_date } - { end_date }{ self.c.OK })' + self.c.RESET );
        print();
        
        obj_arr = [];

        for obj in response:
            
            print( self.c.OK + 'Id: ' + self.c.RESET + str( obj[ 'mpcID' ] ) );
            print( self.c.OK + 'Instrumentos utilizados: ' + self.c.RESET + str( obj[ 'instruments' ][ 0 ][ 'displayName' ] ) );
            print( self.c.OK + 'Hora del evento: ' + self.c.RESET + str( obj[ 'eventTime' ] ) );
            print( self.c.OK + 'Más detalles: ' + self.c.RESET + str( obj[ 'link' ] ) );
            print();

        
            obj_arr.append( 
                    
                { 
                    
                    'gstID' : obj[ 'mpcID' ], 
                    'startTime' : obj[ 'eventTime' ],
                    'link' : obj[ 'link' ]

                } );

        return obj_arr;

    # Formato para el historial de responses

    def historic( self, objcts ):

        print( self.c.OK + 'Historial de peticiones\n' + self.c.RESET );

        for obj in objcts:

            print( self.c.OK + 'Fecha: ' + self.c.RESET + str( obj[ 'date' ] ) );
            print( self.c.OK + 'EndPoint: ' + self.c.RESET + str( obj[ 'endpoint' ] ) );
            print( self.c.OK + 'Datos: ' + self.c.RESET + str( obj[ 'data' ] ) );
            print();