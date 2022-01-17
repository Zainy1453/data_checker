import math
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

class Dashboard():
    """ Dashboard class for quick insights form the data
    Attributes:
          df (pandas dataframe) representing the variable holding the table in question      
    """
    def __init__(self,df):

        self.data = df
   
        
    def show_insights(self):

        return self.data.describe()
    
        
            
        

          
