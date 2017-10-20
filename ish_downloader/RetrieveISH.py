#!/usr/bin/python
'''
Version: 2017.10.20
'''

import gzip
from ftplib import FTP
from StringIO import StringIO

def getISH(usaf, wban, year):
    # Retrieve a yearly ISH file, given the usaf, wban, and year
    # Returns content of the file as a string
    fname = '-'.join([usaf, wban, str(year) + '.gz'])
    try:
        ftp = FTP('ftp.ncdc.noaa.gov')
        ftp.login()

        ftp.cwd('pub/data/noaa/' + str(year))
        weatherCompressed = StringIO()
        ftp.retrbinary('RETR ' + fname, weatherCompressed.write)
        ftp.quit()
    except Exception as e:
        raise e

    weatherCompressed.seek(0)

    weatherDecompressed = gzip.GzipFile(fileobj=weatherCompressed, mode='rb')
    weatherRecords = []
    
    weather = weatherDecompressed.read()
    return weather

