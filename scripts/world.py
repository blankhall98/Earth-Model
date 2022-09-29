import pandas as pd

class World:

    def __init__(self,world_regions,data_parameters):
        #load parameters
        self.world_regions = world_regions
        self.data_parameters = data_parameters

        self.total_timelapse = data_parameters['historical_years'] + data_parameters['prediction_years']

        #read raw data
        self.read_population()
        self.read_GDP()
        self.read_SDG()

        #create regions
        self.create_regions()

        #--debugging--
        print('World Class Correctly Initialized.')

    #   REGION CLASS ----- INNER CLASS
    class Region:

        def __init__(self,regional_statistics):
            self.regional_statistics = regional_statistics

        def __repr__(self):
            return self.regional_statistics['region']

    #   READ RAW DATA SECTION   -----

    #reads raw population database
    def read_population(self):
        self.population = pd.read_csv(self.data_parameters['route']+self.data_parameters['population'])

    #reads raw gdp database
    def read_GDP(self):
        self.GDP = pd.read_csv(self.data_parameters['route']+self.data_parameters['GDP'])

    #reads raw sdg database
    def read_SDG(self):
        self.SDG = pd.read_csv(self.data_parameters['route']+self.data_parameters['SDG'])

    #   REGION CREATION SECTION -----

    #creates sub-base on the population database that only cointains the target region information
    def region_population(self,region_name):
        pop = self.population[self.population['Region'] == region_name].reset_index(drop=True)
        pop = pop[self.total_timelapse]
        return pop

    #creates sub-base on the gdp database that only cointains the target region information
    def region_GDP(self,region_name):
        gdp = self.GDP[self.GDP['Region'] == region_name].reset_index(drop=True)
        gdp = gdp[self.total_timelapse]
        return gdp

    #creates sub-base on the sdg database that only cointains the target region information
    def region_SDG(self,region_name):
        sdg = self.SDG[self.SDG['Region'] == region_name].reset_index(drop=True)
        sdg = sdg[self.total_timelapse+['SDG']]
        sdg['SDG'] = sdg['SDG'].astype('int')
        sdg = sdg.set_index('SDG')
        return sdg

    #creates a region class instance for every region specified in the world_regions input
    def create_regions(self):
        
        for region in self.world_regions.values():
            region_name = region['region']
            
            #subset of regional information
            region_population = self.region_population(region_name)
            region_GDP = self.region_GDP(region_name)
            region_SDG = self.region_SDG(region_name)
            
            #add values to region dictionary
            region['population'] = region_population
            region['GDP'] = region_GDP
            region['SDG'] = region_SDG
            
            #region initialization
            region['instance'] = self.Region(region)