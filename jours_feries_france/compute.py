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
            "Victoire des alliés": JoursFeries.victoireDeAllies(year),
            "Fête Nationale": JoursFeries.feteNationale(year),
            "Assomption": JoursFeries.assomption(year),
            "Toussaint": JoursFeries.toussaint(year),
            "Armistice": JoursFeries.armistice(year),
            "Noël": JoursFeries.noel(year),
            "Lundi de Pâques": JoursFeries.lundiDePaques(year),
            "Ascension": JoursFeries.ascension(year),
            "Pentecôte": JoursFeries.pentecote(year)
        }

        if include_alsace:
            res["Vendredi Saint"] = JoursFeries.vendrediSaint(year)
            res["Saint Étienne"] = JoursFeries.saintEtienne(year)

        return res

    @staticmethod
    def paques(year):
        a = year % 19
        b = math.floor(year / 100)
        c = year % 100
        d = math.floor(b / 4)
        e = b % 4
        f = math.floor((b + 8) / 25)
        g = math.floor((b - f + 1) / 3)
        h = (19 * a + b - d - g + 15) % 30
        i = math.floor(c / 4)
        k = c % 4
        l = (32 + 2 * e + 2 * i - h - k) % 7
        m = math.floor((a + 11 * h + 22 * l) / 451)
        n0 = (h + l + 7 * m + 114)
        n = math.floor(n0 / 31)
        p = n0 % 31 + 1

        return datetime.date(year, int(n), int(p))

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
    def pentecote(year):
        delta = datetime.timedelta(days=50)

        return JoursFeries.paques(year) + delta

    @staticmethod
    def jourDeLAn(year):
        return datetime.date(year, 1, 1)

    @staticmethod
    def feteDuTravail(year):
        return datetime.date(year, 5, 1)

    @staticmethod
    def victoireDeAllies(year):
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
