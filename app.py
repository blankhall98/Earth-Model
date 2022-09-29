#import LIBRARIES
#import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import seaborn as sns
#from scipy.optimize import curve_fit

#import MODULES
from scripts.inputs import Inputs
from scripts.world import World
from scripts.sdg import SDG
from scripts.pb import PB
from scripts.e3 import E3


#main section
def main():
    
    print('EarthModel -----'+'\n')

    e3 = E3(World,SDG,PB,Inputs)

    #   E3 ACTIONS -----
    e3.graph_population()

    e3.graph_regional_population('India')


#run app
if __name__ == '__main__':
    main()
