import csv


def data(filename, max_field, min_field, name_field):
    with open(filename, 'rU') as csvfile:
        for row in csv.DictReader(csvfile):
            yield (
                    abs(int(row[max_field]) - int(row[min_field])),
                    row[name_field])


if __name__=='__main__':
    print sorted(data(
        'parsing-data/football.csv',
        'Goals', 'Goals Allowed', 'Team'
        ))[0][1]
    print sorted(data(
        'parsing-data/weather.csv',
        'MxT', 'MnT', 'Day'
        ))[0][1]
