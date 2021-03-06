# generated with class generator.python.random$Import
from marketsim import registry
from marketsim.gen._out._ifunction._ifunctionfloat import IFunctionfloat
@registry.expose(["Random", "triangular"])
class triangular_FloatFloatFloat(IFunctionfloat):
    """ **Triangular distribution**
    
    
     Return a random floating point number *N* such that *low* <= *N* <= *high* and
           with the specified *mode* between those bounds.
           The *low* and *high* bounds default to zero and one.
           The *mode* argument defaults to the midpoint between the bounds,
           giving a symmetric distribution.
    
    Parameters are:
    
    **Low**
    
    **High**
    
    **Mode**
    """ 
    def __init__(self, Low = None, High = None, Mode = None):
        self.Low = Low if Low is not None else 0.0
        self.High = High if High is not None else 1.0
        self.Mode = Mode if Mode is not None else 0.5
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'Low' : float,
        'High' : float,
        'Mode' : float
    }
    
    
    
    
    
    
    def __repr__(self):
        return "triangular(%(Low)s, %(High)s, %(Mode)s)" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if self.__dict__.get('_bound_ex', False): return
        self.__dict__['_bound_ex'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.bind_ex(self.__dict__['_ctx_ex'])
        self.__dict__['_processing_ex'] = False
    
    def reset_ex(self, generation):
        if self.__dict__.get('_reset_generation_ex', -1) == generation: return
        self.__dict__['_reset_generation_ex'] = generation
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.reset_ex(generation)
        self.__dict__['_processing_ex'] = False
    
    def typecheck(self):
        from marketsim import rtti
        rtti.typecheck(float, self.Low)
        rtti.typecheck(float, self.High)
        rtti.typecheck(float, self.Mode)
    
    def registerIn(self, registry):
        if self.__dict__.get('_id', False): return
        self.__dict__['_id'] = True
        if self.__dict__.get('_processing_ex', False):
            raise Exception('cycle detected')
        self.__dict__['_processing_ex'] = True
        registry.insert(self)
        
        if hasattr(self, '_subscriptions'):
            for s in self._subscriptions: s.registerIn(registry)
        self.__dict__['_processing_ex'] = False
    
    def __call__(self, *args, **kwargs):
        import random
        return random.triangular(self.Low, self.High, self.Mode)
    
    def _casts_to(self, dst):
        return triangular_FloatFloatFloat._types[0]._casts_to(dst)
    
def triangular(Low = None,High = None,Mode = None): 
    from marketsim import rtti
    if Low is None or rtti.can_be_casted(Low, float):
        if High is None or rtti.can_be_casted(High, float):
            if Mode is None or rtti.can_be_casted(Mode, float):
                return triangular_FloatFloatFloat(Low,High,Mode)
    raise Exception('Cannot find suitable overload for triangular('+str(Low) +':'+ str(type(Low))+','+str(High) +':'+ str(type(High))+','+str(Mode) +':'+ str(type(Mode))+')')
