class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe(self):
        print(self.name,self.cuisine)

    def open(self):
        print('Open 19.20 - 20.00')

china = Restaurant('SuperChina','China Food')
mexico = Restaurant('Mex','Mexican Food')
belarus = Restaurant('Dranik','Belarussian Food')

china.describe(), china.open(),
mexico.describe()
belarus.describe()
