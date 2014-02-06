from marketsim import IFunction
from marketsim import IOrderGenerator
from marketsim import Side
from marketsim import registry
from marketsim import float
@registry.expose(["Order", "price_ImmediateOrCancel"])
class sidevolume_price_ImmediateOrCancel(IFunction[IFunction[IOrderGenerator,IFunction[float]],IFunction[Side]
,IFunction[float]]):
    """ 
      Immediate-Or-Cancel order sends an underlying order to the market and
      immediately sends a cancel request for it.
      It allows to combine market and limit order behaviour:
      the order is either executed immediately
      at price equal or better than given one
      either it is cancelled (and consequently never stored in the order queue).
    """ 
    def __init__(self, proto = None):
        from marketsim.gen._out.order._curried._sidevolume_price_Limit import sidevolume_price_Limit as _order__curried_sidevolume_price_Limit
        from marketsim import rtti
        self.proto = proto if proto is not None else _order__curried_sidevolume_price_Limit()
        rtti.check_fields(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'proto' : IFunction[IFunction[IOrderGenerator, IFunction[float]], IFunction[Side],IFunction[float]]
    }
    def __repr__(self):
        return "price_ImmediateOrCancel(%(proto)s)" % self.__dict__
    
    def __call__(self, side = None,volume = None):
        from marketsim.gen._out.side._Sell import Sell as _side_Sell
        from marketsim.gen._out._constant import constant as _constant
        from marketsim.gen._out.order._curried._price_ImmediateOrCancel import price_ImmediateOrCancel
        side = side if side is not None else _side_Sell()
        volume = volume if volume is not None else _constant(1.0)
        proto = self.proto
        return price_ImmediateOrCancel(proto(side,volume))
    
sidevolume_price_ImmediateOrCancel = sidevolume_price_ImmediateOrCancel
