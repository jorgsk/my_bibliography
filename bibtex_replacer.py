"""
Sad script to abbreviate journal names.
"""
import re
from copy import deepcopy

# Make a simple dictionary to replace strings
repdict_nar = {
    '{Journal\sof\sMolecular\sBiology}': '{J Mol Biol}',
    '{Molecular\sCell}': '{Mol Cell}',
    'Biochimica\set\sBiophysica\sActa': 'Biochim Biophys Acta',
    'Biophysical\sJournal': 'Biophys J',
    'Proceedings\sof\sthe\sNational\sAcademy\sof\sSciences\sof\sthe\sUnited\s+States\sof\sAmerica': 'Proc Nat Acad Sci USA',
    'Proceedings\sof\sthe\sNational\sAcademy\sof\sSciences': 'Proc Nat Acad Sci USA',
    'Trends\sin\sMicrobiology': 'Trends in Microbiol',
    'Biophysical\sJournal': 'Biophys J',
    'Annual\sReview\sof\sBiophysics\sand\sBiomolecular\sStructure': 'Annu Rev Biophys Biomol Struct',
    'European\sJournal\sof\sBiochemistry': 'Eur J Biochem',
    'Methods\sin\sEnzymology': 'Meth Enzymol',
    'Biophysical\sJournal': 'Biophys J',
    'Nucleic\sAcids\sResearch': 'Nucleic Acids Res',
    'The\sEMBO\sJournal': 'EMBO J',
    'The\s{EMBO}\sJournal': 'EMBO J',
    'Volume': '',
    'DNA-Scrunching': 'DNA-scrunching',
    'Nature\sReviews\sMolecular\sCell\sBiology': 'Nat Rev Mol Cell Biol',
    'Journal\sof\sBiological\sChemistry': 'J Biol Chem'
}

repdict_biochem = {
    '{Journal\sof\sMolecular\sBiology}': '{J. Mol. Biol.}',
    '{Molecular\sCell}': '{Mol. Cell}',
    'Biochimica\set\sBiophysica\sActa': 'Biochim. Biophys. Acta',
    'Biophysical\sJournal': 'Biophys. J.',
    'Proceedings\sof\sthe\sNational\sAcademy\sof\sSciences\sof\sthe\sUnited\s+States\sof\sAmerica': 'Proc. Natl. Acad. Sci. U.S.A.',
    'Proceedings\sof\sthe\sNational\sAcademy\sof\sSciences': 'Proc. Natl. Acad.  Sci. U.S.A.',
    'Trends\sin\sMicrobiology': 'Trends in Microbiol.',
    'Biophysical\sJournal': 'Biophys. J.',
    'Annual\sReview\sof\sBiophysics\sand\sBiomolecular\sStructure': 'Annu. Rev.  Biophys. Biomol. Struct.',
    'European\sJournal\sof\sBiochemistry': 'Eur. J. Biochem.',
    'Methods\sin\sEnzymology': 'Meth. Enzymol.',
    'Biophysical\sJournal': 'Biophys. J.',
    'Nucleic\sAcids\sResearch': 'Nucleic Acids Res.',
    'The\sEMBO\sJournal': 'EMBO J.',
    'The\s{EMBO}\sJournal': 'EMBO J.',
    'Volume': '',
    'DNA-Scrunching': 'DNA-scrunching',
    'Nature\sReviews\sMolecular\sCell\sBiology': 'Nat. Rev. Mol. Cell. Biol.',
    'Journal\sof\sBiological\sChemistry': 'J. Biol. Chem.'
}

# loop through the input file, line by line, and replace the journal strings

# now you have two abbreviation styles: with and without dots.
journal_map = {'jorgsk_abr_nodot.bib': repdict_nar,
               'jorgsk_abr_dot.bib': repdict_biochem}

#s = "start foo end"
#s = re.sub("foo", "replaced", s)

# Generate a .bbl file by r

# read the bibtex output file (should have been sorted)
# PS: run this script from the directory where it lies
infile_handle = open('jorgsk.bib', 'rb')

file_as_string = infile_handle.read()  # read file as single string
infile_handle.close()

for outfile, repdict in journal_map.items():

    # apply the regular expressions
    # make a copy of the original bib
    bib = deepcopy(file_as_string)
    for original, abr in repdict.items():
        new = re.sub(original, abr, bib)
        bib = new

    # after substitution, write back to file, and close file
    out_handle = open(outfile, 'wb')
    out_handle.write(bib)
    out_handle.close()
