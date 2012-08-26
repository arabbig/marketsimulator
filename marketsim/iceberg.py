from marketsim.order import OrderBase

class Volume(object):
    """ Auxiliary class to hold market order initialization parameters 
    """
    def __init__(self, v):
        self._volume = v

    hasPrice = False

    @property
    def packed(self):
        """ Returns a tuple (volume)"""
        return self._volume,

class PriceVolume(object):
    """ Auxiliary class to hold limit order initialization parameters 
    """

    def __init__(self, p, v):
        self._price = p
        self._volume = v

    hasPrice = True

    @property
    def packed(self):
        """ Returns a tuple (price, volume)"""
        return self._price, self._volume

def unpack(args):
    """ Unpacks from args volume (and possibly) price of order to create 
    """
    return PriceVolume(*args) if len(args) == 2 else Volume(*args)

class IcebergOrder(OrderBase):
    """ Virtual order that implements iceberg strategy:
    First it sends an order for a small potion of its volume to a book and
    once it is filled resends a new order 
    """

    def __init__(self, volumeLimit, orderFactory, *args):
        """ Initializes iceberg order
        volumeLimit -- maximal volume for order that can be sent
        orderFactory -- factory to create real orders: *args -> Order
        *args -- parameters to be passed to real orders
        """
        self._args = unpack(args)
        # we pretend that we are an order initially having given volume
        OrderBase.__init__(self, self._args._volume)
        self._volumeLimit = volumeLimit
        self._orderFactory = orderFactory
        self._current = None

    @property
    def price(self):  # NB! defined only for limit orders
        assert self._args.hasPrice
        return self._args._price

    def _onMatchedWith(self, myOrder, other, pv):
        """ Called when real order has been matched
        We notify our listeners about the trade
        and if it is matched completely try to resend a new order
        """
        self.on_matched.fire(self, other, pv)
        if self._current.empty:
            self._PnL += self._current.PnL
            self._tryToResend()

    def cancel(self):
        """ If we are asked to be cancelled, we mark ourselves as cancelled 
        and the make the real order also cancelled 
        """
        OrderBase.cancel(self)
        if self._current:
            self._current.cancel()

    @property
    def PnL(self):
        """ Returns P&L. It sum of P&L of traded orders and P&L of the order being traded
        """
        return self._PnL + (self._current.PnL if self._current else 0)

    @property
    def volume(self):
        """ Returns volume left to trade. 
        """
        return self._volume + (self._current.volume if self._current else 0)

    def _tryToResend(self):
        """ Tries to send a real order to the order book
        """
        # if we have something to trade
        if self._volume > 0: 
            # define volume to trade
            v = min(self._volumeLimit, self._volume)
            self._args._volume = v
            # diminish our volume to trade
            self._volume -= v
            # create a real order
            self._current = self._orderFactory(*self._args.packed)
            # start listening events about order matching
            self._current.on_matched += self._onMatchedWith
            # and send the order to the order book    
            self._book.process(self._current)
        else:
            # now we have nothing to trade
            self._current = None

    def processIn(self, book):
        """ Called when an order book tries to determine 
        how the order should be processed 
        """
        self._book = book
        self._tryToResend()

def iceberg(volumeLimit, orderFactory):
    """ Returns a function to create iceberg orders with 
    given volumeLimit and orderFactory to create real orders
    """
    def inner(*args):
        return IcebergOrder(volumeLimit, orderFactory, *args)
    return inner