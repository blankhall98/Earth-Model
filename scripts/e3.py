import matplotlib.pyplot as plt

class E3:

    def __init__(self,world,sdg,pb,inputs):

        #load instances
        self.inputs = inputs()
        self.world = world(self.inputs.world_regions,self.inputs.data_parameters)
        self.sdg = sdg(self.inputs.sustainable_goals)
        self.pb = pb(self.inputs.planetary_boundaries)

    #   GRAPHICS SECTION -----

    #graphs the total population by region. dotted line means prediction.
    def graph_population(self):

        plt.figure(figsize=(12,8))

        plt.suptitle('Total Population by Region')
        plt.text(0,0,'The dotted lines represent UN predictions.')
        plt.xlabel('Year')
        plt.ylabel('Population in millions')

        for region in self.world.world_regions.values():

            region_name = region['region']
            regional_population = region['instance'].population
            color = region['color']
            last_year_recorded = [self.inputs.historical_years[-1]]

            plt.plot(self.inputs.historical_years,regional_population[self.inputs.historical_years].values[0],color,label=f'{region_name}')
            plt.plot(last_year_recorded+self.inputs.prediction_years,regional_population[last_year_recorded+self.inputs.prediction_years].values[0],color,linestyle='dashed')
    
        plt.legend()
        plt.show()

    #graphs the total population of specific region given its code
    def graph_regional_population(self,region_code):

        region = self.world.world_regions[region_code]['instance']
        color = self.world.world_regions[region_code]['color']
        last_year_recorded = [self.inputs.historical_years[-1]]

        plt.figure(figsize=(12,8))

        plt.suptitle(f'Total Population {region.name}')
        plt.xlabel('Year')
        plt.ylabel('Population in millions')

        plt.plot(self.inputs.historical_years,region.population[self.inputs.historical_years].values[0],color,label='Historical Values')
        plt.plot(last_year_recorded+self.inputs.prediction_years,region.population[last_year_recorded+self.inputs.prediction_years].values[0],color,linestyle='dashed',label='UN Predictions')

        plt.legend()
        plt.show()
