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

    # DEMOGRAPHIC AND ECONOMICAL INFORMATION
    # graph population
    e3.graph_population()
    e3.graph_regional_population('ASoS')

    # graph gdp
    e3.graph_gdp()
    e3.graph_regional_gdp('ASoS')

    #graph gdp per capita
    e3.graph_gdppc()
    e3.graph_regional_gdppc('ASoS')


#run app
if __name__ == '__main__':
    main()
