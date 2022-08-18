class ModuleManager:

    def __init__(self,earth_module,sdg_module,pb_module):

        #save modules
        self.earth = earth_module
        self.sdg = sdg_module
        self.pb = pb_module

        #greetings
        self.greetings()

    # Greet the client
    def greetings(self):
        print('Welcome to Earth Model.')