import csv


def data(filename):
    with open(filename, 'rU') as csvfile:
        for row in csv.DictReader(csvfile):
            yield (
                    abs(int(row['Goals']) - int(row['Goals Allowed'])),
                    row['Team'])


if __name__=='__main__':
    print sorted(data('parsing-data/football.csv'))[0][1]
