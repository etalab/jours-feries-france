# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from datetime import date

from jours_feries_france.compute import JoursFeries


class TestDatasetParser(unittest.TestCase):
    def test_validates_region(self):
        with self.assertRaises(ValueError):
            JoursFeries.for_year(2018, zone="foo")

    def test_is_holiday(self):
        self.assertTrue(JoursFeries.is_holiday(date(2019, 12, 25)))
        self.assertTrue(JoursFeries.is_holiday(date(2019, 12, 25), zone="Métropole"))
        self.assertTrue(
            JoursFeries.is_holiday(date(2019, 12, 26), zone="Alsace-Moselle")
        )

        self.assertFalse(JoursFeries.is_holiday(date(2019, 12, 26)))
        self.assertFalse(JoursFeries.is_holiday(date(2019, 12, 26), zone="Métropole"))

    def test_next_holiday(self):
        self.assertEquals(
            ("Armistice", date(2018, 11, 11)),
            JoursFeries.next_holiday(date(2018, 11, 10)),
        )

        self.assertEquals(
            ("Armistice", date(2018, 11, 11)),
            JoursFeries.next_holiday(date(2018, 11, 11), zone="Métropole"),
        )

        self.assertEquals(
            ("Noël", date(2018, 12, 25)),
            JoursFeries.next_holiday(date(2018, 12, 11), zone="Métropole"),
        )

    def test_for_year(self):
        self.assertDictEqual(
            JoursFeries.for_year(2018),
            {
                "Jour de l'an": date(2018, 1, 1),
                "Lundi de Pâques": date(2018, 4, 2),
                "Fête du travail": date(2018, 5, 1),
                "Victoire des alliés": date(2018, 5, 8),
                "Ascension": date(2018, 5, 10),
                "Lundi de Pentecôte": date(2018, 5, 21),
                "Fête Nationale": date(2018, 7, 14),
                "Assomption": date(2018, 8, 15),
                "Toussaint": date(2018, 11, 1),
                "Armistice": date(2018, 11, 11),
                "Noël": date(2018, 12, 25),
            },
        )

        self.assertDictEqual(
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
        self.assertDictEqual(
            JoursFeries.for_year(2018, zone="Alsace-Moselle"),
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

        self.assertDictEqual(
            JoursFeries.for_year(2020, zone="Alsace-Moselle"),
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
