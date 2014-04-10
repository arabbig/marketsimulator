from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
from marketsim import registry
from marketsim.gen._out._itrader import ITrader
from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
from marketsim.gen._out._itimeserie import ITimeSerie
from marketsim import listOf
from marketsim.gen._intrinsic.trader.classes import MultiAsset_Impl
@registry.expose(["Trader", "MultiAsset"])
class MultiAsset_ListISingleAssetTraderIMultiAssetStrategyStringFloatListITimeSerie(ITrader,MultiAsset_Impl):
    """ **A trader that trades different assets**
    
      It can be considered as a composition of single asset traders and multi asset strategies
      At the moment there is no way to instruct a multi asset strategy to trade only on subset of the assets
    
    Parameters are:
    
    **traders**
    	 defines accounts for every asset to trade 
    
    **strategy**
    	 multi asset strategy run by the trader 
    
    **name**
    
    **PnL**
    	 current trader balance (number of money units that it owns) 
    
    **timeseries**
    	 defines what data should be gathered for the trader 
    """ 
    def __init__(self, traders = None, strategy = None, name = None, PnL = None, timeseries = None):
        from marketsim.gen._out.strategy._arbitrage import Arbitrage_ as _strategy_Arbitrage_
        from marketsim import deref_opt
        from marketsim import rtti
        self.traders = traders if traders is not None else []
        self.strategy = strategy if strategy is not None else deref_opt(_strategy_Arbitrage_())
        self.name = name if name is not None else "-trader-"
        self.PnL = PnL if PnL is not None else 0.0
        self.timeseries = timeseries if timeseries is not None else []
        rtti.check_fields(self)
        MultiAsset_Impl.__init__(self)
    
    @property
    def label(self):
        return repr(self)
    
    _properties = {
        'traders' : listOf(ISingleAssetTrader),
        'strategy' : IMultiAssetStrategy,
        'name' : str,
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
        for x in self.traders: x.bind(self._ctx_ex)
        self.strategy.bindEx(self._ctx_ex)
        for x in self.timeseries: x.bind(self._ctx_ex)
        delattr(self, '_processing_ex')
    
def MultiAsset(traders = None,strategy = None,name = None,PnL = None,timeseries = None): 
    from marketsim import rtti
    from marketsim.gen._out._itimeserie import ITimeSerie
    from marketsim.gen._out._isingleassettrader import ISingleAssetTrader
    from marketsim import listOf
    from marketsim.gen._out._imultiassetstrategy import IMultiAssetStrategy
    if traders is None or rtti.can_be_casted(traders, listOf(ISingleAssetTrader)):
        if strategy is None or rtti.can_be_casted(strategy, IMultiAssetStrategy):
            if name is None or rtti.can_be_casted(name, str):
                if PnL is None or rtti.can_be_casted(PnL, float):
                    if timeseries is None or rtti.can_be_casted(timeseries, listOf(ITimeSerie)):
                        return MultiAsset_ListISingleAssetTraderIMultiAssetStrategyStringFloatListITimeSerie(traders,strategy,name,PnL,timeseries)
    raise Exception('Cannot find suitable overload for MultiAsset('+str(traders) +':'+ str(type(traders))+','+str(strategy) +':'+ str(type(strategy))+','+str(name) +':'+ str(type(name))+','+str(PnL) +':'+ str(type(PnL))+','+str(timeseries) +':'+ str(type(timeseries))+')')