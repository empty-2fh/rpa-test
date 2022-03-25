#!/usr/bin/python
# *-* coding: utf-8 -*-

# Author: Ariel GA - def Empty(): return;

if ( __name__ == '__main__' ): exit();

from pymongo import MongoClient

from .Colors import Colors

class DataBase:

    def __init__( self ):

        # Credenciales del Cluster MongoAtlas

        self.__user = 'empty-2fh';
        self.__passw = 'o3urKpZA8XUaqXx1';

        # Nombre de la BD

        self.__db_name = 'DenkoApi';

        # Cadena de conexión

        self.__url = f'mongodb+srv://{ self.__user }:{ self.__passw }@emptycluster.lraki.mongodb.net/myFirstDatabase?retryWrites=true&w=majority';

    def connect( self ):

        try:

            cluster = MongoClient( self.__url );

        except:

            c = Colors();

            print( c.FAIL + 'Ha ocurrido un error al tratar de conectar con la base de datos!' )
            exit();

        return cluster[ self.__db_name ];