class Inputs:

    def __init__(self):
        
        self.planetary_boundaries = {
    
                'pb1': {
                    'boundary': 'Global warming',
                    'indicator': 'Temperature rise',
                    'units': 'deg C above 1850',
                    'safe-zone': 1,
                    'high-risk': 2,
                    'risk direction': '>'
                },
                
                'pb2': {
                    'boundary': 'Ozone depletion',
                    'indicator': 'Montreal-gas emissions',
                    'units': 'Mt/y',
                    'safe-zone': 0.25,
                    'high-risk': 2,
                    'risk direction': '>'
                },
                
                'pb3': {
                    'boundary': 'Ocean acidification',
                    'indicator': 'Acidity of ocean surface water',
                    'units': 'pH',
                    'safe-zone': 8.15,
                    'high-risk': 8.1,
                    'risk direction': '<'
                },
                
                'pb4': {
                    'boundary': 'Forest degradation',
                    'indicator': 'Old-growth forest area',
                    'units': 'Mkm2',
                    'safe-zone': 25,
                    'high-risk': 17,
                    'risk direction': '<'
                },
                
                'pb5': {
                    'boundary': 'Nutrient overloading',
                    'indicator': 'Release of bioactive nitrogen',
                    'units': 'Mt/y',
                    'safe-zone': 100,
                    'high-risk': 200,
                    'risk direction': '>'
                },
                
                'pb6': {
                    'boundary': 'Freshwater overuse',
                    'indicator': 'Freshwater withdrawal',
                    'units': 'km3/y',
                    'safe-zone': 3000,
                    'high-risk': 4000,
                    'risk direction': '>'
                },
                
                'pb7': {
                    'boundary': 'Biodiversity loss',
                    'indicator': 'Unused biocapacity',
                    'units': '% of biocapacity',
                    'safe-zone': 25,
                    'high-risk': 18,
                    'risk direction': '<'
                },
                
                'pb8': {
                    'boundary': 'Air pollution',
                    'indicator': 'Urban aerosol concentration',
                    'units': 'mg 2.5M/m3',
                    'safe-zone': 10,
                    'high-risk': 35,
                    'risk direction': '>'
                },
                
                'pb9': {
                    'boundary': 'Toxics contamination',
                    'indicator': 'Release of lead',
                    'units': 'Mt/y',
                    'safe-zone': 5,
                    'high-risk': 10,
                    'risk direction': '>'
                }
            }
        
        self.sustainable_goals = {
    
                'goal1': {
                    'goal': 'No poverty',
                    'indicator': 'Fraction of population living below 1.90$ per day (%)',
                    'units': '%',
                    'green-yellow': 2,
                    'yellow-red': 13,
                    'direction of progress': '<'
                },
                
                'goal2': {
                    'goal': 'Zero hunger',
                    'indicator': 'Fraction of population undernourished (%)',
                    'units': '%',
                    'green-yellow': 7,
                    'yellow-red': 15,
                    'direction of progress': '<'
                },
                
                'goal3': {
                    'goal': 'Good health',
                    'indicator': 'Life expectancy at birth (years)',
                    'units': 'years',
                    'green-yellow': 75,
                    'yellow-red': 70,
                    'direction of progress': '>'
                },
                
                'goal4': {
                    'goal': 'Quality education',
                    'indicator': 'School life expectancy (years)',
                    'units': 'years',
                    'green-yellow': 12,
                    'yellow-red': 10,
                    'direction of progress': '>'
                },
                
                'goal5': {
                    'goal': 'Gender equality',
                    'indicator': 'Gender parity in schooling',
                    'units': '1',
                    'green-yellow': 0.95,
                    'yellow-red': 0.8,
                    'direction of progress': '>'
                },
                
                'goal6': {
                    'goal': 'Safe water',
                    'indicator': 'Fraction of population with access to safe water (%)',
                    'units': '%',
                    'green-yellow': 98,
                    'yellow-red': 80,
                    'direction of progress': '>'
                },
                
                'goal7': {
                    'goal': 'Enough energy',
                    'indicator': 'Fraction of population with access to electricity (%)',
                    'units': '%',
                    'green-yellow': 98,
                    'yellow-red': 80,
                    'direction of progress': '>'
                },
                
                'goal8': {
                    'goal': 'Decent jobs',
                    'indicator': 'Job market growth (%/y)',
                    'units': '%/y',
                    'green-yellow': 1,
                    'yellow-red': 0,
                    'direction of progress': '>'
                },
                
                'goal9': {
                    'goal': 'Industrial output',
                    'indicator': 'GDP per person in manufacturing & construction (2011 PPP US$/p-y)',
                    'units': '2011 PPP US$/p-y',
                    'green-yellow': 6000,
                    'yellow-red': 4000,
                    'direction of progress': '>'
                },
                
                'goal10': {
                    'goal': 'Reduced inequality',
                    'indicator': 'Share of national income to richest 10% (%)',
                    'units': '%',
                    'green-yellow': 40,
                    'yellow-red': 50,
                    'direction of progress': '<'
                },
                
                'goal11': {
                    'goal': 'Clean cities',
                    'indicator': 'Urban aerosol concentration (mg 2.5M/m3)',
                    'units': 'mg 2.5M/m3',
                    'green-yellow': 10,
                    'yellow-red': 35,
                    'direction of progress': '<'
                },
                
                'goal12': {
                    'goal': 'Responsible consumption',
                    'indicator': 'Ecological footprint per person (gha/p)',
                    'units': 'gha/p',
                    'green-yellow': 1.4,
                    'yellow-red': 2,
                    'direction of progress': '<'
                },
                
                'goal13': {
                    'goal': 'Climate action',
                    'indicator': 'Temperature rise (deg C above 1850)',
                    'units': 'deg C above 1850',
                    'green-yellow': 1,
                    'yellow-red': 1.5,
                    'direction of progress': '<'
                },
                
                'goal14': {
                    'goal': 'Life below water',
                    'indicator': 'Acidity of ocean surface water (pH)',
                    'units': 'pH',
                    'green-yellow': 8.15,
                    'yellow-red': 8.1,
                    'direction of progress': '>'
                },
                
                'goal15': {
                    'goal': 'Life on land',
                    'indicator': 'Old-growth-forest area (Mkm2)',
                    'units': 'Mkm2',
                    'green-yellow': 25,
                    'yellow-red': 19,
                    'direction of progress': '>'
                },
                
                'goal16': {
                    'goal': 'Good governance',
                    'indicator': 'Government spending per person (2011 PPP US$/p-y)',
                    'units': '2011 PPP US$/p-y',
                    'green-yellow': 3000,
                    'yellow-red': 2000,
                    'direction of progress': '>'
                },
                
                'goal17': {
                    'goal': 'More partnership',
                    'indicator': 'Exports as a fraction of GDP (%)',
                    'units': '%',
                    'green-yellow': 15,
                    'yellow-red': 10,
                    'direction of progress': '>'
                }
            }

        self.world_regions = {
    
            'region1': {
                'region': 'United States',
                'abreviation': 'USA',
                'members': [],
            },
            
            'region2': {
                'region': 'Other Rich Countries',
                'abreviation': 'ORC',
                'members': []
            },
            
            'region3': {
                'region': 'Emerging Economies',
                'abreviation': 'EE',
                'members': []
            },
            
            'region4': {
                'region': 'China',
                'abreviation': 'China',
                'members': []
            },
            
            'region5': {
                'region': 'Indian Subcontinent',
                'abreviation': 'India',
                'members': []
            },
            
            'region6': {
                'region': 'Africa South of Sahara',
                'abreviation': 'ASoS',
                'members': []
            },
            
            'region7': {
                'region': 'Rest of World',
                'abreviation': 'RoW',
                'members': []
            }
            
        }
    
        self.data_parameters = {
            'route': 'raw_data/',
            'population': 'Population.csv',
            'GDP': 'GDPpp.csv',
            'SDG': 'SDG1-7.csv',
            'historical_years': ['1980','1985','1990','1995','2000','2005','2010','2015'],
            'prediction_years': ['2020','2025','2030','2035','2040','2045','2050']
        }