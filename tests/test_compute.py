# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from datetime import date

from jours_feries_france.compute import JoursFeries


class TestDatasetParser(unittest.TestCase):
    def test_for_year(self):
        self.assertEquals(
            JoursFeries.for_year(2018),
            {
                "Armistice": date(2018, 11, 11),
                "Ascension": date(2018, 5, 10),
                "Assomption": date(2018, 8, 15),
                "Fête Nationale": date(2018, 7, 14),
                "Fête du travail": date(2018, 5, 1),
                "Jour de l'an": date(2018, 1, 1),
                "Lundi de Pâques": date(2018, 4, 2),
                "Noël": date(2018, 12, 25),
                "Lundi de Pentecôte": date(2018, 5, 21),
                "Toussaint": date(2018, 11, 1),
                "Victoire des alliés": date(2018, 5, 8),
            },
        )

        self.assertEquals(
            JoursFeries.for_year(2020),
            {
                "Armistice": date(2020, 11, 11),
                "Ascension": date(2020, 5, 21),
                "Assomption": date(2020, 8, 15),
                "Fête Nationale": date(2020, 7, 14),
                "Fête du travail": date(2020, 5, 1),
                "Jour de l'an": date(2020, 1, 1),
                "Lundi de Pâques": date(2020, 4, 13),
                "Noël": date(2020, 12, 25),
                "Lundi de Pentecôte": date(2020, 6, 1),
                "Toussaint": date(2020, 11, 1),
                "Victoire des alliés": date(2020, 5, 8),
            },
        )

    def test_for_year_in_alsace(self):
        self.maxDiff = None
        self.assertEquals(
            JoursFeries.for_year(2018, include_alsace=True),
            {
                "Armistice": date(2018, 11, 11),
                "Ascension": date(2018, 5, 10),
                "Assomption": date(2018, 8, 15),
                "Fête Nationale": date(2018, 7, 14),
                "Fête du travail": date(2018, 5, 1),
                "Jour de l'an": date(2018, 1, 1),
                "Lundi de Pâques": date(2018, 4, 2),
                "Noël": date(2018, 12, 25),
                "Lundi de Pentecôte": date(2018, 5, 21),
                "Toussaint": date(2018, 11, 1),
                "Victoire des alliés": date(2018, 5, 8),
                "Vendredi Saint": date(2018, 3, 30),
                "Saint Étienne": date(2018, 12, 26),
            },
        )

        self.assertEquals(
            JoursFeries.for_year(2020, include_alsace=True),
            {
                "Armistice": date(2020, 11, 11),
                "Ascension": date(2020, 5, 21),
                "Assomption": date(2020, 8, 15),
                "Fête Nationale": date(2020, 7, 14),
                "Fête du travail": date(2020, 5, 1),
                "Jour de l'an": date(2020, 1, 1),
                "Lundi de Pâques": date(2020, 4, 13),
                "Noël": date(2020, 12, 25),
                "Lundi de Pentecôte": date(2020, 6, 1),
                "Toussaint": date(2020, 11, 1),
                "Victoire des alliés": date(2020, 5, 8),
                "Vendredi Saint": date(2020, 4, 10),
                "Saint Étienne": date(2020, 12, 26),
            },
        )

    def testPaques(self):
        self.assertEquals(JoursFeries.paques(1954), date(1954, 4, 18))
        self.assertEquals(JoursFeries.paques(1981), date(1981, 4, 19))
        self.assertEquals(JoursFeries.paques(2049), date(2049, 4, 18))
