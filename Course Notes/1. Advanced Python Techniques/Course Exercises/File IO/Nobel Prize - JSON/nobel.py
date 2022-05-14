def load_nobel_prizes(filename='prize.json'):
    with open(filename) as f:
        return json.load(f)


def main(year, category):
    data = load_nobel_prizes()
    prizes = data['prizes']

    for prize in prizes:
        if 'laureates' not in prize:
            continue
        if category and prize['category'].lower() != category.lower():
            continue
        if year and prize['year'] != year:
            continue

        print(f"{prize['year']} Nobel Prize in {prize['category'].title()}")
        for laureate in prize['laureates']:
            firstname = laureate['firstname']
            surname = laureate.get('surname', '')
            print(f"{firstname} {surname}: {laureate['motivation']}")