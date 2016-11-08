# utils

Dump site for useful code snippets (ctrl+c ctrl+v > writing and rewriting over and over again).


# Reference

## print_table

#### *Description*

Prints a table from a given array of arrays of strings. Programmer can customize the look of the table.

#### *Dependencies*

Python 3 or greater (python2 gives a `SyntaxError: Non-ASCII character` in line 6.

Tested on Python 3.5.2 running on 4.8.4-1-Arch Linux.

#### *Sample*
~~~~
[alexander@mycoolpc utils]$ ./print_table.py
╔═══════════╦═══════════╦═══════════╦═══════════╗
║ o         ║ o         ║ x         ║           ║
╠═══════════╬═══════════╬═══════════╬═══════════╣
║           ║ x         ║           ║           ║
╠═══════════╬═══════════╬═══════════╬═══════════╣
║ 0         ║ x         ║           ║ alexander ║
╚═══════════╩═══════════╩═══════════╩═══════════╝
~~~~
#### *Todo*
* nothing
