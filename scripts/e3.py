class E3:

    def __init__(self,world,sdg,pb,inputs):

        #load instances
        self.inputs = inputs()
        self.world = world(self.inputs.world_regions,self.inputs.data_parameters)
        self.sdg = sdg(self.inputs.sustainable_goals)
        self.pb = pb(self.inputs.planetary_boundaries)

        
        
