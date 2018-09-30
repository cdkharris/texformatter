Camilla D. K. Harris

October 2018

# texformatter

This module contains functions for printing numbers and tables in TeX format.

## Examples

Use it like this:

    import texformatter as texf
    x = 3.14

    # decimal
    texstr = texf.decimal("{:4.2f}".format(x)) # -> $3.14$
    # scientific notation
    texstr = texf.scinot("{:1.0E}".format(x)) # -> $3\times10^{+00}$

    # Then write the number to a file:
    with open("x.tex","w") as text_file:
        print(texstr, file=text_file)

Then reference the number in your tex source with \input{} like:

    The value of $\pi$ is \input{x.tex}.

Print a table:

    import texformatter as texf
    a = {"b":["1","2","3"],"c":["1","2","3"]}
    print(texf.dict2tab(a,columns=False))

Output will be:

    \begin{tabular}{clll}
    b&1&2&3\\
    c&1&2&3\\
    \end{tabular}