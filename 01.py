import matplotlib as mpl

mpl.rc("axes", labelsize=14)

import pandas as pd

oecd_bli = pd.read_csv("./datasets/lifesat/oecd_bli_2015.csv", thousands=",")
print(oecd_bli.head(), end="\n")
oecd_bli.info()
print(oecd_bli["INEQUALITY"].value_counts(), end="\n")

oecd_bli = oecd_bli[oecd_bli["INEQUALITY"] == "TOT"]
oecd_bli.info()

oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
print(oecd_bli.head(), end="\n")

gdp_per_capita = pd.read_csv("./datasets/lifesat/gdp_per_capita.csv", thousands=",", delimiter="\t", encoding="latin1",
                             na_values="n/a", )
gdp_per_capita.info()

gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
print(gdp_per_capita.head(), end="\n")
gdp_per_capita.set_index("Country", inplace=True)
print(gdp_per_capita.head(), end="\n")
