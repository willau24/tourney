import csv
import random

class Country():
    def __init__(self, name, population, density, area):
        self.name = name
        self.population = population
        self.density = density
        self.area = area

    def __str__(self):
        return self.name

def parseCSV():
    categoryNames = []
    countries = []

    with open("countryData.csv") as file:
        reader = csv.reader(file, delimiter=',')
        count = 0
        for row in reader:
            if count == 0:
                num = len(row)
                for col in range(num):
                    categoryNames.append(row[col])
                count += 1
            else:
                countries.append(Country(row[0], row[1], row[2], row[3]))
    random.shuffle(countries)
    return categoryNames, countries

def compare(answer):
    countries = parseCSV()[1]
    index = countries.index(answer)








