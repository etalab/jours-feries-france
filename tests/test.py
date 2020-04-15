# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import unittest
from datetime import date

from jours_feries_france import JoursFeries


class TestDatasetParser(unittest.TestCase):
    def test_validates_region(self):
        with self.assertRaises(ValueError):
            JoursFeries.for_year(2018, zone="foo")

    def test_is_bank_holiday(self):
        self.assertTrue(JoursFeries.is_bank_holiday(date(2019, 12, 25)))
        self.assertTrue(
            JoursFeries.is_bank_holiday(date(2019, 12, 25), zone="Métropole")
        )
        self.assertTrue(
            JoursFeries.is_bank_holiday(date(2019, 12, 26), zone="Alsace-Moselle")
        )

        self.assertFalse(JoursFeries.is_bank_holiday(date(2019, 12, 26)))
        self.assertFalse(
            JoursFeries.is_bank_holiday(date(2019, 12, 26), zone="Métropole")
        )

    def test_next_bank_holiday(self):
        self.assertEquals(
            ("Armistice", date(2018, 11, 11)),
            JoursFeries.next_bank_holiday(date(2018, 11, 10)),
        )

        self.assertEquals(
            ("Armistice", date(2018, 11, 11)),
            JoursFeries.next_bank_holiday(date(2018, 11, 11), zone="Métropole"),
        )

        self.assertEquals(
            ("Noël", date(2018, 12, 25)),
            JoursFeries.next_bank_holiday(date(2018, 12, 11), zone="Métropole"),
        )

    def test_for_year(self):
        self.assertDictEqual(
            JoursFeries.for_year(2018),
            {
                "Jour de l'an": date(2018, 1, 1),
                "Lundi de Pâques": date(2018, 4, 2),
                "Fête du Travail": date(2018, 5, 1),
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
                "Fête du Travail": date(2020, 5, 1),
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
                "Fête du Travail": date(2018, 5, 1),
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
                "Fête du Travail": date(2020, 5, 1),
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

    def testNamesAllZones(self):
        def names(holidays):
            return set(holidays.keys())

        base = set(
            [
                "Jour de l'an",
                "Fête du Travail",
                "Victoire des alliés",
                "Fête Nationale",
                "Assomption",
                "Toussaint",
                "Armistice",
                "Noël",
                "Lundi de Pâques",
                "Ascension",
                "Lundi de Pentecôte",
            ]
        )

        extra_holidays = [
            ["Alsace-Moselle", set(["Vendredi Saint", "Saint Étienne"])],
            ["Guadeloupe", set(["Abolition de l'esclavage"]),],
            ["Guyane", set(["Abolition de l'esclavage"])],
            ["Martinique", set(["Abolition de l'esclavage"]),],
            ["Mayotte", set(["Abolition de l'esclavage"]),],
            ["Nouvelle-Calédonie", set()],
            ["La Réunion", set(["Abolition de l'esclavage"])],
            ["Polynésie Française", set()],
            ["Saint-Barthélémy", set(["Abolition de l'esclavage"])],
            ["Saint-Martin", set(["Abolition de l'esclavage"])],
            ["Wallis-et-Futuna", set()],
            ["Saint-Pierre-et-Miquelon", set()],
        ]

        self.assertSetEqual(names(JoursFeries.for_year(2020, "Métropole")), base)

        for test in extra_holidays:
            zone, holidays = test
            self.assertEquals(
                names(JoursFeries.for_year(2020, zone)), base.union(holidays)
            )

        self.assertEquals(
            JoursFeries.ZONES, ["Métropole"] + [e[0] for e in extra_holidays]
        )

    def testAbolitionDeLesclavage(self):
        tests = [
            ("Mayotte", date(2020, 4, 27)),
            ("Martinique", date(2020, 5, 22)),
            ("Guadeloupe", date(2020, 5, 27)),
            ("Saint-Martin", date(2020, 5, 28)),
            ("Guyane", date(2020, 6, 10)),
            ("Saint-Barthélémy", date(2020, 10, 9)),
            ("La Réunion", date(2020, 12, 20)),
        ]

        zones = set()
        for test in tests:
            zone, expected_date = test
            zones.add(zone)
            self.assertEquals(
                JoursFeries.abolitionDeLesclavage(2020, zone), expected_date
            )

        for zone in [z for z in JoursFeries.ZONES if z not in zones]:
            self.assertEquals(JoursFeries.abolitionDeLesclavage(2020, zone), None)

        # Saint-Martin
        self.assertEquals(
            JoursFeries.abolitionDeLesclavage(2017, "Saint-Martin"), date(2017, 5, 27)
        )
        self.assertEquals(
            JoursFeries.abolitionDeLesclavage(2018, "Saint-Martin"), date(2018, 5, 28)
        )
