class AutomatException(Exception):
    #klasa bazowa
    pass


class ZaMaloSrodkowException(AutomatException):
    #za malo pieniedzy na wybrany produkt
    pass


class BrakProduktuException(AutomatException):
    #nie ma juz takiego produktu
    pass


class BrakResztyException(AutomatException):
    #brakuje monet na wydanie reszty
    pass


class NiepoprawnyNumerException(AutomatException):
    #wpisano zly numer produktu
    pass
