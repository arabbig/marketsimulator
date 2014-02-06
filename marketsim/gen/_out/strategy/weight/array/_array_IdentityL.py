from marketsim import registry
from marketsim import float
from marketsim import listOf
from marketsim import IFunction
@registry.expose(["Strategy", "array_IdentityL"])
class array_IdentityL_(IFunction[listOf(float), listOf(float)]):
    """ 
    """ 
    def __init__(self):
        from marketsim import rtti
        
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        
    }
    def __repr__(self):
        return "array_IdentityL" % self.__dict__
    
    def __call__(self, array = None):
        from marketsim.gen._out.strategy.weight._IdentityL import IdentityL
        array = array if array is not None else []
        
        return IdentityL(array)
    
array_IdentityL = array_IdentityL_
