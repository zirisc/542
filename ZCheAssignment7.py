import pandas as pd
get_csv = pd.read_csv(r'https://data.cityofnewyork.us/resource/yjub-udmw.csv')
get_csv.describe()

get_csv.pivot_table(index = "type",
                   columns = "boroname",
                   values = "objectid",
                   aggfunc = "count")

nba_data = pd.read_csv(r'https://raw.githubusercontent.com/odonnell31/NBA-Team-Strategies/main/data/nba_teams_data_1990_2020.csv')
nba_data.head()
nba_data[nba_data["Team"] == "New York Knicks"]

import matplotlib.pyplot as plt
knicks_data = nba_data[nba_data["Team"] == "New York Knicks"]
knicks_data.head(2)
x = knicks_data["Year"]
y = knicks_data["W"]

plt.plot(x, y)
plt.show()
