#Jack Blair 6/16/21
from web_searcher import WebSearcher
from Databases.DatabaseGenerator import Database
from profanity_filter import ProfanityFilter

PF = ProfanityFilter()
WS = WebSearcher()
DATABASE = Database("Organizations", 1)

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def google_remaining(ammount : int):
  count = 0
  for x in ALPHA:
    for y in ALPHA:
      for z in ALPHA:
        acronym = x + y + z
        if PF.is_clean(acronym) and not DATABASE.contains(acronym):
          print("Searching", acronym)

          try:
            results = WS.search(acronym)
            print(len(results))
            for item in results:
              DATABASE.add(acronym, item)
            count += 1
          except Exception as e:
            print("Failed on " + acronym + " --> ", e)
          
          print(str(DATABASE)[-100:])
          print(DATABASE.percent_collected(len(ALPHA) ** 3))
        
        if count > ammount:
          return

google_remaining(3)
print(repr(DATABASE))