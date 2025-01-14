## Brian Blaylock
## February 9, 2022

"""
Tests for downloading GFS model
"""

from herbie.archive import Herbie

def test_gefs():
    H = Herbie("2017-03-14", model="gefs", fxx=12, member=0, variable_level='tmp_2m')

    assert H.grib, "GEFS grib2 file not found"
    assert H.idx, "GEFS index file not found"
