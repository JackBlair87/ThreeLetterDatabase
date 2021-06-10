#Jack Blair 6/8/21
import sqlite3 as sl
from web_searcher import WebSearcher
import pickle

WS = WebSearcher()
DATABASE = sl.connect('./Databases/Colleges/college-database.db')
COLLEGES = "./Databases/Colleges/college-abreviations.txt"

with open(COLLEGES) as f:
  for line in f:
    # print(line)
    # print(line.split("-", 1))
    acronym = line.split("-", 1)[0]
    university = line.split("-", 1)[1]
    if len(acronym.strip()) == 3:
      print(acronym.strip(), university.strip())
      result = WS.plain_search(acronym.strip() + " website")[0]
      print(result['link'].split("=", 1)[1])
