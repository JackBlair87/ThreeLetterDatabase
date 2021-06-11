#Jack Blair 6/11/21
from web_searcher import WebSearcher
from Databases.DatabaseGenerator import Database

WS = WebSearcher()
DATABASE = Database("Airports", 1)
US_AIRPORTS = "./Databases/Airports/airport-codes-US.txt"

with open(US_AIRPORTS) as f:
  for line in f:
    airport = line.split("(", 1)[0].strip()
    acronym = line.split("(", 1)[1].strip()[:-1]
    print(acronym, airport)

    #webscrape this website
    #https://www.airnav.com/airport/KGAI


    #   try:
    #     print(acronym)
    #     result = WS.plain_search(acronym.strip() + " website")[0]
    #     DATABASE.add(acronym, (university, result['links'].split("=", 1)[1], result['descriptions'], ""))
    #   except Exception as e:
    #     print(acronym, e)

print(str(DATABASE))
print(repr(DATABASE))