"""
Camilla D. K. Harris
October 2018

This module contains functions for printing numbers and tables in TeX format.

Use it like:

    import texformatter as texf
    x = 3.14

    # decimal
    texstr = texf.decimal("{:4.2f}".format(x)) -> $3.14$
    # scientific notation
    texstr = texf.scinot("{:1E}".format(x)) -> $3\times10^{0}$

    # Then write the number to a file:
    with open("x.tex","w") as text_file:
        print(texstr, file=text_file)

Then reference the number in your tex source with \input{} like:
    The value of $\pi$ is \input{x.tex}.
"""

MATH_DELIM = "$"
SCINOT = ["\times10^{","}"]
TABENV = [r"\begin{tabular}{","}","\end{tabular}"]
NEWLINE = "\n"
HLINE = "\hline"
ROW_DELIM = r"\\"
COL_DELIM = "&"

def decimal(num:str):
    """Returns a decimal string formatted for TeX math mode.
    """
    return MATH_DELIM+num+MATH_DELIM

def scinot(num:str):
    """Returns a scientific notation string formatted for TeX math mode.
    """
    if "e" not in num.lower():
        num = "{:E}".format(num)
    str_part = num.lower().split("e")
    return MATH_DELIM+str_part[0]+SCINOT[0]+str_part[1]+SCINOT[1]+MATH_DELIM
    
def dict2tab(tab:dict,align_str="",columns=True,insert_hline=[]):
    """Returns a table string formatted for TeX.
    Parameters
    ----------
    tab:          A dict with keys for headers, and the values are lists of strings.
    align_str:    The string that describes the alignment of the columns. Default
                  behavior depends on the columns parameter.
    columns:      If True, the keys are column headers and the values are columns.
                  If False, the keys are row headers and the values are rows.
    insert_hline: A list of ints specifying which rows should be horizontal lines.
    """
    if columns:
        ncols = len(tab.keys())
        nrows = max([len(v) for v in tab.values()]) + 1
    else:
        nrows = len(tab.keys())
        ncols = max([len(v) for v in tab.values()]) + 1
    if align_str == "":
        if columns:
            align_str = "c"*ncols
        else:
            align_str = "c"+"l"*(ncols-1)
    keys = [k for k in tab.keys()]
    tab_str = TABENV[0]+align_str+TABENV[1]+NEWLINE
    for r in range(nrows+len(insert_hline)):
        if r in insert_hline:
            line = HLINE
        else:
            if not columns:
                line = keys[r]
                for c in range(ncols-1):
                    line = line + COL_DELIM + tab[keys[r]][c]
                line = line + ROW_DELIM
            else:
                line = tab[keys[0]][r]
                for c in range(1,ncols):
                    line = line + COL_DELIM + tab[keys[c]][r]
                line = line + ROW_DELIM
            line = line + NEWLINE
        tab_str = tab_str + line
    tab_str = tab_str + TABENV[2]+NEWLINE
    return tab_str
