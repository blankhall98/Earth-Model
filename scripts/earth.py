class Earth:

    def __init__(self):
        self.world_regions = ['United States','Other Rich Countries',
        'China','Emerging Economies','Indian Subcontinent','Africa South of Sahara','Rest of World']

    def run(self):
        #greet client
        self.greeting()

    #greetings to the earth module
    def greeting(self):
        print('\n'+'-----'+'Welcome to the Earth Module.'+'-----'+'\n')

    def earth_module_actions(self):
        display = {}
        return display

class Region:

    def __init__(self,region_name):
        self.region_name = region_name