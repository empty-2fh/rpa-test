#!/usr/bin/python
# *-* coding: utf-8 -*-

# Author: Ariel GA - def Empty(): return;

if ( __name__ == '__main__' ): exit();

class Colors:

    def __init__( self ):

        self.OK = '\033[92m'; # Verde
        self.WARNING = '\033[93m'; # Amarillo
        self.FAIL = '\033[91m'; # Rojo
        self.RESET = '\033[0m'; # Reset