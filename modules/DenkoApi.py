#!/usr/bin/python
# *-* coding: utf-8 -*-

# Author: Ariel GA - def Empty(): return;

if ( __name__ == '__main__' ): exit();

import requests;

class DenkoApi:

    def __init__( self ):

        # API KEY

        self.__api_key = "DEMO_KEY";

        # Endpoints de la API

        self.__endpoints = { 
            
            # Solar Flare

            'FLR' : {
                
                        'url' : 'https://api.nasa.gov/DONKI/FLR',
                        'params' : { 'startDate' : '', 'endDate' : '', 'api_key' : self.__api_key  }
                        
                    },

            # Geomagnetic Storm

            'GST' : {
                
                        'url' : 'https://api.nasa.gov/DONKI/GST',
                        'params' : { 'startDate' : '', 'endDate' : '', 'api_key' : self.__api_key  }
                        
                    },

            # Magnetopause Crossing

            'MPC' : {
                
                        'url' : 'https://api.nasa.gov/DONKI/MPC',
                        'params' : { 'startDate' : '', 'endDate' : '', 'api_key' : self.__api_key  }
                        
                    },
            
        };

    # Realizar petición GET al endpoint indicado

    def __request( self, url, params ): 
    
        return requests.get( url, params );

    # Petición a los endpoints Solar Flare (FLR), Geomagnetic Storm(GST), Magnetopause Crossing (MPC)

    def standardEP( self, startDate = '', endDate = '', endpoint = 'FLR' ):

        # Seteo de parámetros

        self.__endpoints[ endpoint ][ 'params' ].update( 
            
            { 
            
                'startDate' : startDate, 
                'endDate' : endDate 
                
            } );

        # Realizar petición

        return self.__request( **self.__endpoints[ endpoint ] );