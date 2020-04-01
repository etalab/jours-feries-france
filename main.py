import os
import json
import datetime

import pandas as pd
from ics import Calendar, Event
from jours_feries_france import JoursFeries
from slugify import slugify


def to_csv(df, filename):
    df.to_csv(filename, index=False, encoding="utf-8")


def add_event(calendar, name, date):
    event = Event()
    event.name = name
    event.begin = date.strftime("%Y-%m-%d")
    event.make_all_day()
    calendar.events.add(event)


current_year = datetime.date.today().year
START, END = -50, 5

os.makedirs("data/csv", exist_ok=True)
os.makedirs("data/ics", exist_ok=True)
for zone in JoursFeries.ZONES:
    zone_slug = slugify(zone)
    os.makedirs(f"data/json/{zone_slug}", exist_ok=True)

    data = []
    calendar = Calendar()
    for year in range(current_year + START, current_year + END + 1):
        bank_holidays = JoursFeries.for_year(year, zone)

        for nom_jour_ferie, the_date in bank_holidays.items():
            is_recent = the_date.year in range(current_year - 5, current_year + 6)

            # Generate ICS calendar only from 5 years ago to 5 years in the future
            if is_recent:
                add_event(calendar, nom_jour_ferie, the_date)

            data.append(
                {
                    "date": the_date.strftime("%Y-%m-%d"),
                    "zone": zone,
                    "nom_jour_ferie": nom_jour_ferie,
                }
            )

        with open(f"data/json/{zone_slug}/{year}.json", "w") as f:
            json.dump(
                {k.strftime("%Y-%m-%d"): k for k, v in bank_holidays.items()},
                f,
                ensure_ascii=False,
            )

    df = pd.DataFrame(data)
    to_csv(df, f"data/csv/jours_feries_{zone_slug}.csv")

    with open(f"data/ics/jours_feries_{zone_slug}.ics", "w") as my_file:
        my_file.writelines(calendar)
