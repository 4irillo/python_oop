# ЛР-5 — Функции как аргументы. Стратегии и делегаты.

## Цель работы

* Освоить передачу функций как аргументов в другие функции и методы.
* Применить встроенные функции высшего порядка: `map`, `filter`, `sorted`.
* Реализовать паттерн «Стратегия» через `callable`-объекты.
* Освоить `lambda`-выражения и их практическое применение.
* Интегрировать функциональный стиль с объектно-ориентированным кодом из ЛР-1 и ЛР-2.

---

# Результат лабораторной

В репозитории должны появиться:

```
python_oop/
├─ README.md
├─ src/
│  ├─ Lab01/
│  ├─ Lab02/
│  ├─ Lab03/
│  ├─ Lab04/
│  ├─ Lab05/
│  │   ├─ strategies.py
│  │   ├─ collection.py
│  │   ├─ README.md
│  │   └─ demo.py
└─ img/
   └─ Lab05/
```

---

**ВАЖНО:** Лабораторная строится поверх кода из ЛР-1. Используются объекты `Teacher`.

---

# Реализованные функции и стратегии

### Функции-стратегии сортировки (`strategies.py`):

```
by_name      — сортировка по имени
by_age       — сортировка по возрасту
by_subject   — сортировка по предмету
by_score     — сортировка по рейтингу
```

### Функции-фильтры (`strategies.py`):

```
is_active    — только активные преподаватели
has_groups   — только преподаватели с назначенными группами
```

### Фабрики функций (`strategies.py`):

```
make_subject_filter(subject)      — создаёт фильтр по предмету
make_min_score_filter(min_score)  — создаёт фильтр по минимальному рейтингу
```

### Функции преобразования (`strategies.py`):

```
to_summary   — преобразует Teacher в строку-сводку
to_name      — извлекает имя преподавателя
```

### Callable-объекты (паттерн «Стратегия»):

```
ByScoreDescStrategy      — ключ сортировки по убыванию рейтинга
ActivateStrategy         — активирует преподавателя
DeactivateIfIdleStrategy — деактивирует преподавателей без групп
```

### Методы коллекции (`collection.py`):

```
StrategyCollection
├── add()
├── remove()
├── get_all()
├── get_active()
├── sort_by(key_func)   — сортировка с функцией-стратегией, возвращает новую коллекцию
├── filter_by(predicate) — фильтрация с предикатом, возвращает новую коллекцию
├── apply(func)         — применяет функцию к каждому элементу, поддерживает цепочку
├── map_to(transform)   — преобразует элементы, возвращает список
├── __len__()
├── __iter__()
└── __repr__()
```

---

# Предметная область — Образование

Используется сущность **Teacher** (Преподаватель) из ЛР-1.

| Атрибут | Тип | Описание |
|---------|-----|----------|
| `personal_info[0]` | str | Имя преподавателя |
| `personal_info[1]` | int | Возраст |
| `subject` | str | Предмет |
| `score` | float | Средний рейтинг |
| `active` | bool | Активность |
| `groups` | set | Назначенные группы |

---

# Задание на 3

## Требования

1. ✅ Минимум 3 функции-стратегии сортировки (`by_name`, `by_age`, `by_subject`).
2. ✅ Использование `sorted()` с параметром `key=`.
3. ✅ Минимум 2 функции-фильтра (`is_active`, `has_groups`).
4. ✅ Применение встроенной функции `filter()`.
5. ✅ Передача функций как аргументов (ссылка, а не вызов).

## Демонстрация

В `demo.py`:
* создание коллекции из 6 объектов `Teacher`
* сортировка тремя стратегиями: `by_name`, `by_age`, `by_score`
* фильтрация двумя функциями через `filter()`: `is_active`, `has_groups`

---

# Задание на 4

## Требования

0. ✅ Реализовать всё из задания на 3.
1. ✅ `map()` для преобразования коллекции (`to_summary`, `to_name`).
2. ✅ Фабрики функций: `make_subject_filter()`, `make_min_score_filter()`.
3. ✅ Методы `sort_by(key_func)` и `filter_by(predicate)` в `StrategyCollection`.
4. ✅ `lambda` там, где функция проста и не переиспользуется.

## Демонстрация

* `map(to_summary, ...)` — преобразование всех Teacher в строки
* сравнение `map(to_name, ...)` vs `map(lambda t: t.personal_info[0], ...)`
* создание фильтра через фабрику и применение
* вызов `col.sort_by()` и `col.filter_by()`

---

# Задание на 5

## Требования

0. ✅ Реализовать всё из заданий на 3 и 4.
1. ✅ Паттерн «Стратегия» через `callable`-объекты (`ByScoreDescStrategy`, `ActivateStrategy`, `DeactivateIfIdleStrategy`).
2. ✅ Метод `apply(func)` — применяет произвольную функцию ко всем элементам.
3. ✅ Цепочка операций: `filter_by → sort_by → apply`.
4. ✅ Все стратегии вынесены в `strategies.py` с `docstring`.

## Демонстрация

* **Сценарий 1:** цепочка `filter_by(is_active).sort_by(by_score).apply(ActivateStrategy())`
* **Сценарий 2:** замена стратегии без изменения кода — `by_subject`, `by_age`, `ByScoreDescStrategy()`
* **Сценарий 3:** callable-объект `DeactivateIfIdleStrategy` как стратегия обработки

---

# Структура модулей

```python
strategies.py
├── by_name(teacher)
├── by_age(teacher)
├── by_subject(teacher)
├── by_score(teacher)
├── is_active(teacher)
├── has_groups(teacher)
├── make_subject_filter(subject)
├── make_min_score_filter(min_score)
├── to_summary(teacher)
├── to_name(teacher)
├── ByScoreDescStrategy
│   └── __call__(teacher)
├── ActivateStrategy
│   └── __call__(teacher)
└── DeactivateIfIdleStrategy
    └── __call__(teacher)

collection.py
└── StrategyCollection
    ├── _from_list(items)      [classmethod]
    ├── add(teacher)
    ├── remove(teacher)
    ├── get_all()
    ├── get_active()
    ├── sort_by(key_func)
    ├── filter_by(predicate)
    ├── apply(func)
    ├── map_to(transform)
    ├── __len__()
    ├── __iter__()
    └── __repr__()
```

---

# Демонстрация работы demo.py

## Сценарий 1: Создание коллекции

Создание 6 объектов `Teacher` с разными атрибутами и добавление в `StrategyCollection`.
![img](/img/Lab05/1.png)

## Сценарий 2: Три стратегии сортировки

Одна коллекция сортируется тремя стратегиями: по имени, по возрасту, по рейтингу.
![img](/img/Lab05/2.png)

## Сценарий 3: Фильтрация через filter()

Применение `filter(is_active, ...)` и `filter(has_groups, ...)`.
![img](/img/Lab05/3.png)

## Сценарий 4: map() и lambda

Преобразование коллекции через `map(to_summary, ...)`. Сравнение `to_name` и `lambda`.
![img](/img/Lab05/4.png)

## Сценарий 5: Фабрики функций

`make_subject_filter("Mathematics")` и `make_min_score_filter(4.0)`.
![img](/img/Lab05/5.png)

## Сценарий 6: Методы коллекции sort_by / filter_by

Вызов `col.sort_by(by_name)`, `col.filter_by(is_active)`, `col.map_to(to_summary)`.
![img](/img/Lab05/6.png)

## Сценарий 7: Цепочка filter_by → sort_by → apply

Полная цепочка: фильтрация активных → сортировка по рейтингу → применение `ActivateStrategy`.
![img](/img/Lab05/7.png)

## Сценарий 8: Замена стратегии

Одна и та же цепочка с разными функциями-стратегиями — разный результат.
![img](/img/Lab05/8.png)

## Сценарий 9: Callable-объект как стратегия

`DeactivateIfIdleStrategy` применяется через `col.apply()`, затем восстановление через `ActivateStrategy`.
![img](/img/Lab05/9.png)

---

# Критерии допуска

* ✅ Работа выполнена полностью (на 5)
* ✅ Есть демонстрационный файл `demo.py`
* ✅ Наличие отчёта в `README.md`
* ✅ Реализована передача функций как аргументов
* ✅ Реализован паттерн «Стратегия» через callable-объекты
* ✅ Все стратегии вынесены в `strategies.py` с `docstring`
