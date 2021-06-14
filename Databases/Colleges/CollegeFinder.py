#Jack Blair 6/8/21
from web_searcher import WebSearcher
from Databases.DatabaseGenerator import Database

WS = WebSearcher()
DATABASE = Database("Colleges", 1)
COLLEGES = "./Databases/Colleges/college-abreviations.txt"

print("College Database Complete")

# with open(COLLEGES) as f:
#   for line in f:
#     acronym = line.split("-", 1)[0].strip()
#     university = line.split("-", 1)[1].strip()
    
#     if len(acronym) == 3:
#       try:
#         print(acronym)
#         result = WS.plain_search(acronym.strip() + " website")[0]
#         DATABASE.add(acronym, (university, result['links'].split("=", 1)[1], result['descriptions'], ""))
#       except Exception as e:
#         print(acronym, e)

# print(str(DATABASE))
# print(repr(DATABASE))