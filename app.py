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
from scripts.e3 import E3

#main section
def main():
    print('... BLANKHALL DEVELOPMENT...')

    #initialize modules
    _earth = Earth()
    _pb = PB()
    _sdg = SDG()
    _e3 = E3()

    #initialize module manager
    manager = ModuleManager(_earth,_sdg,_pb,_e3)

#run app
if __name__ == '__main__':
    main()
