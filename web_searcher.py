from search_engine_parser import GoogleSearch

class WebSearcher:
  def __init__(self):
    self.gsearch = GoogleSearch()
  
  def google(self, query : str):
      return self.gsearch.search(query, 1, cache = False)

  def search(self, acronym : str):
    items = self.google(acronym + " organization")
    items2 = self.google(acronym)
    return [item for item in items] + [item for item in items2]

  def plain_search(self, acronym : str):
    items = self.google(acronym)
    return [item for item in items]
