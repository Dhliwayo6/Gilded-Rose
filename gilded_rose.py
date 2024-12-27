class GildedRose:
    def __init__(self, items):
        self.items = items

    def decrease_quality(self, item):
        if item.quality > 0:
            item.quality -= 1

    def increment_quality(self, item):
        if item.quality < 50:
            item.quality += 1

    def decrease_sell_in(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in -= 1

    def reset_quality_to_0(self, item):
        item.quality = 0

    def aged_brie(self, item):
        ...

    def normal_update(self, item):
        ...

    def backstage_passes(self, item):
        ...

    def conjured(self, item):
        ...
     
    def update_quality(self):   

        ...


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
