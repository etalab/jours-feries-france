[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/AntoineAugusti/jours-feries-france/blob/master/LICENSE.md)
![CircleCI](https://img.shields.io/circleci/project/github/AntoineAugusti/jours-feries-france.svg?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jours-feries-france.svg?style=flat-square)

# Jours Fériés France
This library computes bank holidays dates for France, for a given year.

## Installation
```
pip install jours-feries-france
```

## Usage
```python
from jours_feries_france.compute import JoursFeries

res = JoursFeries.for_year(2018)
# res is now a dict
# {
#     "Jour de l'an": date(2018, 1, 1),
#     "Lundi de Pâques": date(2018, 4, 2),
#     "Fête du travail": date(2018, 5, 1),
#     "Victoire des alliés": date(2018, 5, 8),
#     "Ascension": date(2018, 5, 10),
#     "Lundi de Pentecôte": date(2018, 5, 21),
#     "Fête Nationale": date(2018, 7, 14),
#     "Assomption": date(2018, 8, 15),
#     "Toussaint": date(2018, 11, 1),
#     "Armistice": date(2018, 11, 11),
#     "Noël": date(2018, 12, 25),
# }

# You can also get specific bank holidays as a datetime.date
print (JoursFeries.lundiDePaques(2018))
print (JoursFeries.ascension(2018))
print (JoursFeries.lundiDePentecote(2018))

# Get bank holidays for a specific French zone.
res = JoursFeries.for_year(2018, zone="Alsace-Moselle")

# Some helpers
JoursFeries.is_holiday(datetime.date(2019, 12, 25), zone="Métropole")
# -> True
JoursFeries.next_holiday(datetime.date(2019, 12, 24), zone="Métropole")
# -> ('Noël', datetime.date(2019, 12, 25))
```

### Available zones
The following zones are available:
- `Métropole` (default)
- `Alsace-Moselle`
- `Guadeloupe`
- `Guyane`
- `Martinique`
- `Mayotte`
- `Nouvelle-Calédonie`
- `La Réunion`
- `Polynésie Française`
- `Saint-Barthélémy`
- `Saint-Martin`
- `Wallis-et-Futuna`

## Data
If you just want a CSV dump, check out the ["Jours fériés en France" opendata dataset](https://www.data.gouv.fr/fr/datasets/jours-feries-en-france/) available on data.gouv.fr.

## REST API
Looking for a JSON API? Check out [this GitHub project](https://github.com/AntoineAugusti/api-jours-feries-france).

## School holidays
Interested in school holidays as well (vacances scolaires in French)? There is another pip package for this! Check out https://github.com/AntoineAugusti/vacances-scolaires-france

## Notice
This software is available under the MIT license and was developed as part of the [Entrepreneur d'Intérêt Général program](https://entrepreneur-interet-general.etalab.gouv.fr) by the French government.

Projet développé dans le cadre du programme « [Entrepreneur d’intérêt général](https://entrepreneur-interet-general.etalab.gouv.fr) ».
