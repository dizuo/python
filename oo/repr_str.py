
class Value:
    '''Base class'''
    
    def __init__(self):
        pass

    def __repr__(self):
        return "Value::repr"

    def __str__(self):
        return "Value::str"

tt = Value()
print( tt )
res = '%s' % tt
print(res)

res1 = '%r' % tt
print(res1)

# Result.
#Value::str
#>>> tt
#Value::repr
