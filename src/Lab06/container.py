from typing import TypeVar, Generic, List, Optional, Callable, Protocol, runtime_checkable

T = TypeVar('T')
U = TypeVar('U')


@runtime_checkable
class Displayable(Protocol):
    def get_name(self) -> str: ...


@runtime_checkable
class Scorable(Protocol):
    def get_rating(self) -> float: ...


TDisplayable = TypeVar('TDisplayable', bound=Displayable)
TScorable = TypeVar('TScorable', bound=Scorable)


class TypedCollection(Generic[T]):
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        self._items.append(item)

    def remove(self, item: T) -> None:
        self._items.remove(item)

    def get_all(self) -> List[T]:
        return self._items.copy()

    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> 'TypedCollection[T]':
        result: TypedCollection[T] = TypedCollection()
        result._items = [item for item in self._items if predicate(item)]
        return result

    def map(self, transform: Callable[[T], U]) -> 'TypedCollection[U]':
        result: TypedCollection[U] = TypedCollection()
        result._items = [transform(item) for item in self._items]
        return result

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self) -> str:
        return f"TypedCollection(count={len(self._items)})"


def print_displayable(col: 'TypedCollection[TDisplayable]') -> None:
    for item in col:
        print(f"  {item.get_name()}")


def find_top_scorer(col: 'TypedCollection[TScorable]') -> Optional[TScorable]:
    all_items = col.get_all()
    if not all_items:
        return None
    return max(all_items, key=lambda x: x.get_rating())
