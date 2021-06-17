import installs
from pathlib import Path

root_directory = Path('.')
size = sum(f.stat().st_size for f in root_directory.glob('**/*') if f.is_file())

print(size, "Bytes")
print(size//1000000, "MB")


import Databases.Colleges.CollegeFinder
import Databases.Stocks.stocksProcessor
# import Databases.Airports.airportGenerator
import Databases.Organizations.OrganizationFinder

            

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