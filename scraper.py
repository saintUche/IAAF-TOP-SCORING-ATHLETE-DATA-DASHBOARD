import pandas as pd
import datetime


#Getting the data

def fetch_page(sex, page_number):
    BASE_URL = "https://www.worldathletics.org/world-rankings/overall-ranking/" + sex + "?regionType=world&page=" + page_number + "&rankDate=2023-01-10&limitByCountry=0"
    url = BASE_URL
    return url

def get_data(sex, pages):

   dataframes = []
   
   for num in pages:
    page = pd.read_html(fetch_page(sex, num))
    result_table = page[0]
    dataframes.append(result_table)

   
   combined_table = pd.concat(dataframes)

   return combined_table


page_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

males = get_data("men", page_numbers)
females = get_data("female", page_numbers)


#Data preperation

sexm = 1000*["M"]
sexf = 1000*["F"]

# Add a sex column to competititors
males["Sex"] = sexm
females["Sex"] = sexf

all_athletes = pd.concat([males, females]).drop(["Place"],  axis="columns")
all_athletes = all_athletes.rename(columns={"Event List": "Discipline"})

#convert birth date from string to date
try:
    all_athletes["DOB"] = pd.to_datetime(all_athletes["DOB"], dayfirst=True, utc=False)

except ValueError as vx:
    print(vx)

except Exception as ex:
    print(ex)

else:
    ("dates converted")


# added a column to distinguish whether athlete is a junior or not.

cut_off_date = datetime.datetime(2003, 1, 1)

all_athletes["Jr"] = all_athletes["DOB"].apply(lambda x: x >= cut_off_date)