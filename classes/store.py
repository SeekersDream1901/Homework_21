from classes.abstract_class import Storage


class Store(Storage):
    def __init__(self, items={}, capacity=100):
        if sum(items.values()) <= capacity:
            self._items = items
            self._capacity = capacity
        else:
            print("Неверные входные данные")
            self._items = {}
            self._capacity = capacity

    @property
    def items(self):
        return self._items

    @property
    def capacity(self):
        return self._capacity

    def add(self, title, cnt):
        if self.get_free_space() > cnt:
            self.items[title] = self.items.get(title, 0) + cnt
        else:
            raise Exception(f"Нет места на складе")

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
