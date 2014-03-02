@category = "Price function"

package strategy.price() {
    type LiquidityProvider(/** initial price which is taken if orderBook is empty */ initialValue = 100.0,/** defines multipliers for current asset price when price of
      *             order to create is calculated*/ priceDistr = .math.random.lognormvariate(0.0,0.1),/** asset in question */ book = .orderbook.OfTrader())
    {
        // defined at defs\strategies\parts\price.sc: 13.9
        def Price(side = .side.Sell() : IFunction[Side]) = book~>Queue(side)~>SafeSidePrice(initialValue)*priceDistr
        
        // defined at defs\strategies\parts\price.sc: 17.9
        def OneSideStrategy(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                            /** order factory function*/ orderFactory = order.side_price.Limit(),
                            /** side of orders to create */ side = .side.Sell()) = orderFactory(side,Price(side))~>Strategy(eventGen)
        
        // defined at defs\strategies\parts\price.sc: 27.9
        def Strategy(/** Event source making the strategy to wake up*/ eventGen = event.Every(math.random.expovariate(1.0)),
                     /** order factory function*/ orderFactory = order.side_price.Limit()) = Combine(OneSideStrategy(eventGen,orderFactory,side.Sell()),OneSideStrategy(eventGen,orderFactory,side.Buy()))
    }
}
