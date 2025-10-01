import pytest

from main import somme
#from main import get_weather

#def test_somme():
   # assert somme(2,3) == 10
  #  assert somme(2,5) == 7

#def test_get_weather():
#    assert get_weather(25)=="cold"
 #   assert get_weather(35)=="hot"
@pytest.fixture
def Nbre_Liste():
    return [
        (2, 5, 10),
        (-1 , 1, 0),
        (0, 0, 0),
        (1, 0, 0),
    ]
def test_multiple(Nbre_Liste):
    for a, b, expected in Nbre_Liste :
        assert somme(a,b) == expected