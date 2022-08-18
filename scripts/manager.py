class ModuleManager:

    def __init__(self,earth_module,sdg_module,pb_module,e3_module):

        #save modules
        self.earth = earth_module
        self.sdg = sdg_module
        self.pb = pb_module
        self.e3 = e3_module

        #greetings
        self.greetings()

        #access to menu
        self.menu()

        #goodbye
        self.goodbye()

    # Greet the client
    def greetings(self):
        print('\n'+'----------'+'Welcome to Earth Model.'+'----------')

    # Say goodbye to client
    def goodbye(self):
        print('\n'+'----------'+'\n'+'Thanks for using Earth Model.'+'\n'+'To access the model again, run the application file.')

    # MENU
    def menu(self):
        #activation trigger
        self.active = True
        
        #while loop - stay inside menu
        while self.active:
            
            # display available modules
            print('\n'+'Please select a Module (select number)'+'\n')
            display = self.module_options()
            for i in range(len(display)):
                print(f'{i+1} - {display[list(display.keys())[i]][0]}')
            
            #client selects module
            selected_module = input('\n' + 'Select Module: ')

            #handle client selection
            possible_answers = [str(x) for x in range(1,len(display)+1)]
            if selected_module in possible_answers:
                #run module function
                display[list(display.keys())[int(selected_module)-1]][1]()
            else:
                print('Answer not valid. Stay and select again.')

            # ask client to continue or quit
            stay = input('\n'+'Continue using the model? (yes/no): ')
            if stay == 'yes':
                pass
            elif stay == 'no':
                self.active = False
            else:
                print('Answer not valid. Model will QUIT.')
                self.active = False

    # Display module options - complementary for MENU
    def module_options(self):
        display = {
            'earth': ['Earth Module',self.earth.run],
            'sdg': ['Sustainable Development Goals Module',self.sdg.run],
            'pb': ['Planetary Boundaries Module',self.pb.run],
            'e3': ['Earth3 Simulation Module',self.e3.run]
        }
        return display