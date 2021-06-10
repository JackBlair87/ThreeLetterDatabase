#Jack Blair 6/8/21

import subprocess
#This is a script to run all the necessary installs for REPLIT to correctly import the libraries used
try:
  from profanity_filter import ProfanityFilter
except:
  subprocess.run(["pip", "install", "profanity-filter"])
  subprocess.run(["python", "-m", "spacy", "download", "en"])

try:
  from search_engine_parser import GoogleSearch
except:
  subprocess.run(['pip', 'install', 'git+https://github.com/bisoncorps/search-engine-parser'])