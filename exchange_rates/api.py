from __future__ import annotations

import json
import os.path
from dataclasses import dataclass

import requests
from django.http import JsonResponse


def home(requset):
    data = {"message": "Hello here"}
    return JsonResponse(data)


@dataclass
class ExchangeRate:
    from_: str
    to: str
    value: float

    @classmethod
    def from_response(cls, response: requests.Response):
        pure_response: dict = response.json()["Realtime Currency Exchange Rate"]
        from_ = pure_response["1. From_Currency Code"]
        to = pure_response["3. To_Currency Code"]
        value = pure_response["5. Exchange Rate"]

        return cls(from_=from_, to=to, value=value)

    def as_dict(self) -> dict:
        return {"from": self.from_, "to": self.to, "value": self.value}

    def __eq__(self, other: ExchangeRate) -> bool:
        return self.value == other.value


ExchangeRates = list[ExchangeRate]

# NOTE: class work History class
# class ExchangeRatesHistory:
#     _history: ExchangeRates = []

#     @classmethod
#     def add(cls, instance: ExchangeRate) -> None:
#         if not cls._history:
#             cls._history.append(instance)
#         elif instance != cls._history[-1]:
#             cls._history.append(instance)

#     @classmethod
#     def as_dict(cls) -> dict:
#         return {
#             "results": [er.as_dict() for er in cls._history]
#         }


# NOTE: My homework class
class ExchangeRatesHistoryFile:

    FILE_NAME = "history.json"

    @classmethod
    def get_history(cls):
        # check if file exists
        if not os.path.exists(cls.FILE_NAME):
            file = open(cls.FILE_NAME, "w")
            file.close()

        with open(cls.FILE_NAME, encoding="utf-8", mode="r") as file:
            history = file.read()
            print(f"History: {history}")
            if not history:
                history = "[]"
        return json.loads(history)

    @classmethod
    def save_to_file(cls, new_history):
        with open(cls.FILE_NAME, encoding="utf-8", mode="w") as file:
            json.dump(new_history, file, indent=4, separators=(",", ": "))

    @classmethod
    def add(cls, instance):
        history_json = cls.get_history()
        if len(history_json) == 0:
            history_json.append(instance.as_dict())
            cls.save_to_file(history_json)

        elif instance.value != history_json[-1]["value"]:
            history_json.append(instance.as_dict())
            cls.save_to_file(history_json)

    @classmethod
    def as_dict(cls) -> dict:
        history = cls.get_history()
        return {"results": [er for er in history]}


def btc_usd(requset):
    API_KEY = "OTGJKZDKG8LTTBDS"
    url = (
        "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&"
        f"from_currency=BTC&to_currency=USD&apikey={API_KEY}"
    )
    response = requests.get(url)
    exchange_rate = ExchangeRate.from_response(response)
    ExchangeRatesHistoryFile.add(exchange_rate)

    return JsonResponse(exchange_rate.as_dict())


def history(requset):
    return JsonResponse(ExchangeRatesHistoryFile.as_dict())
