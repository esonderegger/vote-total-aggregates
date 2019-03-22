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


def convert_combined():
    bodies = ['house', 'president', 'senate']
    states = {'all': {}}
    for body in bodies:
        filename = '1976-2016-{}.csv'.format(body)
        with open(filename) as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                po = row['state_po']
                if po not in states:
                    states[po] = {}
                if row['year'] not in states['all']:
                    states['all'][row['year']] = {}
                    for p in ['D', 'R', 'I']:
                        for b in bodies:
                            pbk = '{} ({})'.format(p, b)
                            states['all'][row['year']][pbk] = None
                if row['year'] not in states[po]:
                    states[po][row['year']] = {}
                    for p in ['D', 'R', 'I']:
                        for b in bodies:
                            pbk = '{} ({})'.format(p, b)
                            states[po][row['year']][pbk] = None
                row_votes = int(row['candidatevotes'])
                row_party = 'I'
                if row['party'] in party_aliases['D']:
                    row_party = 'D'
                if row['party'] in party_aliases['R']:
                    row_party = 'R'
                row_pbk = '{} ({})'.format(row_party, body)
                if states['all'][row['year']][row_pbk] is None:
                    states['all'][row['year']][row_pbk] = row_votes
                else:
                    states['all'][row['year']][row_pbk] += row_votes
                if states[po][row['year']][row_pbk] is None:
                    states[po][row['year']][row_pbk] = row_votes
                else:
                    states[po][row['year']][row_pbk] += row_votes
    for k in states.keys():
        with open('combined/{}.json'.format(k), 'w') as outfile:
            json.dump(states[k], outfile, sort_keys=True, indent=2)


if __name__ == '__main__':
    convert_house()
    convert_president()
    convert_combined()
