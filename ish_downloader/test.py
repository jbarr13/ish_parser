import sys
from StationLookup import lookupUSAFWBAN, lookupICAO
from RetrieveISH import getISH


if __name__ == '__main__':
    import sys
    import traceback
    
    try:
        records = []
        
        if len(sys.argv) == 4:
            usaf = '{0:06d}'.format(int(sys.argv[1]))
            wban = '{0:05d}'.format(int(sys.argv[2]))
            year = int(sys.argv[3])
            icao = lookupICAO(usaf, wban)
        elif len(sys.argv) == 3:
            icao = sys.argv[1]
            year = int(sys.argv[2])
            usaf, wban = lookupUSAFWBAN(icao, year)
            
        print getISH(usaf, wban, year)
        
    except Exception as e:
        traceback.print_exc()