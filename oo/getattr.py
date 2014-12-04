class Dynamo:
    tags = {
        'name':'renyafei',
        'addr':'beijing'
        }

    def __init__(self):
        self.entries = []
        l = []
        l.append('name')
        l.append('ryf')
        
    def __getattr__(self, key):
        print('__getattr__')
        if key == 'color':
            return 'dizuo'
        else:
            raise AttributeError

    def __setattr__(self, name, value):
        print ('__setattr__')
        print(name, value)
        for key,entry in self.tags.items():
            if key == name:
                self[key] = value
        self.__dict__[name] = value

    def __getitem__(self, key):
        return __getattr__(self, key)
    
dyn = Dynamo()

'''
>>> dyn = Dynamo()
>>> dyn
<__main__.Dynamo object at 0x01F73510>
>>> dyn.color
__getattr__
'dizuo'
>>> dyn.color = 'name'
>>> dyn.color
'name'
'''

def test():
    print('test')
    
