import csv
import json


party_aliases = {
    'D': [
        'democrat',
        'democratic-farmer-labor',
        'working families',
    ],
    'R': [
        'republican',
        'conservative',
    ],
}


def convert_house():
    filename = '1976-2016-house.csv'
    states = {'all': {}}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            po = row['state_po']
            if po not in states:
                states[po] = {}
            if row['year'] not in states['all']:
                states['all'][row['year']] = {'D': 0, 'R': 0, 'I': 0}
            if row['year'] not in states[po]:
                states[po][row['year']] = {'D': 0, 'R': 0, 'I': 0}
            row_votes = int(row['candidatevotes'])
            if row['party'] in party_aliases['D']:
                states['all'][row['year']]['D'] += row_votes
                states[po][row['year']]['D'] += row_votes
            elif row['party'] in party_aliases['R']:
                states['all'][row['year']]['R'] += row_votes
                states[po][row['year']]['R'] += row_votes
            else:
                states['all'][row['year']]['I'] += row_votes
                states[po][row['year']]['I'] += row_votes
    for k in states.keys():
        with open('house/{}.json'.format(k), 'w') as outfile:
            json.dump(states[k], outfile, sort_keys=True, indent=2)


def convert_president():
    filename = '1976-2016-president.csv'
    states = {'all': {}}
    with open(filename) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            po = row['state_po']
            if po not in states:
                states[po] = {}
            if row['year'] not in states['all']:
                states['all'][row['year']] = {'D': 0, 'R': 0, 'I': 0}
            if row['year'] not in states[po]:
                states[po][row['year']] = {'D': 0, 'R': 0, 'I': 0}
            row_votes = int(row['candidatevotes'])
            if row['party'] in party_aliases['D']:
                states['all'][row['year']]['D'] += row_votes
                states[po][row['year']]['D'] += row_votes
            elif row['party'] in party_aliases['R']:
                states['all'][row['year']]['R'] += row_votes
                states[po][row['year']]['R'] += row_votes
            else:
                states['all'][row['year']]['I'] += row_votes
                states[po][row['year']]['I'] += row_votes
    for k in states.keys():
        with open('president/{}.json'.format(k), 'w') as outfile:
            json.dump(states[k], outfile, sort_keys=True, indent=2)


if __name__ == '__main__':
    # convert_house()
    convert_president()
