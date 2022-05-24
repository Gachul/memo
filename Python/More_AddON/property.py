class Test:
    _welcome = "All Price is Same!"
    _price = 10000
    def __init__(self, name):
        self._name = name
        print(Test._welcome)
        
    @property
    def name(self):
        return f'{self._name} : {Test._price}'
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    


mine = Test('Apple')

print(mine.name)

mine.name = "Blue Berry"

print(mine.name)