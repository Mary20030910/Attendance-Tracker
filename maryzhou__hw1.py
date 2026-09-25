"""
name: Mary Zhou
andrewID: maryzhou
"""

def parse_record(record: str) -> dict:
    fields = record.strip().split(",")
    if len(fields) != 4:
        return None
    for item in fields:
        if item.strip() == "":
            return None

    name = fields[0].strip()
    year = fields[1].strip()
    event = fields[2].strip()
    hours = fields[3].strip()

    if not year.isdigit():
        return None
    else:
        year = int(year)

    if year < 1 or year > 4:
        return None

    try:
        hours = float(hours)
    except ValueError:
        return None

    if hours <= 0:
        return None

    return {
        "name": name,
        "year": year,
        "event": event,
        "hours": hours
    }