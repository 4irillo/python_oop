import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Lab01'))

from model import Teacher


class StrategyCollection:
    def __init__(self):
        self._items = []

    @classmethod
    def _from_list(cls, items):
        col = cls.__new__(cls)
        col._items = list(items)
        return col

    def add(self, teacher: Teacher) -> None:
        if not isinstance(teacher, Teacher):
            raise ValueError("Item must be a Teacher instance.")
        self._items.append(teacher)

    def remove(self, teacher: Teacher) -> None:
        if teacher not in self._items:
            raise ValueError("Teacher not found in collection.")
        self._items.remove(teacher)

    def get_all(self) -> list:
        return self._items.copy()

    def get_active(self) -> list:
        return [t for t in self._items if t.active]

    def sort_by(self, key_func) -> 'StrategyCollection':
        return StrategyCollection._from_list(sorted(self._items, key=key_func))

    def filter_by(self, predicate) -> 'StrategyCollection':
        return StrategyCollection._from_list(item for item in self._items if predicate(item))

    def apply(self, func) -> 'StrategyCollection':
        for item in self._items:
            func(item)
        return self

    def map_to(self, transform) -> list:
        return list(map(transform, self._items))

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"StrategyCollection(count={len(self._items)})"
