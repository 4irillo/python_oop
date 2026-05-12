# ЛР-6 — Аннотации типов и дженерики

## Цель работы

* Освоить систему аннотаций типов в Python (`typing`).
* Реализовать обобщённые (generic) классы с использованием `TypeVar` и `Generic`.
* Применить структурную типизацию через `typing.Protocol`.
* Интегрировать типизацию с объектно-ориентированным кодом из предыдущих ЛР.

---

# Результат лабораторной

В репозитории должны появиться:

```
python_oop/
├─ README.md
├─ src/
│  ├─ Lab01/
│  ├─ ...
│  ├─ Lab06/
│  │   ├─ container.py
│  │   ├─ README.md
│  │   └─ demo.py
└─ img/
   └─ Lab06/
```

---

# Реализованные классы и протоколы

### Протоколы (`container.py`):

```
Displayable — объект умеет возвращать имя: get_name() -> str
Scorable    — объект умеет возвращать рейтинг: get_rating() -> float
```

### TypeVar с ограничениями:

```
TDisplayable = TypeVar('TDisplayable', bound=Displayable)
TScorable    = TypeVar('TScorable', bound=Scorable)
```

### Обобщённая коллекция:

```
TypedCollection[T]
├── add(item: T)
├── remove(item: T)
├── get_all() -> List[T]
├── find(predicate) -> Optional[T]
├── filter(predicate) -> TypedCollection[T]
├── map(transform) -> TypedCollection[U]
├── __len__()
├── __iter__()
└── __repr__()
```

### Функции через протоколы:

```
print_displayable(col: TypedCollection[TDisplayable])
find_top_scorer(col: TypedCollection[TScorable]) -> Optional[TScorable]
```

---

# Предметная область — Образование

Используется сущность **Teacher** из ЛР-1. Teacher удовлетворяет обоим протоколам структурно — без явного наследования:

| Метод / атрибут | Протокол |
|-----------------|----------|
| `get_name()` | `Displayable` |
| `get_rating()` | `Scorable` |

---

# Задание на 3

## Требования

1. ✅ Добавить аннотации типов к существующим классам из ЛР-1.
2. ✅ Создать обобщённый класс `TypedCollection[T]` с методами:
   * `add(item: T)`
   * `remove(item: T)`
   * `get_all() -> List[T]`

## Демонстрация

В `demo.py`:
* создание `TypedCollection[Teacher]`
* добавление и удаление объектов
* вызов `get_all()`

---

# Задание на 4

## Требования

0. ✅ Реализовать всё из задания на 3.
1. ✅ Методы `find()`, `filter()`, `map()`:
   * `find(predicate)` — возвращает первый подходящий элемент
   * `filter(predicate)` — возвращает новую `TypedCollection[T]`
   * `map(transform)` — преобразует элементы, возвращает `TypedCollection[U]`

## Демонстрация

* `find(lambda t: t.personal_info[0] == "Alice Johnson")` — поиск по имени
* `filter(lambda t: t.score >= 4.0)` — фильтрация по рейтингу
* `map(lambda t: t.personal_info[0])` — извлечение имён (`TypedCollection[str]`)
* `map(lambda t: t.score)` — извлечение оценок (`TypedCollection[float]`)

---

# Задание на 5

## Требования

0. ✅ Реализовать всё из заданий на 3 и 4.
1. ✅ Два протокола: `Displayable` и `Scorable` (с `@runtime_checkable`).
2. ✅ Ограниченные `TypeVar`: `TDisplayable`, `TScorable`.
3. ✅ Структурная типизация: `Teacher` удовлетворяет протоколам без наследования.
4. ✅ Функции через протоколы: `print_displayable`, `find_top_scorer`.

## Демонстрация

* `isinstance(alice, Displayable)` → `True` без наследования
* `isinstance(alice, Scorable)` → `True` без наследования
* `isinstance('string', Displayable)` → `False`
* `print_displayable(col)` — работает для `TypedCollection[TDisplayable]`
* `find_top_scorer(col)` — находит Teacher с максимальным рейтингом

---

# Структура модуля container.py

```python
container.py
├── T = TypeVar('T')
├── U = TypeVar('U')
├── Displayable (Protocol, runtime_checkable)
│   └── get_name() -> str
├── Scorable (Protocol, runtime_checkable)
│   └── get_rating() -> float
├── TDisplayable = TypeVar('TDisplayable', bound=Displayable)
├── TScorable = TypeVar('TScorable', bound=Scorable)
├── TypedCollection(Generic[T])
│   ├── __init__()
│   ├── add(item: T)
│   ├── remove(item: T)
│   ├── get_all() -> List[T]
│   ├── find(predicate) -> Optional[T]
│   ├── filter(predicate) -> TypedCollection[T]
│   ├── map(transform) -> TypedCollection[U]
│   ├── __len__()
│   ├── __iter__()
│   └── __repr__()
├── print_displayable(col: TypedCollection[TDisplayable])
└── find_top_scorer(col: TypedCollection[TScorable]) -> Optional[TScorable]
```

---

# Демонстрация работы demo.py

## Сценарий 1: Создание TypedCollection[Teacher]

Добавление 5 объектов `Teacher`, удаление одного и повторное добавление.
![img](/img/Lab06/1.png)

## Сценарий 2: find() и filter()

`find()` находит первый элемент, удовлетворяющий предикату.
`filter()` возвращает новую `TypedCollection[Teacher]` с подходящими элементами.
![img](/img/Lab06/2.png)

## Сценарий 3: map() — преобразование типа

`map(lambda t: t.personal_info[0])` возвращает `TypedCollection[str]`.
`map(lambda t: t.score)` возвращает `TypedCollection[float]`.
![img](/img/Lab06/3.png)

## Сценарий 4: Протокол Displayable

`isinstance(alice, Displayable)` → `True`.
`isinstance('string', Displayable)` → `False`.
Функция `print_displayable()` работает с любым `TypedCollection[TDisplayable]`.
![img](/img/Lab06/4.png)

## Сценарий 5: Протокол Scorable

`isinstance(alice, Scorable)` → `True` — структурная типизация без наследования.
`find_top_scorer(col)` находит преподавателя с наивысшим рейтингом.
![img](/img/Lab06/5.png)

## Сценарий 6: Ограниченные TypeVar

Создание `TypedCollection[TDisplayable]` и `TypedCollection[TScorable]`.
Демонстрация `print_displayable` и `find_top_scorer` с bounded TypeVar.
![img](/img/Lab06/6.png)

## Сценарий 7: Цепочка операций

`col.filter(...).filter(...).map(...)` — вложенные преобразования с сохранением типа.
![img](/img/Lab06/7.png)

---

# Критерии допуска

* ✅ Работа выполнена полностью (на 5)
* ✅ Есть демонстрационный файл `demo.py`
* ✅ Наличие отчёта в `README.md`
* ✅ Реализован generic класс `TypedCollection[T]`
* ✅ Реализованы протоколы `Displayable` и `Scorable`
* ✅ Продемонстрирована структурная типизация через `isinstance`
