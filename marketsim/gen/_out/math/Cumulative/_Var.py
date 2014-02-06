from marketsim.gen._intrinsic.moments.cmv import Variance_Impl
from marketsim import IObservable
from marketsim import registry
from marketsim.ops._function import Function
from marketsim import float
@registry.expose(["Statistics", "Var"])
class Var_Optional__IObservable__Float__(Function[float],Variance_Impl):
    """ 
    """ 
    def __init__(self, source = None):
        from marketsim.gen._out._const import const as _const
        from marketsim import rtti
        self.source = source if source is not None else _const()
        rtti.check_fields(self)
        Variance_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'source' : IObservable[float]
    }
    def __repr__(self):
        return "\\sigma^2_{cumul}(%(source)s)" % self.__dict__
    
Var = Var_Optional__IObservable__Float__
