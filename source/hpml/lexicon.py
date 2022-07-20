lexicon = dict()
lexicon["#LORD"] = "{\\hoskeroe LORD}"
lexicon["#GOD"] = "{\\hoskeroe GOD}"
lexicon["##TAB"] = "{\\vin}"
lexicon["#AHAT"] = "\\^{a}"
lexicon["#AGRAVE"] = "\\`{a}"
lexicon["#EACUTE"] = "\\'{e}"
lexicon["#EGRAVE"] = "\\`{e}"
lexicon["#EDDOT"] = "\\\"{e}"
lexicon["#EHAT"] = "\\^{e}"
lexicon["#CEDILLA"] = "\\c{c}"
lexicon["#ODIAERESIS"] = "\\\"{o}"
lexicon["#KNOTS"] = "\\textsc{kts}"
lexicon["#ETC"] = "\\&c."
lexicon["#SHIP{"] = "{\\hoskeroe "
lexicon["#POUNDS"] = "{\\pounds}"
lexicon["#SHILLINGS"] = "s"
lexicon["#PENCE"] = "d"
lexicon["#ENDOFSECTION"] = "\\aldine"
lexicon["#PERCENT"] = "\\%"
lexicon["#NUMERO"] = "\\textnumero"
lexicon["#ITAL{"] = "\\textit{"
lexicon["|"] = "$\mid$"

fractions = dict()
half = dict()
half["words"] = "half"
half["latex"] = "\\sfrac{$1$}{$2$}"
fractions["#HALF"] = half
third = dict()
third["words"] = "third"
third["latex"] = "\\sfrac{$1$}{$3$}"
fractions["#THIRD"] = third
quarter = dict()
quarter["words"] = "quarter"
quarter["latex"] = "\\sfrac{$1$}{$4$}"
fractions["#QUARTER"] = quarter