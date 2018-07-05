# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
import datetime

from jours_feries_france.compute import JoursFeries


class TestDatasetParser(unittest.TestCase):
    def test_for_year(self):
        self.assertEquals(
            JoursFeries.for_year(2018),
            {
                'Armistice': datetime.date(2018, 11, 11),
                'Ascension': datetime.date(2018, 5, 10),
                'Assomption': datetime.date(2018, 8, 15),
                'Fête Nationale': datetime.date(2018, 7, 14),
                'Fête du travail': datetime.date(2018, 5, 1),
                "Jour de l'an": datetime.date(2018, 1, 1),
                'Lundi de Pâques': datetime.date(2018, 4, 2),
                'Noël': datetime.date(2018, 12, 25),
                'Pentecôte': datetime.date(2018, 5, 21),
                'Toussaint': datetime.date(2018, 11, 1),
                'Victoire des alliés': datetime.date(2018, 5, 8)
            }
        )

        self.assertEquals(
            JoursFeries.for_year(2020),
            {
                'Armistice': datetime.date(2020, 11, 11),
                'Ascension': datetime.date(2020, 5, 21),
                'Assomption': datetime.date(2020, 8, 15),
                'Fête Nationale': datetime.date(2020, 7, 14),
                'Fête du travail': datetime.date(2020, 5, 1),
                "Jour de l'an": datetime.date(2020, 1, 1),
                'Lundi de Pâques': datetime.date(2020, 4, 13),
                'Noël': datetime.date(2020, 12, 25),
                'Pentecôte': datetime.date(2020, 6, 1),
                'Toussaint': datetime.date(2020, 11, 1),
                'Victoire des alliés': datetime.date(2020, 5, 8)
            }
        )

    def test_for_year_in_alsace(self):
        self.maxDiff = None
        self.assertEquals(
            JoursFeries.for_year(2018, include_alsace=True),
            {
                'Armistice': datetime.date(2018, 11, 11),
                'Ascension': datetime.date(2018, 5, 10),
                'Assomption': datetime.date(2018, 8, 15),
                'Fête Nationale': datetime.date(2018, 7, 14),
                'Fête du travail': datetime.date(2018, 5, 1),
                "Jour de l'an": datetime.date(2018, 1, 1),
                'Lundi de Pâques': datetime.date(2018, 4, 2),
                'Noël': datetime.date(2018, 12, 25),
                'Pentecôte': datetime.date(2018, 5, 21),
                'Toussaint': datetime.date(2018, 11, 1),
                'Victoire des alliés': datetime.date(2018, 5, 8),
                'Vendredi Saint': datetime.date(2018, 3, 30),
                'Saint Étienne': datetime.date(2018, 12, 26)
            }
        )

        self.assertEquals(
            JoursFeries.for_year(2020, include_alsace=True),
            {
                'Armistice': datetime.date(2020, 11, 11),
                'Ascension': datetime.date(2020, 5, 21),
                'Assomption': datetime.date(2020, 8, 15),
                'Fête Nationale': datetime.date(2020, 7, 14),
                'Fête du travail': datetime.date(2020, 5, 1),
                "Jour de l'an": datetime.date(2020, 1, 1),
                'Lundi de Pâques': datetime.date(2020, 4, 13),
                'Noël': datetime.date(2020, 12, 25),
                'Pentecôte': datetime.date(2020, 6, 1),
                'Toussaint': datetime.date(2020, 11, 1),
                'Victoire des alliés': datetime.date(2020, 5, 8),
                'Vendredi Saint': datetime.date(2020, 4, 10),
                'Saint Étienne': datetime.date(2020, 12, 26)
            }
        )
