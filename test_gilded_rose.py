import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)
        self.assertEqual(-1, items[0].sell_in)

    def test_quality_never_negative(self):
        items = [Item("Milk", 2, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)

    def test_quality_never_above_fifty(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(1, items[0].sell_in)
        self.assertEqual(50, items[0].quality)

    def test_aged_brie_increase_quality(self):
        items = [Item("Aged Brie", 10, 16)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(17, items[0].quality)

    def test_quality_increaseby2_after_sell_date(self):
        items = [Item("Aged Brie", -1, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-2, items[0].sell_in)
        self.assertEqual(2, items[0].quality)

    def test_backstage_quality_increase(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 12, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(4, items[0].quality)
        self.assertEqual(11, items[0].sell_in)

    def test_backstage_quality_increase_by2(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 10, 3)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(5, items[0].quality)
        self.assertEqual(9, items[0].sell_in)

    def test_backstage_quality_increase_by3(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 13)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(16, items[0].quality)
        self.assertEqual(4, items[0].sell_in)

    def test_backstage_quality_drops_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 16)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_sulfuras_never_alters(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 10, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80, items[0].quality)
        
    def test_conjured(self):
        items = [Item("Conjured", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(48, items[0].quality)

    def test_conjured_beyond_selldate(self):
        items = [Item("Conjured", -1, 4)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0, items[0].quality)


if __name__ == '__main__':
    unittest.main()
