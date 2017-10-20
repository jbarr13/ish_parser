import csv
from ftplib import FTP
from StringIO import StringIO

def lookupUSAFWBAN(icao, year):
    # Given the ICAO and a year, look up the usaf and wban for the station
    # Returns the usaf and wban for the first station matching the ICAO and
    #       the year is within the begin and end dates of records
    try:
        ftp = FTP('ftp.ncdc.noaa.gov')
        ftp.login()

        ftp.cwd('pub/data/noaa/' )
        isdhistory = StringIO()
        ftp.retrbinary('RETR ' + "isd-history.csv", isdhistory.write)
        ftp.quit()
    except Exception as e:
        raise e
    isdhistory.seek(0)
    csvreader = csv.reader(isdhistory)
    for row in csvreader:
        if row[5] == icao and int(row[-2]) <= int(str(year) + "0101") and int(row[-1]) >= int(str(year) + "1231"):
            return row[0], row[1]
    
def lookupICAO(usaf, wban):
    # Look up the ICAO given the usaf and wban
    # Returns ICAO string
    try:
        ftp = FTP('ftp.ncdc.noaa.gov')
        ftp.login()

        ftp.cwd('pub/data/noaa/' )
        isdhistory = StringIO()
        ftp.retrbinary('RETR ' + "isd-history.csv", isdhistory.write)
        ftp.quit()
    except Exception as e:
        raise e
    isdhistory.seek(0)
    csvreader = csv.reader(isdhistory)
    for row in csvreader:
        if row[0] == usaf and row[1] == wban:
            return row[5]