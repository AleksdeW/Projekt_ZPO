import pytest
from klasy.szufladka import Szufladka
from klasy.wyjatki import BrakProduktuException

def test_poprawne_utworzenie_szufladki():
    s = Szufladka(1, "Cola", 4.50, 3)

    assert s.numer_szufladki == 1
    assert s.nazwa_produktu == "Cola"
    assert s.cena == 4.50
    assert s.ilosc == 3
    assert s.czy_pusta() is False

    with pytest.raises(ValueError):
        Szufladka(0, "Cola", 4.50, 3)

    with pytest.raises(ValueError):
        Szufladka(-1, "Cola", 4.50, 3)

    with pytest.raises(ValueError):
        Szufladka(1, "", 4.50, 3)

    with pytest.raises(ValueError):
        Szufladka(1, " ", 4.50, 3)

    with pytest.raises(ValueError):
        Szufladka(1, "Cola", 0, 3)

    with pytest.raises(ValueError):
        Szufladka(1, "Cola", -2.0, 3)

    with pytest.raises(ValueError):
        Szufladka(1, "Cola", 4.50, -1)

    with pytest.raises(ValueError):
        Szufladka(1, "Cola", 4.50, 6)

def test_wydaj_produkt():
    s = Szufladka(1, "Cola", 4.50, 2)
    s.wydaj_produkt()

    assert s.ilosc == 1
    assert s.czy_pusta() is False

def test_wydaj_produkt_z_pustej_szufladki():
    s = Szufladka(1, "Cola", 4.50, 0)

    with pytest.raises(BrakProduktuException):
        s.wydaj_produkt()

def test_podaj_status():
    s_pelna = Szufladka(1, "Cola", 4.50, 5)
    assert s_pelna.podaj_status() == "1. Cola - 4.50 zł (5 szt.)"

    s_pusta = Szufladka(1, "Cola", 4.50, 0)
    assert s_pusta.podaj_status() == "1. Cola - brak produktu"
