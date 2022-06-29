class Wrapper:
    def __init__(self,object):
        self.wrapped = object
    
    def __getattr__(self,attrname):
        "__getattr__은 속성참조 X.a"
        print("Trace: " + attrname)
        return getattr(self.wrapped,attrname)

    