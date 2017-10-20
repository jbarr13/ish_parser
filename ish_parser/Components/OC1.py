from ..Speed import Speed
from .BaseComponent import BaseComponent

class OC1(BaseComponent):
  ''' 
  Atmospheric pressure observation
  handler for MA1 data type 
  '''
  SPEED_SCALE = 10.0
 
  def __str__(self):
    return str(self.wind_gust_observation)

  def __repr__(self):
    return self.wind_gust_observation
    
  def __getitem__(self, val):
    return self.wind_gust_observation[val]

  def loads(self, string):
    self.wind_gust_observation = {'wind_gust_speed_rate': Speed(int(string[0:4])/self.SPEED_SCALE,
                                                                                                       Speed.METERSPERSECOND,
                                                                                                       string[4])}
