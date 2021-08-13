from gilded_rose import *

import unittest


class GildedRoseTest(unittest.TestCase):

    def setUp(self):
        self.items = []

      # longMessage = True  

    def test_update_quality_with_a_single_normal_item(self):
        self.items.append(Item("NORMAL ITEM", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'sell_in': 4}
        item = self.items[0]
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_update_quality_with_a_single_normal_item_before_sell_date(self):
        self.items.append(Item("NORMAL ITEM", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'sell_in': 4}
        item = self.items[0]
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_update_quality_with_a_single_normal_item_on_sell_date(self):
        self.items.append(Item("NORMAL ITEM", 0, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 8 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_normal_item_after_sell_date(self):
        self.items.append(Item("NORMAL ITEM", -10, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 8 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_normal_item_of_zero_quality(self):
        self.items.append(Item("NORMAL ITEM", 5, 0))
        GildedRose(self.items).update_quality()
        expected = {'quality': 0 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_aged_brie_item(self):
        self.items.append(Item("Aged Brie", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'sell_in': 4 }
        item = self.items[0]
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_update_quality_with_a_single_aged_brie_item_before_sell_date(self):
        self.items.append(Item("Aged Brie", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 11 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_aged_brie_item_before_sell_date_with_max_quality(self):
        self.items.append(Item("Aged Brie", 5, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_aged_brie_item_on_sell_date(self):
        self.items.append(Item("Aged Brie", 0, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 12 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_aged_brie_item_on_sell_date_with_near_max_quality(self):
        self.items.append(Item("Aged Brie", 0, 49))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_aged_brie_item_on_sell_date_with_max_quality(self):
        self.items.append(Item("Aged Brie", 0, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_aged_brie_item_after_sell_date(self):
        self.items.append(Item("Aged Brie", -10, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 12 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_aged_brie_item_after_sell_date_with_max_quality(self):
        self.items.append(Item("Aged Brie", -10, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_sulfuras_item(self):
        self.items.append(Item("Sulfuras, Hand of Ragnaros", 5, 80))
        GildedRose(self.items).update_quality()
        expected = {'sell_in': 5 }
        item = self.items[0]
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_update_quality_with_a_single_sulfuras_item_before_sell_date(self):
        self.items.append(Item("Sulfuras, Hand of Ragnaros", 5, 80))
        GildedRose(self.items).update_quality()
        expected = {'quality': 80 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_sulfuras_item_on_sell_date(self):
        self.items.append(Item("Sulfuras, Hand of Ragnaros", 0, 80))
        GildedRose(self.items).update_quality()
        expected = {'quality': 80 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_sulfuras_item_after_sell_date(self):
        self.items.append(Item("Sulfuras, Hand of Ragnaros", -10, 80))
        GildedRose(self.items).update_quality()
        expected = {'quality': 80 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'sell_in': 4 }
        item = self.items[0]
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_update_quality_with_a_single_backstage_pass_long_before_sell_date(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 11, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 11 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_long_before_sell_date_at_max_quality(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 11, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_medium_close_to_sell_date_with_upper_bound(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 10, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 12 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_medium_close_to_sell_date_with_upper_bound_at_max_quality(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 10, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_medium_close_to_sell_date_with_lower_bound(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 6, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 12 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_with_medium_close_to_sell_date_with_lower_bound_at_max_quality(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 6, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_with_very_close_to_sell_date_with_upper_bound(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 13 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_with_very_close_to_sell_date_with_upper_bound_at_max_quality(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 5, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_with_very_close_to_sell_date_with_lower_bound(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 1, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 13 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_with_very_close_to_sell_date_with_lower_bound_at_max_quality(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 1, 50))
        GildedRose(self.items).update_quality()
        expected = {'quality': 50 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_on_sell_date(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", 0, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 0 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_backstage_pass_after_sell_date(self):
        self.items.append(Item("Backstage passes to a TAFKAL80ETC concert", -10, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 0 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])
  
    def test_update_quality_with_a_single_conjured_item(self):
        self.items.append(Item("Conjured Mana Cake", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'sell_in': 4 }
        item = self.items[0]
        self.assertEqual(item.sell_in, expected['sell_in'])

    def test_update_quality_with_conjured_item_before_the_sell_date(self):
        self.items.append(Item("Conjured Mana Cake", 5, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 8}
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_conjured_item_before_the_sell_date_at_zero_quality(self):
        self.items.append(Item("Conjured Mana Cake", 5, 0))
        GildedRose(self.items).update_quality()
        expected = {'quality': 0 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_conjured_item_on_the_sell_date(self):
        self.items.append(Item("Conjured Mana Cake", 0, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 6 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_conjured_item_on_the_sell_date_at_zero_quality(self):
        self.items.append(Item("Conjured Mana Cake", 0, 0))
        GildedRose(self.items).update_quality()
        expected = {'quality': 0 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_conjured_item_after_sell_date(self):
        self.items.append(Item("Conjured Mana Cake", -10, 10))
        GildedRose(self.items).update_quality()
        expected = {'quality': 6 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_with_a_single_conjured_item_after_sell_date_at_zero_quality(self):
        self.items.append(Item("Conjured Mana Cake", -10, 0))
        GildedRose(self.items).update_quality()
        expected = {'quality': 0 }
        item = self.items[0]
        self.assertEqual(item.quality, expected['quality'])

    def test_update_quality_order_with_several_objects(self):
        self.items.append(Item("NORMAL ITEM", 5, 10))
        self.items.append(Item("Aged Brie", 3, 10))
        GildedRose(self.items).update_quality()
        expected = [
            {'quality': 9 , 'sell_in': 4},
            {'quality': 11, 'sell_in': 2 }
        ]

        for index, expectation in enumerate(expected):
            item = self.items[index]
            self.assertEqual(item.quality, expectation['quality'])
            self.assertEqual(item.sell_in, expectation['sell_in'])

if __name__ == '__main__':
        unittest.main()