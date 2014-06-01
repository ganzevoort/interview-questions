import csv


def data(filename):
    with open(filename, 'rU') as csvfile:
        for row in csv.DictReader(csvfile):
            print row
            yield (
                    abs(int(row['MxT']) - int(row['MnT'])),
                    row['Day'])


if __name__=='__main__':
    print sorted(data('parsing-data/weather.csv'))[0][1]
