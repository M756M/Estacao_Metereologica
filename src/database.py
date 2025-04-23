import sqlite3, re;
from datetime import datetime
from typing import Callable

class Date:
    type Adapter = Callable[['Date'], str]

    _ID: int

    year: int
    month: int
    day: int

    hour: int
    minute: int

    def __init__(self, source: str, format: str = "YYYY-MM-DD hh:mm"):
        if(re.search(r"(?<!Y)YYYY(?!Y)", format) is None): raise ValueError("A formatação deve especificar o ano em 4 dígitos (YYYY)")
        if(re.search(r"(?<!M)MM(?!M)"  , format) is None): raise ValueError("A formatação deve especificar o mês em 2 dígitos (MM)")
        if(re.search(r"(?<!D)DD(?!D)"  , format) is None): raise ValueError("A formatação deve especificar o dia em 2 dígitos (DD)")
        if(re.search(r"(?<!h)hh(?!h)"  , format) is None): raise ValueError("A formatação deve especificar a hora em 2 dígitos (hh)")
        if(re.search(r"(?<!m)mm(?!m)"  , format) is None): raise ValueError("A formatação deve especificar os minutos em 2 dígitos (mm)")

        yearSpan = re.search(r"(?<!Y)YYYY(?!Y)", format).span()
        monthSpan = re.search(r"(?<!M)MM(?!M)"  , format).span()
        daySpan = re.search(r"(?<!D)DD(?!D)"  , format).span()
        hourSpan = re.search(r"(?<!h)hh(?!h)"  , format).span()
        minuteSpan = re.search(r"(?<!m)mm(?!m)"  , format).span()

        if(re.search(r"\d{4}", source[yearSpan[0]:yearSpan[1]]) is None): raise ValueError("A data fornecida não contem o ano")
        if(re.search(r"\d{2}", source[monthSpan[0]:monthSpan[1]]) is None): raise ValueError("A data fornecida não contem o mês")
        if(re.search(r"\d{2}", source[daySpan[0]:daySpan[1]]) is None): raise ValueError("A data fornecida não contem o dia")
        if(re.search(r"\d{2}", source[hourSpan[0]:hourSpan[1]]) is None): raise ValueError("A data fornecida não contem a hora")
        if(re.search(r"\d{2}", source[minuteSpan[0]:minuteSpan[1]]) is None): raise ValueError("A data fornecida não contem os minutos")

        self.year = int(source[yearSpan[0]:yearSpan[1]])
        self.month = int(source[monthSpan[0]:monthSpan[1]])
        self.day = int(source[daySpan[0]:daySpan[1]])
        self.hour = int(source[hourSpan[0]:hourSpan[1]])
        self.minute = int(source[minuteSpan[0]:minuteSpan[1]])

        if(self.month > 12 or self.month < 1): raise ValueError("O mês da data fornecida é inválido")
        if(self.day > 32 or self.day < 1): raise ValueError("O dia da data fornecida é inválido")
        if(self.hour >= 24 or self.hour < 0): raise ValueError("A hora da data fornecida é inválida")
        if(self.minute >= 60 or self.minute < 0): raise ValueError("Os minutos da data fornecida são inválidos")
        
        return

    def getAdapter(self, format: str = "YYYY-MM-DD hh:mm") -> Adapter:
        raise NotImplementedError()

class Crude:
    _ID: int

    date: Date
    airSpeed: float
    relativeMoisture: float
    airTemperature: float

    source: str

class Polished:
    _ID: int

    date: Date

    apparentTemperature: float