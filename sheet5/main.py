"""Relationship between life expectancy and GDP per capita"""
import numpy as np
import pandas as pd

url = ("https://raw.githubusercontent.com/swcarpentry/"
       "r-novice-gapminder/gh-pages/_episodes_rmd/data/gapminder_data.csv")

# What does the variable name "df" stand for? Hint: What type does the object have?
df = pd.read_csv(url)
# df.head()  # What does this method do?

df.sample(10)  # What does this method do?

# What does this line do? How did the DataFrame change?
df["logGdpPercap"] = np.log(df["gdpPercap"])
# What is the default kind of plot?
df.plot(x="lifeExp", y="logGdpPercap", kind="scatter")
