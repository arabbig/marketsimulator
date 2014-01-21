from marketsim import registry
from marketsim.ops._function import Function
from marketsim import Side
from marketsim import IOrderBook
from marketsim.gen._out.strategy.side._FundamentalValue import FundamentalValue as _strategy_side_FundamentalValue
from marketsim.gen._out.math.EW._Avg import Avg as _math_EW_Avg
from marketsim.gen._out.orderbook._MidPrice import MidPrice as _orderbook_MidPrice
from marketsim import context
@registry.expose(["Side function", "MeanReversion"])
class MeanReversion(Function[Side]):
    """ 
    """ 
    def __init__(self, alpha = None, book = None):
        from marketsim.gen._out.orderbook._OfTrader import OfTrader as _orderbook_OfTrader
        self.alpha = alpha if alpha is not None else 0.015
        self.book = book if book is not None else _orderbook_OfTrader()
        self.impl = self.getImpl()
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'alpha' : float,
        'book' : IOrderBook
    }
    def __repr__(self):
        return "MeanReversion(%(alpha)s, %(book)s)" % self.__dict__
    
    _internals = ['impl']
    def getImpl(self):
        return _strategy_side_FundamentalValue(_math_EW_Avg(_orderbook_MidPrice(self.book),self.alpha),self.book)
    
    
    
    def bind(self, ctx):
        self._ctx = ctx.clone()
    
    def reset(self):
        self.impl = self.getImpl()
        ctx = getattr(self, '_ctx', None)
        if ctx: context.bind(self.impl, ctx)
    
    def __call__(self, *args, **kwargs):
        return self.impl()
    