class Szufladka:
    def __init__(self, numer_szufladki, nazwa_produktu, cena, ilosc):

        if numer_szufladki <=0:
            raise ValueError("Numer szufladki musi być większy od zera")

        if not nazwa_produktu.strip():
            raise ValueError("Nazwa produktu nie może być pusta")

        if cena<=0:
            raise ValueError("Cena musi być większa od zera")

        if ilosc<0 or ilosc>5:
            raise ValueError("Ilość musi wynosić od 0 do 5")

        self._numer_szufladki = numer_szufladki
        self._nazwa_produktu = nazwa_produktu
        self._cena = cena
        self._ilosc = ilosc

    @property
    def numer_szufladki(self):
        return self._numer_szufladki

    @property
    def nazwa_produktu(self):
        return self._nazwa_produktu

    @property
    def cena(self):
        return self._cena
    @property
    def ilosc(self):
        return self._ilosc

    def czy_pusta(self):
        return self.ilosc==0

    def podaj_status(self):
        if self.czy_pusta():
            return f"{self._numer_szufladki}. {self._nazwa_produktu} - brak produktu"

        return  f"{self._numer_szufladki}. {self._nazwa_produktu} -{self._cena:} zł {self._ilosc} szt."

    def wydaj_produkt(self):
        if self.czy_pusta():
            raise BrakProduktuException(f"Brak produktu: {self._nazwa_produktu}")
        self._ilosc -=1


