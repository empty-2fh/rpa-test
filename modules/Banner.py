#!/usr/bin/python
# *-* coding: utf-8 -*-

# Author: Ariel GA - def Empty(): return;

if ( __name__ == '__main__' ): exit();

from .Colors import Colors

class Banner:

    def __init__( self ):

        self.c = Colors();

    def get( self ):

        print(  self.c.OK  );

        print( '██████╗ ██████╗  █████╗     ████████╗███████╗███████╗████████╗' );
        print( '██╔══██╗██╔══██╗██╔══██╗    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝' );
        print( '██████╔╝██████╔╝███████║       ██║   █████╗  ███████╗   ██║   ' );
        print( '██╔══██╗██╔═══╝ ██╔══██║       ██║   ██╔══╝  ╚════██║   ██║   ' );
        print( '██║  ██║██║     ██║  ██║       ██║   ███████╗███████║   ██║   ' );
        print( '╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝       ╚═╝   ╚══════╝╚══════╝   ╚═╝   ' );
        print( '\t  Coded by Ariel GA - def Empty(): return;\n' );