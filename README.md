[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/etalab/jours-feries-france/blob/master/LICENSE.md)
![CircleCI](https://img.shields.io/circleci/project/github/etalab/jours-feries-france.svg?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jours-feries-france.svg?style=flat-square)

# Jours fériés France
Cette librairie calcule les jours fériés en France.

## Installation
```
pip install jours-feries-france
```

## Usage
```python
import datetime

from jours_feries_france import JoursFeries

res = JoursFeries.for_year(2018)
# res est un dictionnaire
# {
#     "Jour de l'an": date(2018, 1, 1),
#     "Lundi de Pâques": date(2018, 4, 2),
#     "Fête du Travail": date(2018, 5, 1),
#     "Victoire des alliés": date(2018, 5, 8),
#     "Ascension": date(2018, 5, 10),
#     "Lundi de Pentecôte": date(2018, 5, 21),
#     "Fête Nationale": date(2018, 7, 14),
#     "Assomption": date(2018, 8, 15),
#     "Toussaint": date(2018, 11, 1),
#     "Armistice": date(2018, 11, 11),
#     "Noël": date(2018, 12, 25),
# }

# Vous pouvez aussi obtenir certains jours fériés en tant que datetime.date
print (JoursFeries.lundiDePaques(2018))
print (JoursFeries.ascension(2018))
print (JoursFeries.lundiDePentecote(2018))

# Obtenir les jours fériés pour une zone spécifique
res = JoursFeries.for_year(2018, zone="Alsace-Moselle")

# Quelques fonctions d'aide
JoursFeries.is_holiday(datetime.date(2019, 12, 25), zone="Métropole")
# -> True
JoursFeries.next_holiday(datetime.date(2019, 12, 24), zone="Métropole")
# -> ('Noël', datetime.date(2019, 12, 25))
```

### Zones disponibles
Les zones suivantes sont disponibles :
- `Métropole` (par défaut)
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

## Données
Si vous souhaitez simplement un export, consultez le jeu de données ["Jours fériés en France"](https://www.data.gouv.fr/fr/datasets/jours-feries-en-france/) sur data.gouv.fr.

## Sources
- [Code du travail : articles L3133-1 à L3133-3](https://www.legifrance.gouv.fr/affichCode.do?idSectionTA=LEGISCTA000033008129&cidTexte=LEGITEXT000006072050)
- [ Code du travail - Article L3422-2](https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000035902463&cidTexte=LEGITEXT000006072050)
