# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import date, timedelta


class JoursFeries(object):
    ZONES = [
        "Métropole",
        "Alsace-Moselle",
        "Guadeloupe",
        "Guyane",
        "Martinique",
        "Mayotte",
        "Nouvelle-Calédonie",
        "La Réunion",
        "Polynésie Française",
        "Saint-Barthélémy",
        "Saint-Martin",
        "Wallis-et-Futuna",
        "Saint-Pierre-et-Miquelon",
    ]

    def __init__(self):
        super(JoursFeries, self).__init__()

    @staticmethod
    def check_zone(zone):
        zone = zone or "Métropole"

        if zone not in JoursFeries.ZONES:
            valid_values = ", ".join(JoursFeries.ZONES)
            raise ValueError(
                "%s is invalid. Supported values: %s" % (zone, valid_values)
            )

        return zone

    @staticmethod
    def is_bank_holiday(date, zone=None):
        return date in JoursFeries.for_year(date.year, zone).values()

    @staticmethod
    def next_bank_holiday(date, zone=None):
        while not JoursFeries.is_bank_holiday(date, zone):
            date = date + timedelta(days=1)

        return [
            (k, v)
            for k, v in JoursFeries.for_year(date.year, zone).items()
            if v == date
        ][0]

    @staticmethod
    def for_year(year, zone=None):
        JoursFeries.check_zone(zone)

        bank_holidays = {
            "1er janvier": JoursFeries.premier_janvier(year),
            "1er mai": JoursFeries.premier_mai(year),
            "8 mai": JoursFeries.huit_mai(year),
            "14 juillet": JoursFeries.quatorze_juillet(year),
            "Assomption": JoursFeries.assomption(year),
            "Toussaint": JoursFeries.toussaint(year),
            "11 novembre": JoursFeries.onze_novembre(year),
            "Jour de Noël": JoursFeries.jour_noel(year),
            "Lundi de Pâques": JoursFeries.lundi_paques(year),
            "Ascension": JoursFeries.ascension(year),
            "Lundi de Pentecôte": JoursFeries.lundi_pentecote(year),
            "Vendredi saint": JoursFeries.vendredi_saint(year, zone),
            "2ème jour de Noël": JoursFeries.deuxieme_jour_noel(year, zone),
            "Abolition de l'esclavage": JoursFeries.abolition_esclavage(year, zone),
        }

        bank_holidays = {k: v for k, v in bank_holidays.items() if v}

        return {
            k: v for k, v in sorted(bank_holidays.items(), key=lambda item: item[1])
        }

    @staticmethod
    def paques(year):
        if year < 1886:
            return None
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1
        return date(year, month, day)

    @staticmethod
    def lundi_paques(year):
        if year >= 1886:
            return JoursFeries.paques(year) + timedelta(days=1)
        return None

    @staticmethod
    def vendredi_saint(year, zone):
        if zone == JoursFeries.check_zone("Alsace-Moselle"):
            return JoursFeries.paques(year) - timedelta(days=2)
        return None

    @staticmethod
    def ascension(year):
        if year >= 1802:
            return JoursFeries.paques(year) + timedelta(days=39)
        return None

    @staticmethod
    def lundi_pentecote(year):
        if year >= 1886:
            return JoursFeries.paques(year) + timedelta(days=50)
        return None

    @staticmethod
    def premier_janvier(year):
        if year > 1810:
            return date(year, 1, 1)
        return None

    @staticmethod
    def premier_mai(year):
        if year > 1919:
            return date(year, 5, 1)
        return None

    @staticmethod
    def huit_mai(year):
        if (1953 <= year <= 1959) or year > 1981:
            return date(year, 5, 8)
        return None

    @staticmethod
    def quatorze_juillet(year):
        if year >= 1880:
            return date(year, 7, 14)
        return None

    @staticmethod
    def toussaint(year):
        if year >= 1802:
            return date(year, 11, 1)
        return None

    @staticmethod
    def assomption(year):
        if year >= 1802:
            return date(year, 8, 15)
        return None

    @staticmethod
    def onze_novembre(year):
        if year >= 1918:
            return date(year, 11, 11)
        return None

    @staticmethod
    def jour_noel(year):
        if year >= 1802:
            return date(year, 12, 25)
        return None

    @staticmethod
    def deuxieme_jour_noel(year, zone):
        if zone == JoursFeries.check_zone("Alsace-Moselle"):
            return date(year, 12, 26)
        return None

    @staticmethod
    def abolition_esclavage(year, zone):
        if zone == JoursFeries.check_zone("Mayotte"):
            return date(year, 4, 27)

        if zone == JoursFeries.check_zone("Martinique"):
            return date(year, 5, 22)

        if zone == JoursFeries.check_zone("Guadeloupe"):
            return date(year, 5, 27)

        if zone == JoursFeries.check_zone("Saint-Martin"):
            if year >= 2018:
                return date(year, 5, 28)
            else:
                return date(year, 5, 27)

        if zone == JoursFeries.check_zone("Guyane"):
            return date(year, 6, 10)

        if zone == JoursFeries.check_zone("Saint-Barthélémy"):
            return date(year, 10, 9)

        if zone == JoursFeries.check_zone("La Réunion") and year >= 1981:
            return date(year, 12, 20)

        return None
