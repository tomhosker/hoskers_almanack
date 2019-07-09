### This code holds a class which builds the LaTeX code for the Almanack's
### various months.

# Imports.
import sqlite3

# Local imports.
import constants
from article import Article

# Constants.
all_selects = dict()
pri1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
pri2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
pri3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
pri = [pri1, pri2, pri3]
all_selects["Primilis"] = pri
sec1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
sec2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
sec3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
sec = [sec1, sec2, sec3]
all_selects["Sectilis"] = sec
ter1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
ter2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
ter3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
ter = [ter1, ter2, ter3]
all_selects["Tertilis"] = ter
qua1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"english folk\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
qua2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 58 "+
        "ORDER BY ranking DESC;")
qua3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
qua = [qua1, qua2, qua3]
all_selects["Quartilis"] = qua
qui1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"scots-irish folk\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
qui2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"shanty\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
qui3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
qui = [qui1, qui2, qui3]
all_selects["Quintilis"] = qui
sex1 = ("SELECT id FROM article "+
        "WHERE (type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"imperial folk\" "+
          "AND ranking BETWEEN 1 AND 19) "+
        "OR (type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"hymn\" "+
          "AND ranking BETWEEN 1 AND 10) "+
        "ORDER BY aux_type, ranking DESC;")
sex2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
sex3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking DESC;")
sex = [sex1, sex2, sex3]
all_selects["Sextilis"] = sex
sep1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
sep2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
sep3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
sep = [sep1, sep2, sep3]
all_selects["September"] = sep
oct1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"october\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
oct2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"october\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
oct3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"october\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
octo = [oct1, oct2, oct3]
all_selects["October"] = octo
nov1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
nov2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
nov3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
nov = [nov1, nov2, nov3]
all_selects["November"] = nov
dec1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
dec2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
dec3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
dec = [dec1, dec2, dec3]
all_selects["December"] = dec
uno1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
uno2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
uno3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
uno = [uno1, uno2, uno3]
all_selects["Unodecember"] = uno
duo1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
duo2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
duo3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
duo = [duo1, duo2, duo3]
all_selects["Duodecember"] = duo
int1 = ("SELECT id FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"intercalaris\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
int2 = ("SELECT id FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"intercalaris\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
int3 = ("SELECT id FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"intercalaris\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
inter = [int1, int2, int3]
all_selects["Intercalaris"] = inter

# A helper class.
class Month:
  def __init__(self, name, intro, articles, fullness, mods):
    self.name = name
    self.intro = intro
    self.songs = articles["songs"]
    self.sonnets = articles["sonnets"]
    self.proverbs = articles["proverbs"]
    self.fullness = fullness
    self.mods = mods
    self.printout = self.build_printout()

  def build_printout(self):
    lengths = [len(self.songs), len(self.sonnets), len(self.proverbs)]
    n = min(lengths)
    result = "\\chapter{"+self.name+"}\n\n"+self.intro+"\n\n"
    for i in range(n):
      song_obj = Article(self.songs[i], self.fullness, self.mods)
      sonnet_obj = Article(self.sonnets[i], self.fullness, self.mods)
      proverb_obj = Article(self.proverbs[i], self.fullness, self.mods)
      song = song_obj.digest()
      sonnet = sonnet_obj.digest()
      proverb = proverb_obj.digest()
      result = result+"\\bigskip\n\\bigskip\n\\section{}\n\n"
      result = result+"\\subsection{}\n\n"+song+"\n\n"
      result = result+"\\subsection{}\n\n"+sonnet+"\n\n"
      result = result+"\\subsection{}\n\n"+proverb+"\n\n"
    return result

  def digest(self):
    return self.printout

# The class in question.
class Month_builder:
  def __init__(self, fullness, mods):
    self.fullness = fullness
    self.mods = mods
    conn = sqlite3.connect(constants.db)
    self.c = conn.cursor()
    self.primilis = self.build_month("Primilis")
    self.sectilis = self.build_month("Sectilis")
    self.tertilis = self.build_month("Tertilis")
    self.quartilis = self.build_month("Quartilis")
    self.quintilis = self.build_month("Quintilis")
    self.sextilis = self.build_month("Sectilis")
    self.september = self.build_month("September")
    self.october = self.build_month("October")
    self.november = self.build_month("November")
    self.december = self.build_month("December")
    self.unodecember = self.build_month("Unodecember")
    self.duodecember = self.build_month("Duodecember")
    self.intercalaris = self.build_month("Intercalaris")
    conn.close()

  # Fetches the month's introduction from the database.
  def fetch_intro(self, month_name):
    select = "SELECT content FROM month_intros WHERE month_name = ?;"
    self.c.execute(select, (month_name,))
    extract = self.c.fetchone()
    result = extract[0]
    return result

  # Fetches a given months articles from the database.
  def fetch_articles(self, selects):
    result = dict()
    # Songs.
    select = selects[0]
    self.c.execute(select)
    extract = self.c.fetchall()
    songs = []
    for item in extract:
      songs.append(item[0])
    result["songs"] = songs
    # Sonnets.
    select = selects[1]
    self.c.execute(select)
    extract = self.c.fetchall()
    sonnets = []
    for item in extract:
      sonnets.append(item[0])
    result["sonnets"] = sonnets
    # Proverbs.
    select = selects[2]
    self.c.execute(select)
    extract = self.c.fetchall()
    proverbs = []
    for item in extract:
      proverbs.append(item[0])
    result["proverbs"] = proverbs
    return result

  # Ronseal.
  def build_month(self, name):
    intro = self.fetch_intro(name)
    articles = self.fetch_articles(all_selects[name])
    result = Month(name, intro, articles, self.fullness, self.mods).digest()
    return result

  # Wrap all months into one string.
  def digest(self):
    result = (self.primilis+self.sectilis+self.tertilis+self.quartilis+
              self.quintilis+self.sextilis+self.september+self.october+
              self.november+self.december+self.unodecember+self.duodecember+
              self.intercalaris)
    return result

# Run a demo.
def demo():
  mb = Month_builder("full")
  print(mb.digest())

# Run and wrap up.
def run():
  demo()
#run()
