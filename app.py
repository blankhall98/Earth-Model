#import LIBRARIES
#import numpy as np
#import pandas as pd
#import matplotlib.pyplot as plt
#import seaborn as sns
#from scipy.optimize import curve_fit

#import MODULES
from scripts.inputs import Inputs
from scripts.world import World, Region
from scripts.sdg import SDG
from scripts.pb import PB
from scripts.e3 import E3

#input class has the following columns:
#1. planetary_boundaries
#2. sustainable_goals
#3. world_regions
#4. data_parameters

#main section
def main():
    
    e3 = E3(World,SDG,PB,Inputs)

#run app
if __name__ == '__main__':
    main()
