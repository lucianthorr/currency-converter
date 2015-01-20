from currency import *

def test_convert_parameters():
        assert convert([],12,"USD","USD") == 12
        assert convert([],0.12,"EUR","EUR") == 0.12
