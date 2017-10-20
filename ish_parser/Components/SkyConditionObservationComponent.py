from ..CloudCoverage import CloudCoverage
from .BaseComponent import BaseComponent

class SkyConditionObservationComponent(BaseComponent):
  ''' handler for GF1 data type '''
 
  def __str__(self):
    return str(self.sky_condition_observation)

  def __repr__(self):
    return self.sky_condition_observation
    
  def __getitem__(self, val):
    return self.sky_condition_observation[val]

  def loads(self, string):
    self.sky_condition_observation = {'total_coverage': CloudCoverage(string[0:2], CloudCoverage.OKTA, string[4:5]),
                                                    'total_opaque_coverage': CloudCoverage(string[2:4], CloudCoverage.OKTA, string[4:5]),
                                                    'total_lowest_coverage': CloudCoverage(string[5:7], CloudCoverage.OKTA, string[7:8])}
