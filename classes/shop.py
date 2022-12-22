from classes.abstract_class import Storage


class Shop(Storage):
    def __init__(self, items={}, capacity=20, unique_items_count=5):
        if sum(items.values()) <= capacity and len(items) <= unique_items_count:
            self._items = items
            self._capacity = capacity
            self._unique_items_count = unique_items_count
        else:
            print("Неверные входные данные")
            self._items = {}
            self._capacity = capacity
            self._unique_items_count = unique_items_count

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def unique_items_count(self):
        return self._unique_items_count

    def add(self, title, cnt):
        if self.get_unique_items_count() < self.unique_items_count() and self.get_free_space() >= cnt:
            self.items[title] = self.items.get(title, 0) + cnt
        else:
            raise Exception(f"В магазине нет места под новый товар")

    def remove(self, title, cnt):
        if title in self.items:
            if self.items[title] > cnt:
                self.items[title] -= cnt
            elif self.items[title] == cnt:
                del self.items[title]
            else:
                raise Exception(f"Товара {title} недостаточно")
        else:
            raise Exception(f"Продукта {title} нет на складе")

    def _get_sum(self):
        return sum(self.items.values())

    def get_free_space(self):
        return self.capacity - self._get_sum()

    def get_items(self):
        return self.items

    def get_unique_items_count(self):
        return len(self.items)
