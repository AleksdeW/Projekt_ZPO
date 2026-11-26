from klasy.szufladka import Szufladka
from klasy.wyjatki import NiepoprawnyNumerException
import json

class BazaSzufladek:
    def __init__(self, max_szufladek=12):
        self._szufladki={}
        self._max_szufladek = max_szufladek     #maksymalna liczba szufladek

    def dodaj_szufladke(self, szufladka):
        if len(self._szufladki) >= self._max_szufladek:
            raise ValueError("osiągnięto maksymalną liczbę szufladek")

        if szufladka.numer_szufladki in self._szufladki:
            raise ValueError("taka szufladka już istnieje")

        self._szufladki[szufladka.numer_szufladki] = szufladka

    def pobierz_szufladke(self, numer_szufladki):
        if numer_szufladki not in self._szufladki:
            raise NiepoprawnyNumerException("niepoprawny numer szufladki")

        else:
            return self._szufladki[numer_szufladki]

    def podaj_produkty(self):
        oferta = []
        for numer_szufladki in self._szufladki:
            oferta.append(self._szufladki[numer_szufladki].podaj_status())

        return oferta

    def wczytaj_z_pliku(self, plik):
        with open(plik, "r", encoding="utf-8") as dane:
            dane = json.load(dane)

        licznik = 1
        for produkt in dane:
            nazwa = produkt["nazwa"]
            ilosc = produkt["ilosc"]
            cena = produkt["cena"]

            while ilosc>0:
                do_dodania = min(ilosc, 5)
                nowa_szufladka=Szufladka(licznik, nazwa, cena, do_dodania)
                self.dodaj_szufladke(nowa_szufladka)
                ilosc -= do_dodania
                licznik += 1








