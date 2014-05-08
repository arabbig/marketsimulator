package marketsim.orderbook

import marketsim._

abstract class Entry
{
    val order : LimitOrder

    private var volumeUnmatched = order.volumeAbsolute

    def isEmpty = volumeUnmatched == 0
    def getVolumeUnmatched = volumeUnmatched

    def side : Side
    def canMatchWith(other : LimitOrder) : Boolean
    def signedTicks = makeSignedTicks(order.price)
    def makeSignedTicks(ticks : Int) : Ticks

    // returns unmatched volume of the other order
    def matchWith[T](other : Order[T], otherVolumeUnmatched : Volume) =
    {
        assert(otherVolumeUnmatched > 0)
        assert(volumeUnmatched > 0)

        val volume = otherVolumeUnmatched min volumeUnmatched
        val price = order.price

        order.OnTraded(price, volume)
        other.OnTraded(price, volume)

        volumeUnmatched -= volume
        otherVolumeUnmatched - volume
    }
}

final case class SellEntry(order : LimitOrder) extends Entry
{
    def side = Sell

    def canMatchWith(other : LimitOrder) = {
        assert(other.side == Buy)
        other.price >= order.price
    }

    def makeSignedTicks(price : Ticks) = price
}

final case class BuyEntry(order : LimitOrder) extends Entry
{
    def side = Buy

    def canMatchWith(other : LimitOrder) = {
        assert(other.side == Sell)
        other.price <= order.price
    }

    def makeSignedTicks(price : Ticks) = -price
}

object Entry
{
    def apply(order : LimitOrder) =
        order.side match {
            case Sell => new SellEntry(order)
            case Buy => new BuyEntry(order)
        }
}