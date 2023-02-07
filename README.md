# IAAF-TOP-SCORING-ATHLETE-DATA-DASHBOARD
Uses collected data from official page of International Association of Athletics Federation to showcase performance of countries in relation to other varibales such as number of athletes or number of event in a dashboard created in powerBI.


## Inspiration 

I wanted to see how different countries produced top scoring athletes from the 2021/2022 athletics season. I took the top 1000 scoring male athletes and top 1000 scoring female athletes from IAAF ranking page ( female : https://worldathletics.org/world-rankings/overall-ranking/women?regionType=world&page=1&rankDate=2023-01-17&limitByCountry=0 , male: https://worldathletics.org/world-rankings/overall-ranking/men?regionType=world&page=1&rankDate=2023-01-17&limitByCountry=0).

## How IAAF scoring system works:

https://www.worldathletics.org/world-ranking-rules/basics


## Data Pipeline

Web -> Python -> SQL -> PowerBI
 
### Getting the data 

(scrapper.py)

I created a web scraper using pandas function 'read_html'. 
The base URL was found allowing to get the data across the different tables by changing the URL where necessary.


### Data preparation/manipulation

(scrapper.py)

I removed and added new data column(s) where necessary.  
I also made sure the column values were in their necessary data types.

(rankingsSchema.sql)

Here more tables were creaated based off of other column values.

(webDataToSQL.py)

Here data was manipulation so that information based off countries could be obtained.

### Data visualisations 

The visualisations were carried out in powerBI


## Findings 

![image](https://user-images.githubusercontent.com/79328765/214068903-86fa9853-4b43-4977-bedb-36119c1e9dd1.png)



From the visualisation we can conclude:

- USA was the most successful country
- The number of athletes is very closesly related to the country score
- The number of events a country competes in is cloesly related to country score
- Most top scoring athletes are senior athletes 
- Kenya has the highest scoring juniors 








