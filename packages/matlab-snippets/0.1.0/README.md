## MATLAB Snippets
A small package for [espanso](https://espanso.org/) with triggers for headers and code snippets I constantly use in [MATLAB](https://www.mathworks.com/products/matlab.html?s_tid=hp_products_matlab). Feel free to use and modify any of these as you see fit.

### Global Variables:
    myName
        Global variable for your name. Make sure to change to your name or username. Can be replaced in the headers with any pre-existing variables that have your name.

### Triggers: 
    :matHead
        Generic header form with spaces to enter the file name, a summary and any collaborators.
    :matFunc
        Generic Function header with blanks to enter the function name, a summary and any collaborators.
    :matPlot
        Code snippet with basic commands used when making a plot. Saves figure to a variable that can be used to reopen, modify and print a plot.
    :matPrnt
        Code snippet for printing out MATLAB figures (.fig). Uses the name assigned to a variable as seen in :matPlot
    :matData
        Code snippet for loading multiple files from a folder into a structure.

Last Updated: 08/19/2024