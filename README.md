[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/AntoineAugusti/jours-feries-france/blob/master/LICENSE.md)
![CircleCI](https://img.shields.io/circleci/project/github/AntoineAugusti/jours-feries-france.svg?style=flat-square)


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
#     'Armistice': datetime.date(2018, 11, 11),
#     'Ascension': datetime.date(2018, 5, 10),
#     'Assomption': datetime.date(2018, 8, 15),
#     'Fête Nationale': datetime.date(2018, 7, 14),
#     'Fête du travail': datetime.date(2018, 5, 1),
#     "Jour de l'an": datetime.date(2018, 1, 1),
#     'Lundi de Pâques': datetime.date(2018, 4, 2),
#     'Noël': datetime.date(2018, 12, 25),
#     'Pentecôte': datetime.date(2018, 5, 21),
#     'Toussaint': datetime.date(2018, 11, 1),
#     'Victoire des alliés': datetime.date(2018, 5, 8)
# }

# You can also get specific bank holidays as a datetime.date
print (JoursFeries.lundiDePaques(2018))
print (JoursFeries.ascension(2018))
print (JoursFeries.pentecote(2018))
print (JoursFeries.jourDeLAn(2018))
print (JoursFeries.feteDuTravail(2018))
print (JoursFeries.victoireDeAllies(2018))
print (JoursFeries.feteNationale(2018))
print (JoursFeries.toussaint(2018))
print (JoursFeries.assomption(2018))
print (JoursFeries.armistice(2018))
print (JoursFeries.noel(2018))

# The Alsace-Moselle region has 2 extra bank holidays.
# You can include them this way
res = JoursFeries.for_year(2018, include_alsace=True)

print (JoursFeries.vendrediSaint(2018))
print (JoursFeries.saintEtienne(2018))
```
