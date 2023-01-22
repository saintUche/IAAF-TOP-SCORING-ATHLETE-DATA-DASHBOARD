from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("mysql://{user}:{pw}@localhost:3306/{db}".format(user="root", pw="", db="eventRankings"))

all_athletes = pd.read_sql('SELECT * FROM Rankings', con=engine)


#creating country table

countries = all_athletes["Nat"].unique()

num_athletes_country = []
num_males_country = []
num_females_country = []
score_female_country = []
score_males_country = []
socre_total_country = []
no_events_country = []

for country in countries:

    country_athletes = all_athletes.loc[all_athletes['Nat'] == country]

    num_athletes = country_athletes.shape[0]

    male_athletes = country_athletes.loc[country_athletes["Sex"] == 'M']
    num_males = male_athletes.shape[0]

    female_athletes = country_athletes.loc[country_athletes["Sex"] == 'F']
    num_females = female_athletes.shape[0]
    
    score_male = male_athletes["Score"].sum()
    score_female = female_athletes["Score"].sum()
    score_total = country_athletes["Score"].sum()

    events = country_athletes["Discipline"].unique()
    no_events = events.shape[0]

    num_athletes_country.append(num_athletes)
    num_males_country.append(num_males) 
    num_females_country.append(num_females)
    score_female_country.append(score_female)
    score_males_country.append(score_male)
    socre_total_country.append(score_total)
    no_events_country.append(no_events)


country_dict = {

    "Nat" : countries,
    "AthleteCount": num_athletes_country,
    "Males" : num_males_country,
    "Females" : num_females_country,
    "ScoreMale" : score_males_country,
    "ScoreFemale": score_female_country,
    "ScoreTotal" : socre_total_country,
    "EventCount" : no_events_country

}

country_data = pd.DataFrame(data=country_dict)

db_connection = engine.connect()

try:
    country_data.to_sql("CountryData", db_connection, if_exists='append', index=False)

except ValueError as vx:
    print(vx)
    print("did not connect")

except Exception as ex:
    print(ex)
    print("did not connect")

else:
    ("Tables created successufully.")

finally:
    db_connection.close()
