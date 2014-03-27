from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
from marketsim.gen._intrinsic.observable.minmax_eps import MaxEpsilon_Impl
from marketsim.gen._out.math._cumulative import Cumulative
from marketsim import registry
from marketsim.gen._out._observable._observablefloat import Observablefloat
@registry.expose(["Statistics", "MaxEpsilon"])
class MaxEpsilon_mathCumulativeFloat(Observablefloat,MaxEpsilon_Impl):
    """ 
      It fires updates only if *source* value becomes greater than the old value plus *epsilon*
    """ 
    def __init__(self, x = None, epsilon = None):
        from marketsim import deref_opt
        from marketsim.gen._out._observable._observablefloat import Observablefloat
        from marketsim import rtti
        from marketsim.gen._out.math._cumulative import Cumulative_IObservableFloat as _math_Cumulative_IObservableFloat
        from marketsim.gen._out._constant import constant_Float as _constant_Float
        Observablefloat.__init__(self)
        self.x = x if x is not None else deref_opt(_math_Cumulative_IObservableFloat())
        
        self.epsilon = epsilon if epsilon is not None else deref_opt(_constant_Float(0.01))
        
        rtti.check_fields(self)
        MaxEpsilon_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'x' : Cumulative,
        'epsilon' : IFunctionfloat
    }
    def __repr__(self):
        return "Max_{\\epsilon}(%(x)s)" % { name : getattr(self, name) for name in self._properties.iterkeys() }
    
def MaxEpsilon(x = None,epsilon = None): 
    from marketsim.gen._out.math._cumulative import Cumulative
    from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
    from marketsim import rtti
    if x is None or rtti.can_be_casted(x, Cumulative):
        if epsilon is None or rtti.can_be_casted(epsilon, IFunctionfloat):
            return MaxEpsilon_mathCumulativeFloat(x,epsilon)
    raise Exception('Cannot find suitable overload for MaxEpsilon('+str(x) +':'+ str(type(x))+','+str(epsilon) +':'+ str(type(epsilon))+')')
