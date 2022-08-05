import calendar
import os
from datetime import datetime


def translate_month(month_data):
    """
    translates a number into an abbreviated month string
    eg Jun, Jul, Aug
    """
    return calendar.month_abbr[int(month_data)]


def get_oldest(datetimes):
    """
    returns the year as a string
    the month number is called into the translate_month method (above)
    and that method will translate said number into the short month name
    eg Jun, July, Aug
    """
    oldest = min(datetimes)
    month = translate_month(datetime.fromtimestamp(oldest).strftime("%m"))
    year = datetime.fromtimestamp(oldest).strftime("%Y")
    return month, year


def getfiles(dirname):
    """
    returns a list of all files in dir
    searches recursively
    replaces any spaces with non-blanks
    uses the extend function to avoid returning a list of lists
    """
    allFiles = list()
    for entry in os.listdir(dirname):
        if "." in entry:
            if " " in entry:
                entry = entry.replace(" ", "")

            allFiles.append(entry.replace(" ", ""))
        else:
            allFiles.extend(getfiles(dirname + "/" + entry))
    return allFiles


def getListOfFiles(dirName):
    """
    returns a list of all files in dir
    searches recursively
    replaces any spaces with non-blanks
    """
    listOfFile = os.listdir(dirName)
    allFiles = list()

    for entry in listOfFile:
        fullPath = os.path.join(dirName, entry)
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles
