import pandas

data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirells = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirells = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirells = len(data[data['Primary Fur Color'] == 'Black'])

my_dict = {
    "Fur Colour": ['Gray', 'Cinnamon', 'Black'],
    "Count": [gray_squirells, red_squirells, black_squirells]
}

df = pandas.DataFrame(my_dict)
df.to_csv('fur_count2.csv')