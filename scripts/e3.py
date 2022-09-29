import matplotlib.pyplot as plt

class E3:

    def __init__(self,world,sdg,pb,inputs):

        #load instances
        self.inputs = inputs()
        self.world = world(self.inputs.world_regions,self.inputs.data_parameters)
        self.sdg = sdg(self.inputs.sustainable_goals)
        self.pb = pb(self.inputs.planetary_boundaries)

        #call sgd ~ gdp correlation process
        self.correlate()

    #   GRAPHICS SECTION -----

    # DEMOGRAPHIC AND ECONOMICAL INFORMATION
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

    #graph total gdv by region
    def graph_gdp(self):

        plt.figure(figsize=(12,8))

        plt.suptitle('Total Gross Domestic Product by Region')
        plt.text(0,0,'The dotted lines represent WorldBank predictions.')
        plt.xlabel('Year')
        plt.ylabel('Gross Domestic Product in millions')

        for region in self.world.world_regions.values():

            region_name = region['region']
            regional_gdp = region['instance'].gdp
            color = region['color']
            last_year_recorded = [self.inputs.historical_years[-1]]

            plt.plot(self.inputs.historical_years,regional_gdp[self.inputs.historical_years].values[0],color,label=f'{region_name}')
            plt.plot(last_year_recorded+self.inputs.prediction_years,regional_gdp[last_year_recorded+self.inputs.prediction_years].values[0],color,linestyle='dashed')
    
        plt.legend()
        plt.show()

    # graph regional gdp given athe region code
    def graph_regional_gdp(self,region_code):

        region = self.world.world_regions[region_code]['instance']
        color = self.world.world_regions[region_code]['color']
        last_year_recorded = [self.inputs.historical_years[-1]]

        plt.figure(figsize=(12,8))

        plt.suptitle(f'Total Gross Domestic Product {region.name}')
        plt.xlabel('Year')
        plt.ylabel('GDP in millions')

        plt.plot(self.inputs.historical_years,region.gdp[self.inputs.historical_years].values[0],color,label='Historical Values')
        plt.plot(last_year_recorded+self.inputs.prediction_years,region.gdp[last_year_recorded+self.inputs.prediction_years].values[0],color,linestyle='dashed',label='World Bank Predictions')

        plt.legend()
        plt.show()

    #graph the gross domestic product per capita per region 
    def graph_gdppc(self):

        plt.figure(figsize=(12,8))

        plt.suptitle('Total Gross Domestic Product per Capita by Region')
        plt.text(0,0,'The dotted lines represent WorldBank predictions.')
        plt.xlabel('Year')
        plt.ylabel('Gross Domestic Product per Capita in millions')

        for region in self.world.world_regions.values():

            region_name = region['region']
            regional_gdppc = region['instance'].gdppc
            color = region['color']
            last_year_recorded = [self.inputs.historical_years[-1]]

            plt.plot(self.inputs.historical_years,regional_gdppc[self.inputs.historical_years].values[0],color,label=f'{region_name}')
            plt.plot(last_year_recorded+self.inputs.prediction_years,regional_gdppc[last_year_recorded+self.inputs.prediction_years].values[0],color,linestyle='dashed')
    
        plt.legend()
        plt.show()

    # graph the gdp per capita of specific region given the region code
    def graph_regional_gdppc(self,region_code):

        region = self.world.world_regions[region_code]['instance']
        color = self.world.world_regions[region_code]['color']
        last_year_recorded = [self.inputs.historical_years[-1]]

        plt.figure(figsize=(12,8))

        plt.suptitle(f'Total Gross Domestic Product per Capita {region.name}')
        plt.xlabel('Year')
        plt.ylabel('GDP per capita in millions')

        plt.plot(self.inputs.historical_years,region.gdppc[self.inputs.historical_years].values[0],color,label='Historical Values')
        plt.plot(last_year_recorded+self.inputs.prediction_years,region.gdppc[last_year_recorded+self.inputs.prediction_years].values[0],color,linestyle='dashed',label='World Bank Predictions')

        plt.legend()
        plt.show()

    # graph - by region - the progress on specific sustainable development goal
    def graph_sdg(self,goal):

        goal_data = self.sdg.sustainable_goals[goal]

        plt.figure(figsize=(12,8))

        plt.title(goal_data['goal']+' : '+goal_data['indicator'])
        plt.ylabel(goal_data['indicator'])
        plt.xlabel('Year')

        green_yellow = goal_data['green-yellow']
        yellow_red = goal_data['yellow-red']

        plt.fill_between(self.inputs.historical_years,green_yellow,yellow_red, color = 'yellow', alpha = 0.09,label='Warning Zone')
        minimum_values = []
        maximum_values = []

        

        for region in self.world.world_regions.values():

            region_name = region['region']
            regional_sdg = region['instance'].sdg.loc[int(goal)]
            color = region['color']
            #last_year_recorded = [self.inputs.historical_years[-1]]

            plt.plot(self.inputs.historical_years,regional_sdg[self.inputs.historical_years],color,label=f'{region_name}')
            #plt.plot(last_year_recorded+self.inputs.prediction_years,regional_gdppc[last_year_recorded+self.inputs.prediction_years].values[0],color,linestyle='dashed')

            minimum_values.append(min(regional_sdg[self.inputs.historical_years]))
            maximum_values.append(max(regional_sdg[self.inputs.historical_years]))

        if goal_data['direction of progress'] == '<':
            best = min(minimum_values) 
            worst = max(maximum_values) 
        else:
            best = max(maximum_values) 
            worst = min(minimum_values) 

        plt.fill_between(self.inputs.historical_years,worst,yellow_red, color = 'red', alpha = 0.09,label='Danger Zone')
        plt.fill_between(self.inputs.historical_years,green_yellow,best, color = 'green', alpha = 0.09,label='Safe Zone')

        plt.legend()
        plt.show()

    # graph regional sdg progress given specific region
    def graph_regional_sdg(self,region_code,goal):

        goal_data = self.sdg.sustainable_goals[goal]

        plt.figure(figsize=(12,8))

        plt.title(goal_data['goal']+' : '+goal_data['indicator'])
        plt.ylabel(goal_data['indicator'])
        plt.xlabel('Year')

        green_yellow = goal_data['green-yellow']
        yellow_red = goal_data['yellow-red']

        plt.fill_between(self.inputs.historical_years,green_yellow,yellow_red, color = 'yellow', alpha = 0.09,label='Warning Zone')
        minimum_values = []
        maximum_values = []

        region = self.world.world_regions[region_code]['instance']
        color = self.world.world_regions[region_code]['color']
        plt.plot(self.inputs.historical_years,region.sdg.loc[int(goal)][self.inputs.historical_years],color,label=f'{region.name}')

        for region in self.world.world_regions.values():
            regional_sdg = region['instance'].sdg.loc[int(goal)]

            minimum_values.append(min(regional_sdg[self.inputs.historical_years]))
            maximum_values.append(max(regional_sdg[self.inputs.historical_years]))

        if goal_data['direction of progress'] == '<':
            best = min(minimum_values)
            worst = max(maximum_values)
        else:
            best = max(maximum_values)
            worst = min(minimum_values)

        plt.fill_between(self.inputs.historical_years,worst,yellow_red, color = 'red', alpha = 0.09,label='Danger Zone')
        plt.fill_between(self.inputs.historical_years,green_yellow,best, color = 'green', alpha = 0.09,label='Safe Zone')

        plt.legend()
        plt.show()

    # graph - by - region the relation between a sdg indicator and gdp
    def graph_sdgXgdp(self):
        pass

    # graph the correlation between a sdg indicator and gdp fpr specific region given region code
    def graph_regional_sdgXgdp(self):
        pass


    #   CORRELATE
    def correlate(self):
        print('.. beep boop correlating...')
    #   ADJUST
    #   PERFORMANCE