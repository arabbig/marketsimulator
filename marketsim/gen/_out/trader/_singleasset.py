from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim.gen._out._iorderbook import IOrderBook
from marketsim.gen._intrinsic.trader.classes import SingleAsset_Impl
from marketsim import listOf
from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy

class SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie(ISingleAssetTrader,SingleAsset_Impl):
    """ **A trader that trades a single asset on a single market**
    
    
    Parameters are:
    
    **orderBook**
    	 order book for the asset being traded 
    
    **strategy**
    	 strategy run by the trader 
    
    **name**
    
    **amount**
    	 current position of the trader (number of assets that it owns) 
    
    **PnL**
    	 current trader balance (number of money units that it owns) 
    
    **timeseries**
    	 defines what data should be gathered for the trader 
    """ 
    def __init__(self, orderBook , strategy = None, name = None, amount = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._empty import Empty_ as _strategy_Empty_
        from marketsim import deref_opt
        from marketsim import rtti
        self.orderBook = orderBook
        self.strategy = strategy if strategy is not None else deref_opt(_strategy_Empty_())
        self.name = name if name is not None else "-trader-"
        self.amount = amount if amount is not None else 0.0
        self.PnL = PnL if PnL is not None else 0.0
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        SingleAsset_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'orderBook' : IOrderBook,
        'strategy' : ISingleAssetStrategy,
        'name' : str,
        'amount' : float,
        'PnL' : float,
        'timeseries' : listOf(ITimeSerie)
    }
    
    
    
    
    
    
    
    
    
    
    
    
    def __repr__(self):
        return "%(name)s" % dict([ (name, getattr(self, name)) for name in self._properties.iterkeys() ])
    
    def bind_ex(self, ctx):
        if hasattr(self, '_processing_ex'):
            raise Exception('cycle detected')
        setattr(self, '_processing_ex', True)
        self._ctx_ex = self.updateContext_ex(ctx) if hasattr(self, 'updateContext_ex') else ctx
        self.orderBook.bindEx(self._ctx_ex)
        self.strategy.bindEx(self._ctx_ex)
        for x in self.timeseries: x.bind(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def SingleAsset(orderBook = None,strategy = None,name = None,amount = None,PnL = None,timeseries = None): 
    from marketsim import rtti
    from marketsim.gen._out._itimeserie import ITimeSerie
    from marketsim.gen._out._iorderbook import IOrderBook
    from marketsim.gen._out._isingleassetstrategy import ISingleAssetStrategy
    from marketsim import listOf
    if orderBook is None or rtti.can_be_casted(orderBook, IOrderBook):
        if strategy is None or rtti.can_be_casted(strategy, ISingleAssetStrategy):
            if name is None or rtti.can_be_casted(name, str):
                if amount is None or rtti.can_be_casted(amount, float):
                    if PnL is None or rtti.can_be_casted(PnL, float):
                        if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                            return SingleAsset_IOrderBookISingleAssetStrategyStringFloatFloatListITimeSerie(orderBook,strategy,name,amount,PnL,timeseries)
    raise Exception('Cannot find suitable overload for SingleAsset('+str(orderBook) +':'+ str(type(orderBook))+','+str(strategy) +':'+ str(type(strategy))+','+str(name) +':'+ str(type(name))+','+str(amount) +':'+ str(type(amount))+','+str(PnL) +':'+ str(type(PnL))+','+str(timeseries) +':'+ str(type(timeseries))+')')