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

def decimal(num):
    return MATH_DELIM+num+MATH_DELIM

def scinot(num):
    if "e" not in num.lower():
        num = "{:E}".format(num)
    str_part = num.lower().split("e")
    return MATH_DELIM+str_part[0]+SCINOT[0]+str_part[1]+SCINOT[1]+MATH_DELIM
    
