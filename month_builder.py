### This code holds a class which builds the LaTeX code for the Almanack's
### various months.

# Imports.
import sqlite3

# Local imports.
from hpml.hpml_compiler import HPML_compiler
from encapsulator import Mini_encapsulator

# Constants.
all_selects = dict()
pri1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
pri2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
pri3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
pri = [pri1, pri2, pri3]
all_selects["Primilis"] = pri
sec1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
sec2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
sec3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking;")
sec = [sec1, sec2, sec3]
all_selects["Sectilis"] = sec
ter1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
ter2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
ter3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 89 "+
        "ORDER BY ranking;")
ter = [ter1, ter2, ter3]
all_selects["Tertilis"] = ter
qua1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"english folk\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
qua2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 58 "+
        "ORDER BY ranking DESC;")
qua3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
qua = [qua1, qua2, qua3]
all_selects["Quartilis"] = qua
qui1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"scots-irish folk\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
qui2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"shanty\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
qui3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking DESC;")
qui = [qui1, qui2, qui3]
all_selects["Quintilis"] = qui
sex1 = ("SELECT content FROM article "+
        "WHERE (type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"american folk\" "+
          "AND ranking BETWEEN 1 AND 19) "+
        "OR (type = 1 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"hymn\" "+
          "AND ranking BETWEEN 1 AND 10) "+
        "ORDER BY aux_type, ranking DESC;")
sex2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
sex3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"blood\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 59 "+
        "ORDER BY ranking DESC;")
sex = [sex1, sex2, sex3]
all_selects["Sextilis"] = sex
sep1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
sep2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
sep3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 30 "+
        "ORDER BY ranking;")
sep = [sep1, sep2, sep3]
all_selects["September"] = sep
oct1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"october\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
oct2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"october\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
oct3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"october\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking;")
octo = [oct1, oct2, oct3]
all_selects["October"] = octo
nov1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
nov2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
nov3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"phlegm\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 31 AND 60 "+
        "ORDER BY ranking;")
nov = [nov1, nov2, nov3]
all_selects["November"] = nov
dec1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
dec2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
dec3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 60 AND 88 "+
        "ORDER BY ranking DESC;")
dec = [dec1, dec2, dec3]
all_selects["December"] = dec
uno1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
uno2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
uno3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 30 AND 59 "+
        "ORDER BY ranking DESC;")
uno = [uno1, uno2, uno3]
all_selects["Unodecember"] = uno
duo1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
duo2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
duo3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"black bile\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
duo = [duo1, duo2, duo3]
all_selects["Duodecember"] = duo
int1 = ("SELECT content FROM article "+
        "WHERE type = 1 "+
          "AND humour = \"intercalaris\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
int2 = ("SELECT content FROM article "+
        "WHERE type = 2 "+
          "AND humour = \"intercalaris\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
int3 = ("SELECT content FROM article "+
        "WHERE type = 3 "+
          "AND humour = \"intercalaris\" "+
          "AND aux_type = \"n\" "+
          "AND ranking BETWEEN 1 AND 29 "+
        "ORDER BY ranking DESC;")
inter = [int1, int2, int3]
all_selects["Intercalaris"] = inter

# Converts a snippet of HPML into (encapsulated) LaTeX code.
def to_latex(hpml):
  compiler = HPML_compiler(None, hpml)
  latex = compiler.digest()
  mini_encapsulator = Mini_encapsulator(latex)
  result = mini_encapsulator.digest()
  return result

### A helper class.
class Month:
  def __init__(self, name, intro, articles):
    self.songs = articles["songs"]
    self.sonnets = articles["sonnets"]
    self.proverbs = articles["proverbs"]

  # Construct a string from
    lengths = [len(self.songs), len(self.sonnets), len(self.proverbs)]
    n = min(lengths)
    self.d = "\\chapter{"+name+"}\n\n"+intro+"\n\n"
    for i in range(n):
      self.d = self.d+"\\bigskip\n\\bigskip\n\\section{}\n\n"
      self.d = self.d+"\\subsection{}\n\n"
      self.d = self.d+to_latex(self.songs[i])+"\n\n"
      self.d = self.d+"\\subsection{}\n\n"
      self.d = self.d+to_latex(self.sonnets[i])+"\n\n"
      self.d = self.d+"\\bigskip\n\\subsection{}\n\n"
      self.d = self.d+to_latex(self.proverbs[i])+"\n\n"

  def digest(self):
    return self.d

### The class in question.
class Month_builder:
  def __init__(self):
    conn = sqlite3.connect("almanack.db")
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
    result = Month(name, intro, articles).digest()
    return result

  # Wrap all months into one string.
  def digest(self):
    result = (self.primilis+self.sectilis+self.tertilis+self.quartilis+
              self.quintilis+self.sextilis+self.september+self.october+
              self.november+self.december+self.unodecember+self.duodecember+
              self.intercalaris)
    return result

#mb = Month_builder()
#print(mb.digest())
