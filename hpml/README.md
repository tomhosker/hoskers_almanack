# HPML = Hosker's Poetical Markup Language

The code in this directory creates a markup language, HPML, to be used for formatting poetry. HPML is to be compiled into **LaTeX**, and the **verse** package thereof, which can then be compiled into a PDF.

## Assumptions

* HPML is to be used to write **English** poetry only.
* The English language uses only those familiar printable ASCII characters, and also the pounds sterling symbol.
* English poetry uses the same characters as the English language, except that foreign words, and thus foreign characters, are occasionally used.
* The user may wish to print foreign words, the names of books/films/etc, the names of people and the names of places, respectively, in special fonts.
* The user may wish to add headings to certain verses.
* The user may wish to affix observations to lines.
* The user may wish to add comments to the code.

## Language Structure

* Commands are called using the `#` character.
* "Structural" commands are denoted using the `##` string.
* Comments are created using the `###` string. No in-line comments, and no multi-line comments.
* Braces are used in the same fashion as in LaTeX.

## Lexicon

### LaTeX Equivalents

HPML on the left, LaTeX on the right.

`\n` = `\\` and `\\*`
`\n\n` = `\\!`
`##TAB` = `\vin`

#### Foreign Characters

`#{EACUTE}` = `\'e`
`#{EHAT}` = `\^e`

### Semantic Markups

`#PLACE{Somewhere}` : with default settings, this would be compiled into `{\sc Somewhere}`.
`#PERSON{Someone}` : with default settings, this would be compiled into `\textit{Someone}`.
`#PUBLICATION{Book}` : with default settings, this would be compiled into `{\hge Book}`.
`#FOREIGN{Parlez-vous}` : with default settings, this would be compiled into `{\hge Parlez-vous}`.
`#HALF`, `#THIRD`, `#QUARTER` : with default settings, these would be compiled into `\sfrac{1}{2}`, `\sfrac{1}{3}`, `\sfrac{1}{4}`.
`--` : with default settings, this would be compiled into `--`.
