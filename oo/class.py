class Foo(object):
    @staticmethod
    def show():
        print('Foo static')

    @staticmethod
    def show_1(s):
        print('Foo static [%s]' % s)

    tag = 'tx'
    @classmethod
    def get_no_of_instance(cls):
        print( '---->Foo classmthod' )
        cls.show()#visit static method.
        print( cls.tag )#visit static member
        print( '<----Foo classmthod' )
        
    def __init__(self):
        self.__private_var = 0
        self.name = 'dizuo'
		
    def say(self):
        print( 'var:%d,name:%s' % (self.__private_var, self.name) )

    def __impl(self):
        print( 'impl' )
    
def main():
    Foo.show()
    Foo.show_1('main')
    Foo.get_no_of_instance()

    foo = Foo()
    foo.say()
    print( 'name = %s' % foo.name )

    print( foo.__dict__ )
    foo.__private_var = 121 #insert new public member.
    foo.__xx_var = 12232
    foo.say()

    print( foo.__dict__ )
    
    #foo.__impl()# 'Foo' object has no attribute '__impl'    
    
if __name__ == "__main__":
    main()
