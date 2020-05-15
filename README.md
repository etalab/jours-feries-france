[![Software License](https://img.shields.io/badge/License-MIT-orange.svg?style=flat-square)](https://github.com/etalab/jours-feries-france/blob/master/LICENSE.md)
![CircleCI](https://img.shields.io/circleci/project/github/etalab/jours-feries-france.svg?style=flat-square)
![PyPI - Downloads](https://img.shields.io/pypi/dm/jours-feries-france.svg?style=flat-square)

# Jours fériés France
Cette librairie calcule les jours fériés en France. Vous pouvez découvrir plus de détails sur les jours fériés français sur [service-public.fr](https://www.service-public.fr/particuliers/vosdroits/F2405).

Cette librairie fonctionne à partir de la version 2.7 de Python.

## Installation
```
pip install jours-feries-france
```

## Usage
```python
import datetime

from jours_feries_france import JoursFeries

# Obtenir les jours fériés pour une année, pour la métropole
res = JoursFeries.for_year(2018)
# res est un dictionnaire
# {
#     '1er janvier': datetime.date(2018, 1, 1),
#     'Lundi de Pâques': datetime.date(2018, 4, 2),
#     '1er mai': datetime.date(2018, 5, 1),
#     '8 mai': datetime.date(2018, 5, 8),
#     'Ascension': datetime.date(2018, 5, 10),
#     'Lundi de Pentecôte': datetime.date(2018, 5, 21),
#     '14 juillet': datetime.date(2018, 7, 14),
#     'Assomption': datetime.date(2018, 8, 15),
#     'Toussaint': datetime.date(2018, 11, 1),
#     '11 novembre': datetime.date(2018, 11, 11),
#     'Jour de Noël': datetime.date(2018, 12, 25)
# }

# Vous pouvez aussi obtenir certains jours fériés en tant que datetime.date
print (JoursFeries.lundi_paques(2018))
print (JoursFeries.ascension(2018))
print (JoursFeries.lundi_pentecote(2018))

# Obtenir les jours fériés pour une zone spécifique
res = JoursFeries.for_year(2018, zone="Alsace-Moselle")

# Quelques fonctions d'aide
JoursFeries.is_bank_holiday(datetime.date(2019, 12, 25), zone="Métropole")
# -> True
JoursFeries.next_bank_holiday(datetime.date(2019, 12, 24), zone="Métropole")
# -> ('Noël', datetime.date(2019, 12, 25))
```

### Zones disponibles
Les zones suivantes sont disponibles :
- `Métropole` (par défaut)
- `Alsace-Moselle`
- `Guadeloupe`
- `Guyane`
- `La Réunion`
- `Martinique`
- `Mayotte`
- `Nouvelle-Calédonie`
- `Polynésie Française`
- `Saint-Barthélémy`
- `Saint-Martin`
- `Saint-Pierre-et-Miquelon`
- `Wallis-et-Futuna`

Ces zones sont disponibles dans une constante :
```python
from jours_feries_france import JoursFeries

print(JoursFeries.ZONES)
# [
#     'Métropole', 'Alsace-Moselle', 'Guadeloupe',
#     'Guyane', 'Martinique', 'Mayotte', 'Nouvelle-Calédonie',
#     'La Réunion', 'Polynésie Française', 'Saint-Barthélémy',
#     'Saint-Martin', 'Wallis-et-Futuna', 'Saint-Pierre-et-Miquelon'
# ]
```

### Noms des jours fériés
Les noms des jours fériés sont fixés d'[après le code du travail](#sources).

Pour les zones `Métropole` (par défaut), `Nouvelle-Calédonie`, `Polynésie Française`, `Saint-Pierre-et-Miquelon` et `Wallis-et-Futuna`, les jours fériés sont orthographiés de la façon suivante :
- `1er janvier`
- `Lundi de Pâques`
- `1er mai`
- `8 mai`
- `Ascension`
- `Lundi de Pentecôte`
- `14 juillet`
- `Assomption`
- `Toussaint`
- `11 novembre`
- `Jour de Noël`

Pour la zone `Alsace-Moselle`, il existe 2 jours fériés supplémentaires, orthographiés de la façon suivante :
- `2ème jour de Noël`
- `Vendredi saint`

Pour les zones `Guadeloupe`, `Guyane`, `La Réunion`, `Martinique`, `Mayotte`, `Saint-Barthélémy` et `Saint-Martin`, il existe un jour férié supplémentaire, orthographié de la façon suivante :
- `Abolition de l'esclavage`

### Noms des méthodes Python

Vous pouvez calculer chaque jour férié individuellement à l'aide d'une méthode spécifique.

```python
from jours_feries_france import JoursFeries

year = 2020
zone = 'Métropole'

print("1er janvier", JoursFeries.premier_janvier(year))
print("1er mai", JoursFeries.premier_mai(year))
print("8 mai", JoursFeries.huit_mai(year))
print("14 juillet", JoursFeries.quatorze_juillet(year))
print("Assomption", JoursFeries.assomption(year))
print("Toussaint", JoursFeries.toussaint(year))
print("11 novembre", JoursFeries.onze_novembre(year))
print("Jour de Noël", JoursFeries.jour_noel(year))
print("Lundi de Pâques", JoursFeries.lundi_paques(year))
print("Ascension", JoursFeries.ascension(year))
print("Lundi de Pentecôte", JoursFeries.lundi_pentecote(year))
print("Vendredi saint", JoursFeries.vendredi_saint(year, zone))
print("2ème jour de Noël", JoursFeries.deuxieme_jour_noel(year, zone))
print("Abolition de l'esclavage", JoursFeries.abolition_esclavage(year, zone))
```

Certaines méthodes acceptent une `zone` en paramètre car ce jour férié est spécifique à certaines zones. Si ce jour férié n'est pas férié pour la zone passée en argument, vous aurez la valeur `None` en retour au lieu d'une date.

## Données
Si vous souhaitez simplement un export, consultez le jeu de données ["Jours fériés en France"](https://www.data.gouv.fr/fr/datasets/jours-feries-en-france/) sur data.gouv.fr.

## Sources
La liste des jours fériés est définie [dans le code du travail](#sources).

Certaines commémorations locales ou professionnelles sont également des jours fériés, parmi lesquelles :
- Saint-Éloi (reconnu jour férié par certaines conventions collectives dans la métallurgie) ;
- Sainte-Barbe (pour les salariés travaillant dans les mines) ;
- Mi-carême dans certains DOM.

Ces fêtes locales ou professionnelles ne sont pas disponibles dans cette librairie.

- [Code du travail : articles L3133-1 à L3133-3](https://www.legifrance.gouv.fr/affichCode.do?idSectionTA=LEGISCTA000033008129&cidTexte=LEGITEXT000006072050)
- [Code du travail - Article L3422-2](https://www.legifrance.gouv.fr/affichCodeArticle.do?idArticle=LEGIARTI000035902463&cidTexte=LEGITEXT000006072050)
