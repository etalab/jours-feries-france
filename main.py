import os
import json
import datetime
from collections import defaultdict

import pandas as pd
from ics import Calendar, Event
from jours_feries_france import JoursFeries
from slugify import slugify


def to_csv(df, filename):
    df.sort_values(by="date").to_csv(filename, index=False, encoding="utf-8")


def add_event(calendar, name, date):
    event = Event()
    event.name = name
    event.begin = date.strftime("%Y-%m-%d")
    event.make_all_day()
    calendar.events.add(event)


def write_calendar(calendar, filename, name):
    content = str(calendar).split("\n")

    # Add calendar name
    content.insert(2, f"NAME:{name}\r")
    content.insert(2, f"X-WR-CALNAME:{name}\r")

    with open(filename, "w") as f:
        f.writelines(content)


def write_json(filename, bank_holidays):
    with open(filename, "w") as f:
        json.dump(
            {k.strftime("%Y-%m-%d"): v for k, v in bank_holidays.items()},
            f,
            ensure_ascii=False,
        )


current_year = datetime.date.today().year
START, END = -20, 5

os.makedirs("data/csv", exist_ok=True)
os.makedirs("data/ics", exist_ok=True)
all_dates = defaultdict(list)
for zone, zone_slug in [(z, slugify(z)) for z in JoursFeries.ZONES]:
    os.makedirs(f"data/json/{zone_slug}", exist_ok=True)

    csv_data = []
    json_data = {}
    calendar = Calendar()
    calendar.creator = "Etalab"
    for year in range(current_year + START, current_year + END + 1):
        bank_holidays = JoursFeries.for_year(year, zone)

        for nom_jour_ferie, the_date in bank_holidays.items():
            # Generate ICS calendar only from 5 years ago to 5 years in the future
            is_recent = the_date.year in range(current_year - 5, current_year + 6)
            if is_recent:
                add_event(calendar, nom_jour_ferie, the_date)

            csv_data.append(
                {
                    "date": the_date.strftime("%Y-%m-%d"),
                    "annee": str(the_date.year),
                    "zone": zone,
                    "nom_jour_ferie": nom_jour_ferie,
                }
            )
            all_dates[(the_date.strftime("%Y-%m-%d"), nom_jour_ferie)].append(zone)

        json_for_year = {v: k for k, v in bank_holidays.items()}
        write_json(f"data/json/{zone_slug}/{year}.json", json_for_year)
        json_data = {**json_for_year, **json_data}

    to_csv(pd.DataFrame(csv_data), f"data/csv/jours_feries_{zone_slug}.csv")
    write_json(f"data/json/{zone_slug}.json", json_data)

    write_calendar(
        calendar, f"data/ics/jours_feries_{zone_slug}.ics", f"Jours fériés {zone}"
    )

res = []
for (date, name), zones in all_dates.items():
    res.append({"date": date, "nom_jour_ferie": name, "zones": "|".join(zones)})
to_csv(pd.DataFrame(res), f"data/csv/jours_feries.csv")
