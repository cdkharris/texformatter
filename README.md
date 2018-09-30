Camilla D. K. Harris
October 2018

This module contains functions for printing numbers and tables in TeX format.

Use it like:

    import texformatter as texf
    x = 3.14

    # decimal
    texstr = texf.decimal("{:4.2f}".format(x)) # -> $3.14$
    # scientific notation
    texstr = texf.scinot("{:1E}".format(x)) # -> $3\times10^{0}$

    # Then write the number to a file:
    with open("x.tex","w") as text_file:
        print(texstr, file=text_file)

Then reference the number in your tex source with \input{} like:

    The value of $\pi$ is \input{x.tex}.
