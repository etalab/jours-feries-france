# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import math


class JoursFeries(object):
    def __init__(self):
        super(JoursFeries, self).__init__()

    @staticmethod
    def for_year(year, include_alsace=False):
        res = {
            "Jour de l'an": JoursFeries.jourDeLAn(year),
            "Fête du travail": JoursFeries.feteDuTravail(year),
            "Victoire des alliés": JoursFeries.victoireDesAllies(year),
            "Fête Nationale": JoursFeries.feteNationale(year),
            "Assomption": JoursFeries.assomption(year),
            "Toussaint": JoursFeries.toussaint(year),
            "Armistice": JoursFeries.armistice(year),
            "Noël": JoursFeries.noel(year),
            "Lundi de Pâques": JoursFeries.lundiDePaques(year),
            "Ascension": JoursFeries.ascension(year),
            "Lundi de Pentecôte": JoursFeries.lundiDePentecote(year),
        }

        if include_alsace:
            res["Vendredi Saint"] = JoursFeries.vendrediSaint(year)
            res["Saint Étienne"] = JoursFeries.saintEtienne(year)

        return res

    @staticmethod
    def paques(year):
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1
        return datetime.date(year, month, day)

    @staticmethod
    def lundiDePaques(year):
        delta = datetime.timedelta(days=1)

        return JoursFeries.paques(year) + delta

    @staticmethod
    def vendrediSaint(year):
        delta = datetime.timedelta(days=2)

        return JoursFeries.paques(year) - delta

    @staticmethod
    def ascension(year):
        delta = datetime.timedelta(days=39)

        return JoursFeries.paques(year) + delta

    @staticmethod
    def lundiDePentecote(year):
        delta = datetime.timedelta(days=50)

        return JoursFeries.paques(year) + delta

    @staticmethod
    def jourDeLAn(year):
        return datetime.date(year, 1, 1)

    @staticmethod
    def feteDuTravail(year):
        return datetime.date(year, 5, 1)

    @staticmethod
    def victoireDesAllies(year):
        return datetime.date(year, 5, 8)

    @staticmethod
    def feteNationale(year):
        return datetime.date(year, 7, 14)

    @staticmethod
    def toussaint(year):
        return datetime.date(year, 11, 1)

    @staticmethod
    def assomption(year):
        return datetime.date(year, 8, 15)

    @staticmethod
    def armistice(year):
        return datetime.date(year, 11, 11)

    @staticmethod
    def noel(year):
        return datetime.date(year, 12, 25)

    @staticmethod
    def saintEtienne(year):
        return datetime.date(year, 12, 26)
