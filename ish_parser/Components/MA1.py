from ..Pressure import Pressure
from .BaseComponent import BaseComponent

class MA1(BaseComponent):
  ''' 
  Atmospheric pressure observation
  handler for MA1 data type 
  '''
  PRESSURE_SCALE = 10.0
 
  def __str__(self):
    return str(self.atmospheric_pressure_observation)

  def __repr__(self):
    return self.atmospheric_pressure_observation
    
  def __getitem__(self, val):
    return self.atmospheric_pressure_observation[val]

  def loads(self, string):
    self.atmospheric_pressure_observation = {'altimeter_setting_rate': Pressure(int(string[0:5])/self.PRESSURE_SCALE,
                                                                                                       Pressure.HECTOPASCALS,
                                                                                                       string[5]),
                                                                  'station_pressure_rate': Pressure(int(string[6:11])/self.PRESSURE_SCALE,
                                                                                                       Pressure.HECTOPASCALS,
                                                                                                       string[11])}
