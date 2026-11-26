import pytest
from klasy.baza_szufladek import BazaSzufladek
from klasy.szufladka import Szufladka
from klasy.wyjatki import NiepoprawnyNumerException

#sprawdzenie, czy można szufladke pobrać po numerze
def test_dodaj_i_pobierz_szufladke():
    baza = BazaSzufladek()
    szufladka = Szufladka(1, "Cola", 4.50, 5)
    baza.dodaj_szufladke(szufladka)
    pobrana = baza.pobierz_szufladke(1)

    assert pobrana == szufladka
    assert pobrana.numer_szufladki == 1
  
# Sprawdza zabezpieczenie przed nadpisaniem zajętego numeru szufladki
def test_dodaj_duplikat_szufladki():
    baza = BazaSzufladek()
    szufladka1 = Szufladka(1, "Cola", 4.50, 5)
    szufladka2 = Szufladka(1, "Cola", 4.50, 4)

    baza.dodaj_szufladke(szufladka1)

    with pytest.raises(ValueError):
        baza.dodaj_szufladke(szufladka2)

#sprawdzenie, czy jak przekroczymy dozwolony limit szufladek da Error
def test_limit():
    baza = BazaSzufladek(2)
    szufladka1 = Szufladka(1, "Cola", 4.50, 4)
    szufladka2 = Szufladka(2, "woda", 3.50, 5)
    szufladka3 = Szufladka(4, "Cola", 4.50, 4)
    baza.dodaj_szufladke(szufladka1)
    baza.dodaj_szufladke(szufladka2)

    with pytest.raises(ValueError):
        baza.dodaj_szufladke(szufladka3)

#sprawdzenie, czy próba dostania się do nieistniejącej szufladki da błąd
def test_nieistniejacy_numer():
    baza = BazaSzufladek()
    with pytest.raises(NiepoprawnyNumerException):
        baza.pobierz_szufladke(1)

#sprawdzenie, czy metoda zwraca listę z opisami
def test_podaj_produkty():
    baza = BazaSzufladek()
    szufladka1 = Szufladka(1, "Cola", 4.50, 5)
    szufladka2 = Szufladka(2, "Cola", 4.50, 4)
    baza.dodaj_szufladke(szufladka1)
    baza.dodaj_szufladke(szufladka2)

    oferta = baza.podaj_produkty()

    assert len(oferta) == 2
    assert "Cola" in oferta[0]

#sprawdzenie, czy metoda dobrze dzieli produkty na szufladki
def test_wczytanie_z_pliku():
    baza = BazaSzufladek()
    baza.wczytaj_z_pliku("data/produkty.json")

    assert len(baza.podaj_produkty()) == 5 #szufladki
    assert baza.pobierz_szufladke(3).ilosc == 2
    assert baza.pobierz_szufladke(5).nazwa_produktu == "Baton"


