#import MODULES
from scripts.inputs import Inputs
from scripts.world import World
from scripts.sdg import SDG
from scripts.pb import PB
from scripts.e3 import E3


#main section
def main():
        
    e3 = E3(World,SDG,PB,Inputs)

    #   E3 ACTIONS -----

    # DEMOGRAPHIC AND ECONOMICAL INFORMATION
    # graph population
    '''
    e3.graph_population()
    e3.graph_regional_population('ASoS')
    '''

    # graph gdp
    '''
    e3.graph_gdp()
    e3.graph_regional_gdp('ASoS')
    '''

    #graph gdp per capita
    '''
    e3.graph_gdppc()
    e3.graph_regional_gdppc('ASoS')
    '''

    # SUSTAINABLE DEVELOPMENT GOALS VS GROSS DOMESTIC PRODUCT
    # graph correlation between sdg and gdp
    '''
    e3.graph_sdgXgdp('1')
    e3.graph_sdgXgdp('1',corr=True)
    e3.graph_regional_sdgXgdp('ASoS','1')
    e3.graph_regional_sdgXgdp('ASoS','1',corr = True)
    '''
    
    #fit goals
    '''
    e3.correlate()
    '''

    # SUSTAINABLE DEVELOPMENT GOALS PROGRESS
    #graph sustainable development goal
    '''
    e3.graph_sdg('7')
    e3.graph_regional_sdg('ASoS','7')
    '''

    #predict goals
    '''
    e3.predict()
    '''
    e3.predict_goal('1')


    


#run app
if __name__ == '__main__':
    print('\n'+'----- EarthModel -----'+'\n')
    main()
