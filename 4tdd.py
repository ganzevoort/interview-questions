import csv
import unittest


class GenericCSV(object):
    def __init__(self):
        self.header = []
        self.data = []
        with open(self.filename, 'rU') as csvfile:
            for i, row in enumerate(csv.reader(csvfile)):
                if i == 0:
                    self.header = row
                else:
                    self.data.append(row)

    def value_annotated(self):
        return [(self.value(row), row) for row in self.data]

    def best_value(self):
        value, row = sorted(self.value_annotated())[0]
        return row

    def best_value_name(self):
        return self.best_value()[0]


class FootballCSV(GenericCSV):
    filename = 'parsing-data/football.csv'

    def value(self, row):
        row = dict(zip(self.header, row))
        return abs(int(row['Goals Allowed']) - int(row['Goals']))


class WeatherCSV(GenericCSV):
    filename = 'parsing-data/weather.csv'

    def value(self, row):
        return int(row[1]) - int(row[2])


class TestFootballCSV(unittest.TestCase):
    def setUp(self):
        self.csv = FootballCSV()

    def test_namefield(self):
        self.assertTrue('Team' in self.csv.header)

    def test_team_is_column_0(self):
        self.assertEqual(self.csv.header[0], 'Team')

    def test_team_arsenal(self):
        team_names = [row[0] for row in self.csv.data]
        self.assertTrue('Arsenal' in team_names)

    def test_value(self):
        for row in self.csv.data:
            if row[0]=='Arsenal':
                self.assertEqual(self.csv.value(row), 43)

    def test_best_value(self):
        best_row = self.csv.best_value()
        best_value = self.csv.value(best_row)
        self.assertEqual(len(best_row), len(self.csv.header))
        for row in self.csv.data:
            self.assertGreaterEqual(self.csv.value(row), best_value)


class TestWeatherCSV(unittest.TestCase):
    def setUp(self):
        self.csv = WeatherCSV()

    def test_columns(self):
        self.assertEqual(self.csv.header[:3], ['Day', 'MxT', 'MnT'])

    def test_value(self):
        for row in self.csv.data:
            self.assertGreaterEqual(self.csv.value(row), 0)

    def test_best_value(self):
        best_row = self.csv.best_value()
        best_value = self.csv.value(best_row)
        self.assertEqual(len(best_row), len(self.csv.header))
        for row in self.csv.data:
            self.assertGreaterEqual(self.csv.value(row), best_value)


if __name__ == '__main__':
    print FootballCSV().best_value_name()
    print WeatherCSV().best_value_name()
    unittest.main()

