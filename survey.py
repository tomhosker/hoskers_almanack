"""
This code holds a class which identifies the gaps presently in the Almanack,
and sends a report to the screen and/or a file.
"""

# Standard imports.
import sqlite3
import sys

# Local imports.
import constants
import month_builder

# Constants.
p_pri1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_pri2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_pri3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_pri = [p_pri1, p_pri2, p_pri3]
p_sec1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_sec2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_sec3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_sec = [p_sec1, p_sec2, p_sec3]
p_ter1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_ter2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_ter3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'bile') AND (ranking = 999));")
p_ter = [p_ter1, p_ter2, p_ter3]
p_qua1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'blood') AND (aux_type = 'english folk') AND "+
          "(ranking = 999));")
p_qua2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'blood') AND (ranking = 999));")
p_qua3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'blood') AND (ranking = 999));")
p_qua = [p_qua1, p_qua2, p_qua3]
p_qui1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'blood') AND (aux_type = 'scots-irish folk') AND "+
          "(ranking = 999));")
p_qui2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(aux_type = 'shanty') AND (humour = 'blood') AND "+
          "(ranking = 999));")
p_qui3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'blood') AND (ranking = 999));")
p_qui = [p_qui1, p_qui2, p_qui3]
p_sex1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'blood') AND (aux_type = 'imperial folk') AND "+
          "(ranking = 999)) OR ((type = 1) AND (humour = 'blood') AND "+
          "(aux_type = 'hymn') AND (ranking = 999));")
p_sex2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'blood') AND (ranking = 999));")
p_sex3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'blood') AND (ranking = 999));")
p_sex = [p_sex1, p_sex2, p_sex3]
p_sep1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'phlegm') AND (ranking = 999));")
p_sep2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'phlegm') AND (ranking = 999));")
p_sep3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'phlegm') AND (ranking = 999));")
p_sep = [p_sep1, p_sep2, p_sep3]
p_oct1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'phlegm') AND (aux_type = 'october') AND "+
          "(ranking = 999));")
p_oct2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'phlegm') AND (aux_type = 'october') AND "+
          "(ranking = 999));")
p_oct3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'phlegm') AND (aux_type = 'october') AND "+
          "(ranking = 999));")
p_oct = [p_oct1, p_oct2, p_oct3]
p_nov1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'phlegm') AND (ranking = 999));")
p_nov2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'phlegm') AND (ranking = 999));")
p_nov3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'phlegm') AND (ranking = 999));")
p_nov = [p_nov1, p_nov2, p_nov3]
p_dec1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_dec2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_dec3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_dec = [p_dec1, p_dec2, p_dec3]
p_uno1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_uno2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_uno3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_uno = [p_uno1, p_uno2, p_uno3]
p_duo1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_duo2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_duo3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'black bile') AND (ranking = 999));")
p_duo = [p_duo1, p_duo2, p_duo3]
p_int1 = ("SELECT id FROM article WHERE ((type = 1) AND "+
          "(humour = 'intercalaris') AND (ranking = 999));")
p_int2 = ("SELECT id FROM article WHERE ((type = 2) AND "+
          "(humour = 'intercalaris') AND (ranking = 999));")
p_int3 = ("SELECT id FROM article WHERE ((type = 3) AND "+
          "(humour = 'intercalaris') AND (ranking = 999));")
p_int = [p_int1, p_int2, p_int3]

##############
# MAIN CLASS #
##############

# The class in question.
class Survey:
    def __init__(self):
        pri = build_survey_for_month("Primilis", month_builder.pri, p_pri,
                                     30)
        sec = build_survey_for_month("Sectilis", month_builder.sec, p_sec,
                                     29)
        ter = build_survey_for_month("Tertilis", month_builder.ter, p_ter,
                                     30)
        qua = build_survey_for_month("Quartilis", month_builder.qua, p_qua,
                                     29)
        qui = build_survey_for_month("Quintilis", month_builder.qui, p_qui,
                                     30)
        sex = build_survey_for_month("Sextilis", month_builder.sex, p_sex,
                                     29)
        sep = build_survey_for_month("September", month_builder.sep, p_sep,
                                     30)
        ott = build_survey_for_month("October", month_builder.octo, p_oct,
                                     29)
        nov = build_survey_for_month("November", month_builder.nov, p_nov,
                                     30)
        dec = build_survey_for_month("December", month_builder.dec, p_dec,
                                     29)
        uno = build_survey_for_month("Unodecember", month_builder.uno,
                                     p_uno, 30)
        duo = build_survey_for_month("Duodecember", month_builder.duo,
                                     p_duo, 29)
        inter = build_survey_for_month("Intercalaris", month_builder.inter,
                                       p_int, 29)
        self.printout = (pri+"\n\n"+sec+"\n\n"+ter+"\n\n"+qua+"\n\n"+qui+
                         "\n\n"+sex+"\n\n"+sep+"\n\n"+ott+"\n\n"+nov+"\n\n"+
                         dec+"\n\n"+uno+"\n\n"+duo+"\n\n"+inter)

    def print_to_screen(self):
        """ Ronseal. """
        print(self.printout)

    def write_to_file(self):
        """ Ronseal. """
        with open("survey.txt", "w") as survey_file:
            survey_file.write(self.printout)

####################
# HELPER FUNCTIONS #
####################

def count_select(select):
    """ A template for counting the length of the result of a SELECT
    query. """
    conn = sqlite3.connect(constants.db)
    cursor = conn.cursor()
    cursor.execute(select)
    rows = cursor.fetchall()
    result = len(rows)
    return result

def build_survey_for_month(name, selects, potential_selects, month_length):
    """ Ronseal. """
    songs = count_select(selects[0])
    sonnets = count_select(selects[1])
    proverbs = count_select(selects[2])
    potential_songs = count_select(potential_selects[0])
    potential_sonnets = count_select(potential_selects[1])
    potential_proverbs = count_select(potential_selects[2])
    result = "For the month of "+name+"...\n"
    result = (result+str(songs)+" songs out of "+str(month_length)+
              " needed, and "+str(potential_songs)+" available.\n")
    result = (result+str(sonnets)+" sonnets out of "+str(month_length)+
              " needed, and "+str(potential_sonnets)+" available.\n")
    result = (result+str(proverbs)+" proverbs out of "+str(month_length)+
              " needed, and "+str(potential_proverbs)+" available.")
    return result

###################
# RUN AND WRAP UP #
###################

def run():
    survey = Survey()
    if "--test" not in sys.argv:
        survey.print_to_screen()

if __name__ == "__main__":
    run()
