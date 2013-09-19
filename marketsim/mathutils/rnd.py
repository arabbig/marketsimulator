from marketsim import registry, types, ops
import random

@registry.expose(['Random', 'Beta distribution'])
class betavariate(ops.Function[float]):
    """  Beta distribution. Conditions on the parameters are |alpha| > 0 and |beta| > 0.
        Returned values range between 0 and 1.
    """    

    def __init__(self, Alpha = 1.0,Beta = 1.0):
        self.__dict__ = { 'Alpha' : Alpha,'Beta' : Beta }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Alpha' : types.positive,'Beta' : types.positive }
    
    def _casts_to(self, dst):
        return betavariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.betavariate(self.Alpha,self.Beta)
    
    def __repr__(self):
        rv = "betavariate"
        rv += "("
        for k in betavariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Exponential distribution'])
class expovariate(ops.Function[float]):
    """  Exponential distribution. |lambda| is 1.0 divided by the desired mean. 
        It should be greater zero. Returned values range from 0 to positive infinity
    """    

    def __init__(self, Lambda = 1.0):
        self.__dict__ = { 'Lambda' : Lambda }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Lambda' : types.positive }
    
    def _casts_to(self, dst):
        return expovariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.expovariate(self.Lambda)
    
    def __repr__(self):
        rv = "expovariate"
        rv += "("
        for k in expovariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Uniform integer distribution'])
class randint(ops.Function[int]):
    """ Return a random integer *N* such that *a* <= *N* <= *b*.
    """    

    def __init__(self, High = 10,Low = -10):
        self.__dict__ = { 'High' : High,'Low' : Low }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'High' : int,'Low' : int }
    
    def _casts_to(self, dst):
        return randint._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.randint(self.High,self.Low)
    
    def __repr__(self):
        rv = "randint"
        rv += "("
        for k in randint._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Uniform distribution'])
class uniform(ops.Function[float]):
    """  Return a random floating point number *N* such that 
            *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
        The end-point value *b* may or may not be included in the range depending on 
            floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
    """    

    def __init__(self, High = 10.0,Low = -10.0):
        self.__dict__ = { 'High' : High,'Low' : Low }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'High' : float,'Low' : float }
    
    def _casts_to(self, dst):
        return uniform._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.uniform(self.High,self.Low)
    
    def __repr__(self):
        rv = "uniform"
        rv += "("
        for k in uniform._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Triangular distribution'])
class triangular(ops.Function[float]):
    """  Return a random floating point number *N* such that *low* <= *N* <= *high* and 
        with the specified *mode* between those bounds.
        The *low* and *high* bounds default to zero and one.
        The *mode* argument defaults to the midpoint between the bounds,
        giving a symmetric distribution.
    """    

    def __init__(self, High = 1.0,Low = 0.0,Mode = 0.5):
        self.__dict__ = { 'High' : High,'Low' : Low,'Mode' : Mode }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'High' : float,'Low' : float,'Mode' : float }
    
    def _casts_to(self, dst):
        return triangular._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.triangular(self.High,self.Low,self.Mode)
    
    def __repr__(self):
        rv = "triangular"
        rv += "("
        for k in triangular._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Gamma distribution'])
class gammavariate(ops.Function[float]):
    """ Gamma distribution. Conditions on the parameters are |alpha| > 0 and |beta| > 0.
    
    The probability distribution function is: ::
    
                x ** (alpha - 1) * math.exp(-x / beta)
      pdf(x) =  --------------------------------------
                   math.gamma(alpha) * beta ** alpha
    """    

    def __init__(self, Alpha = 1.0,Beta = 1.0):
        self.__dict__ = { 'Alpha' : Alpha,'Beta' : Beta }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Alpha' : types.positive,'Beta' : types.positive }
    
    def _casts_to(self, dst):
        return gammavariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.gammavariate(self.Alpha,self.Beta)
    
    def __repr__(self):
        rv = "gammavariate"
        rv += "("
        for k in gammavariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Log normal distribution'])
class lognormvariate(ops.Function[float]):
    """  Log normal distribution.
        If you take the natural logarithm of this distribution, 
        you'll get a normal distribution with mean |mu| and standard deviation |sigma|. 
        |mu| can have any value, and |sigma| must be greater than zero.
    """    

    def __init__(self, Mu = 0.0,Sigma = 1.0):
        self.__dict__ = { 'Mu' : Mu,'Sigma' : Sigma }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Mu' : float,'Sigma' : types.positive }
    
    def _casts_to(self, dst):
        return lognormvariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.lognormvariate(self.Mu,self.Sigma)
    
    def __repr__(self):
        rv = "lognormvariate"
        rv += "("
        for k in lognormvariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Normal distribution'])
class normalvariate(ops.Function[float]):
    """ Normal distribution. |mu| is the mean, and |sigma| is the standard deviation.
    """    

    def __init__(self, Mu = 0.0,Sigma = 1.0):
        self.__dict__ = { 'Mu' : Mu,'Sigma' : Sigma }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Mu' : float,'Sigma' : types.positive }
    
    def _casts_to(self, dst):
        return normalvariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.normalvariate(self.Mu,self.Sigma)
    
    def __repr__(self):
        rv = "normalvariate"
        rv += "("
        for k in normalvariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Von Mises distribution'])
class vonmisesvariate(ops.Function[float]):
    """  |mu| is the mean angle, expressed in radians between 0 and 2|pi|, 
        and |kappa| is the concentration parameter, which must be greater than or equal to zero. 
        If |kappa| is equal to zero, this distribution reduces 
        to a uniform random angle over the range 0 to 2|pi|
    """    

    def __init__(self, Kappa = 0.0,Mu = 0.0):
        self.__dict__ = { 'Kappa' : Kappa,'Mu' : Mu }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Kappa' : types.non_negative,'Mu' : float }
    
    def _casts_to(self, dst):
        return vonmisesvariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.vonmisesvariate(self.Kappa,self.Mu)
    
    def __repr__(self):
        rv = "vonmisesvariate"
        rv += "("
        for k in vonmisesvariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Pareto distribution'])
class paretovariate(ops.Function[float]):
    """ Pareto distribution. |alpha| is the shape parameter.
    """    

    def __init__(self, Alpha = 1.0):
        self.__dict__ = { 'Alpha' : Alpha }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Alpha' : types.positive }
    
    def _casts_to(self, dst):
        return paretovariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.paretovariate(self.Alpha)
    
    def __repr__(self):
        rv = "paretovariate"
        rv += "("
        for k in paretovariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"


@registry.expose(['Random', 'Weibull distribution'])
class weibullvariate(ops.Function[float]):
    """ Weibull distribution. |alpha| is the scale parameter and |beta| is the shape parameter.
    """    

    def __init__(self, Alpha = 1.0,Beta = 1.0):
        self.__dict__ = { 'Alpha' : Alpha,'Beta' : Beta }
        
    @property
    def label(self):
        return repr(self)
        
    _properties = { 'Alpha' : types.positive,'Beta' : types.positive }
    
    def _casts_to(self, dst):
        return weibullvariate._types[0]._casts_to(dst)
    
    def __call__(self, *args, **kwargs):
        return random.weibullvariate(self.Alpha,self.Beta)
    
    def __repr__(self):
        rv = "weibullvariate"
        rv += "("
        for k in weibullvariate._properties:
            rv += (k + "=" + str(self.__dict__[k]) + ",")
        return rv[:-1] + ")"

