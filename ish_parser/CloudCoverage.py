from .Observation import Observation

MAP = {'00': 'None, SKC or CLR',
         '01': 'One okta - 1/10 or less but not zero',
         '02': 'Two oktas - 2/10 - 3/10, or FEW',
         '03': 'Three oktas - 4/10',
         '04': 'Four oktas - 5/10, or SCT',
         '05': 'Five oktas - 6/10',
         '06': 'Six oktas - 7/10 - 8/10',
         '07': 'Seven oktas - 9/10 or more but not 10/10, or BKN',
         '08': 'Eight oktas - 10/10, or OVC',
         '09': 'Sky obscured, or cloud amount cannot be estimated',
         '10': 'Partial obscuration',
         '11': 'Thin scattered',
         '12': 'Scattered',
         '13': 'Dark scattered',
         '14': 'Thin broken',
         '15': 'Broken',
         '16': 'Dark broken',
         '17': 'Thin overcast',
         '18': 'Overcast',
         '19': 'Dark overcast',
         '99': None}


class CloudCoverage(Observation):
    '''okta is a unit of measurement used to 
    describe the amount of cloud cover at any given location such 
    as a weather station. Sky conditions are estimated in 
    terms of how many eighths of the sky are covered in cloud, 
    ranging from 0 oktas (completely clear sky) through to 
    8 oktas (completely overcast).
    '''
    OKTA = 1
    MISSING = [99, '99']

    def __str__(self):
        if self._obs_value in self.MISSING:
            return str(None)
        else:
            return MAP[self._obs_value]

    def __repr__(self):
        if self._obs_value in self.MISSING:
            return str(None)
        else:
            return self.__str__()

    def __eq__(self, value2):
        if self._obs_value == value2:
          return True
        else:
          return False
