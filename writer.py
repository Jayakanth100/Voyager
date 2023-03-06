import pickle

class user_data:

    def __init__(self):
        self.hi_score = 0
        self.user_settings = [0 , 1 , 0]        

    def update(self):
        pickle.dump(self, open("game_data.dat", "wb"))
        
def extract_user_data(obj):

    temp = user_data()
    
    try:

        f = open("game_data.dat" , 'rb')
        f.close()

        temp = pickle.load(open("game_data.dat", "rb")) 
        
    except (FileNotFoundError , pickle.UnpicklingError):    
        pass

    obj.hi_score = temp.hi_score
    obj.user_settings = temp.user_settings
    



    
            