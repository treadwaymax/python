#! python3
# renameDates.py - renames filenames with American MM-DD-YY date format to European dates format DD-MM-YY.
import shutil, os, re

# create a regex that matches files with the American date format.
datePattern = re.compile(r'''^(.*?) # all text before the date
    ((0|1)?\d)-     # one or two digits for the month
    ([0-3]?\d)-     # one or two digits for the day
    ((19|20)\d\d)   # four digits for the year
    (.*?)$          # all the text after the date
    ''', re.VERBOSE)

# loop over the files in the working directory
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # skip files without a date
    if mo == None:
        continue
    # get the different parts of a filename
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(3)
    yearPart = mo.group(4)
    afterPart = mo.group(5)
    # form the European-style filename
    euroFilename = beforePart + monthPart + '-' + dayPart + '-' + yearPart + afterPart
    # get the full, absolute file path
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    # rename the files
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    #shutil.move(amerFilename, euroFilename) # uncomment after testing