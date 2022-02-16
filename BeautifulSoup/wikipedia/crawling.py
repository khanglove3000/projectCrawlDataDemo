from bs4 import BeautifulSoup
import requests
import pandas as pd
import json
import numpy as np

# get html data first
html_data = requests.get("https://en.wikipedia.org/wiki/World_Happiness_Report")

# check if status is 200 -> shows that its allowed to scrape the webpage
print(html_data.status_code)

# parse html data now using BeautifulSoup
soup = BeautifulSoup(html_data.text, "html.parser")

# get all tables from wikipedia page
tables = soup.find_all('table',{'class':"wikitable"})

# store target table
table = tables[0]

# convert table html code to pandas df
data = pd.read_html(str(table))
df_happiness = pd.DataFrame(data[0]) 


#=======================================

from tqdm import tqdm

# rename some countries to later match the country names from RapidAPI
df_happiness = df_happiness.apply(lambda x: x.replace("Congo (Kinshasa)", "DR Congo"))
df_happiness = df_happiness.apply(lambda x: x.replace("Congo (Brazzaville)", "Congo"))
df_happiness = df_happiness.apply(lambda x: x.replace("Ivory Coast", "Côte d'Ivoire"))

# create URL and headers for API call
url = "https://world-population.p.rapidapi.com/population"

# the headers can be found when logging in to your RapidAPI account and opening the link above
headers = {
    'x-rapidapi-host': "world-population.p.rapidapi.com",
    'x-rapidapi-key': "***************************"
}

# add population column first by setting all values to NaN
df_happiness["Population"] = np.nan

# loop over countries and get population
for country in tqdm(df_happiness["Country or region"].to_list()):
    # create querystring for API call
    querystring = {"country_name" : country}
    
    # create request and fetch response
    response = requests.request("GET", url, headers=headers, params=querystring)
    
    # add population to dataframe in case response is okay
    response_dict = json.loads(response.text)
    if response_dict== True:
        population = response_dict["body"]["population"]
        df_happiness.loc[df_happiness["Country or region"] == country, "Population"] = population

#================================

html_data = requests.get("https://www.worlddata.info/average-age.php")

# check if status is 200 -> shows that its allowed to scrape the webpage
print(html_data.status_code)

# parse html data now using BeautifulSoup
soup = BeautifulSoup(html_data.text, "html.parser")

# get all tables from wikipedia page
tables = soup.find_all('table',{'class':"std100 hover"})

# store target table
table = tables[0]

# convert table html code to pandas df
data = pd.read_html(str(table))
df_average_age = pd.DataFrame(data[0]) 


# let's use pandas join functionality for joining these tables together
df_final = df_happiness.set_index("Country or region").join(df_average_age.set_index("Country")).reset_index()

# Transform
# Compute GDP by using GDP per capita and the Population columns
df_final["GDP"] = df_final["GDP per capita"] * df_final["Population"]

# Remove % sign of Population under 20 years old column and convert it to be of type float
def transform_col(col_val):
    try: 
        return float(col_val.replace(" %", ""))
    except: # value is NaN
        return col_val

df_final["Population under 20 years old in %"] = df_final["Population under20 years old"].apply(transform_col)
df_final = df_final.drop(columns=["Population under20 years old"])


# Load
def load(dataset):
    dataset.to_csv("final_dataset.csv", index=False)

load(df_final)