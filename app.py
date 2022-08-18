#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#import scripts
from scripts.sdg import SDG
from scripts.pb import PB
from scripts.earth import Earth
from scripts.manager import ModuleManager

#main section
def main():
    print('app working')

    #initialize modules
    _earth = Earth()
    _pb = PB()
    _sdg = SDG()

    #initialize module manager
    manager = ModuleManager(_earth,_pb,_sdg)

#run app
if __name__ == '__main__':
    main()
