#Jack Blair 6/8/21
import sqlite3 as sl
import pickle

ALPHA = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

class WebsiteDatabase:
  def __init__(self):
    self.database = sl.connect('./Databases/Organizations/website-database.db')
    self.completion_list = './Databases/Organizations/completion-list.txt'
    self.db_name = "ENTRIES"

    f = open(self.completion_list,"rb")
    if not f.read(1):
      self.counts = dict()
    else:
      f.seek(0)
      self.counts = pickle.load(f)
    f.close()

  def add(self, entry, acronym):
    try:
      sql = 'INSERT INTO {0} (acronym, name, link, description) values(?, ?, ?, ?)'.format(self.db_name)
      data = (str(acronym), str(entry["titles"]), str(entry["links"]), str(entry["descriptions"]))
  
      with self.database:
          self.database.executemany(sql, [data])
      if acronym not in self.counts:
        self.counts[acronym] = 0
      self.counts[acronym] += 1

      f = open(self.completion_list,"wb")
      pickle.dump(self.counts, f)
      f.close()

    except:
      # print("Item is unoriginal")
      pass

  def __str__(self):
    output = ""
    for item in self.counts.keys():
      output += str(item) + ": " + str(self.counts[item]) + " entries \n" 
    return output

  def __repr__(self):
    output = ""
    with self.database:
        data = self.database.execute("SELECT * FROM {0}".format(self.db_name))
        for row in data:
            output += row[0] + " " + row[1] + "\n"
    return output

  def clear(self):
    if(input("Are you sure you want to proceed? (Y/N)") == "Y"):
      with self.database:
        self.database.execute("delete from {0}".format(self.db_name)).rowcount
      
      self.counts = dict()
      f = open(self.completion_list,"wb")
      pickle.dump(self.counts, f)
      f.close()

  def create_table(self):
    with self.database:
      self.database.execute("CREATE TABLE {0} (acronym TEXT, name TEXT, link TEXT, description TEXT, PRIMARY KEY (acronym, name, link));".format(self.db_name))

  def specific_acronym(self, acronym):
    with self.database:
        try:
            data = self.database.execute("SELECT * FROM {0} WHERE acronym = \'{1}\'".format(self.db_name, acronym))
        except sl.OperationalError:
            return []
    return list(data)

  def contains(self, acronym):
    if acronym in self.counts:
      if self.counts[acronym] > 30:
        return True
    return False

  def percent_collected(self):
    count = 0
    correct = 0

    for x in ALPHA:
      for y in ALPHA:
        for z in ALPHA:
          count += 1
          if self.contains(x + y + z):
            correct += 1

    return str(correct/count * 100)[0:5] + "%"
