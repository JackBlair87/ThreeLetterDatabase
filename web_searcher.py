from search_engine_parser import GoogleSearch

class WebSearcher:
  def __init__(self):
    self.gsearch = GoogleSearch()
  
  def google(self, query : str):
      return self.gsearch.search(query, 1, cache = False)

  def search(self, acronym : str):
    items = self.google(acronym + " acronym")
    
    items2 = self.google(acronym + " organization")
    items3 = self.google(acronym)
    return [item for item in items3] + [item for item in items2] + [item for item in items]

  def plain_search(self, acronym : str):
    items = self.google(acronym)
    return [item for item in items]


# def search(term, max_tries = 50):
#     for x in range(max_tries):
#         print("Searching {0} (Attempt {1})...".format(term, x+1))
#         search_results = google.search(term, 8)
#         print(search_results)
#         print('Length of search_results:', len(search_results))
#         if len(search_results) > 0:
#             return search_results
#     raise RuntimeError("Search on term {0} did not work!".format(str(term)))

