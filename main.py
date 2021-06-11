import installs
from search_engine_parser import GoogleSearch
from profanity_filter import ProfanityFilter
from Databases.Organizations.websiteDatabase import WebsiteDatabase
from web_searcher import WebSearcher
from multiprocessing import Pool
import time

# import Databases.Colleges.CollegeFinder
import Databases.Stocks.stocksProcessor

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
REVERSED_ALPHA = "".join(reversed(ALPHA)) 
DATABASE = WebsiteDatabase()
PF = ProfanityFilter()
WS = WebSearcher()

def google_all():
    count = 0
    for y in ALPHA:
        for z in ALPHA:
            acronym = "I" + y + z
            if PF.is_clean(acronym):
              print(acronym)

              try:
                results = WS.search(acronym)
                print(len(results))

                for item in results:
                  DATABASE.add(item, acronym)
                count += 1
              except Exception as e:
                print(e)
              
              print(str(DATABASE)[-100:])
            
            # time.sleep(5)

        if count > 200:
          break

def google_wanted():
  count = 0
  for x in ALPHA:
    for y in ALPHA:
      for z in ALPHA:
        acronym = x + y + z
        if PF.is_clean(acronym) and not DATABASE.contains(acronym):
          print(acronym)

          try:
            results = WS.search(acronym)
            print(len(results))

            for item in results:
              DATABASE.add(item, acronym)
            count += 1
          except Exception as e:
            print(e)
          
          print(str(DATABASE)[-100:])
          print(DATABASE.percent_collected())
        
        if count > 200:
          break

def googlar(acronym):
  if PF.is_clean(acronym) and not DATABASE.contains(acronym):
    print(acronym)

    try:
      results = WS.search(acronym)
      print(len(results))

      for item in results:
        DATABASE.add(item, acronym)
      print(DATABASE.percent_collected())
      print()

    except Exception as e:
      # print(e)
      pass
    
    # print(str(DATABASE)[-100:])
        
            

if __name__=="__main__":
  # google_wanted()


  # values = []

  # for x in ALPHA:
  #   for y in ALPHA:
  #     for z in ALPHA:
  #       values.append(x + y + z)

  # print(values)

  # with Pool() as pool:
  #     res = pool.map(googlar, values)

  # print(str(DATABASE))
  # print(DATABASE.percent_collected())
  pass