# Лаба1
**Что есть учитель?**  \
Т.к. мой номер 21, мне выпала тема №1 (образование) и я выбрал создать класс учителя.
Что на мой взгляд характеризует учителя? 
 - Предмет преподавания
 - Группы, которым он преподает 
 - +-личная информация о нем
 - Его рейтинг среди студентов
Непосредстевнно этими атрибутами я и наделили его.
```python
class Teacher: 
    # Public vars
    subject: str
    groups: set
    personal_info: list  # [name: str, age: int, rank: str]
    score: float
    active: bool
```
Так же для корректного подсчета оценивания была введена защищеная переменная хранящая количества оценок. 

**Что мы должен уметь делать с учителем?**\
Конечно же в первую очередь мы должны уметь его рейтить. Для этого я ввел метод ```rate```. Помимо этого так же хотелось бы уметь узнавать рейтинг учителя. Для этого я ввел метод ```get_rating```:
```python
    def rate(self, x: float) -> None:
        if not isinstance(x, (int, float)) or x > 5 or x < 0:
            raise ValueError('Invalid score, it must be between 0 and 5.')
        if self.active == False:
            raise AttributeError('Teacher must be active in order to rate.')
        self.score = (self.score * self.__number_of_rates + float(x)) / (self.__number_of_rates + 1)
        self.__number_of_rates += 1
    
    def get_rating(self) -> float:
        return self.score
```
Помимо этого необходимо реализовать методы для менеджмента групп:
```python
    def assign_group(self, group: str) -> None:
        if not isinstance(group, str) or len(group.strip()) == 0:
            raise ValueError('Invalid group name.')
        if group in self.groups:
            raise ValueError('This group is already assigned to this teacher.')
        if self.active == False:
            raise AttributeError('Teacher must be active in order to assign.')
        self.groups.add(group)
    
    def unassign_group(self, group: str) -> None:
        if not isinstance(group, str) or len(group.strip()) == 0:
            raise ValueError('Invalid group name.')
        if group not in self.groups:
            raise ValueError('This group is not assigned to this teacher.')
        self.groups.remove(group)
```
И методы менеджемента персональной инфой тоже тогда уже сделаю:
```python
    def update_name(self, new_name: str) -> None:
        if not isinstance(new_name, str) or len(new_name.strip()) == 0:
            raise ValueError("Name must be a non-empty string.")
        self.personal_info[0] = new_name
    
    def update_age(self, new_age: int) -> None:
        if not isinstance(new_age, int) or new_age < 16 or new_age > 100:
            raise ValueError("Age must be an integer between 16 and 100.")
        if new_age < self.personal_info[1]:
            raise ValueError("Age cannot decrease.")
        self.personal_info[1] = new_age
    
    def update_rank(self, new_rank: str) -> None:
        if not isinstance(new_rank, str) or len(new_rank.strip()) == 0:
            raise ValueError("Rank must be a non-empty string.")
        if self.active == False:
            raise AttributeError('Teacher must be active in order to update rank.')
        self.personal_info[2] = new_rank
    
    def get_name(self) -> str:
        return self.personal_info[0]
    
    def get_age(self) -> int:
        return self.personal_info[1]
    
    def get_rank(self) -> str:
        return self.personal_info[2] 
``` 
И да я знаю что по хорошему это должен был быть map, но у меня к сожалению будет лист.


**Состояние** \
Очевидно что у преподавателя бывает только 2 состояния: активный и не активный, следовательно это булевая переменая (как я и сделал), так же сделал интерфейс для взаимодействия с этим параметром.
```python
    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        if len(self.groups) != 0:
            raise AttributeError('Teacher must have no assigned groups in order to deactivate.')
        self.active = False
```
Так же я реализовал необходимые *магические* методы
```python
    def __repr__(self):
        return (f"Teacher(name='{self.personal_info[0]}', age={self.personal_info[1]}, "
                f"rank='{self.personal_info[2]}', subject='{self.subject}', "
                f"score={self.score:.2f}, active={self.active}, "
                f"groups={self.groups})")
    
    def __eq__(self, other):
        if not isinstance(other, Teacher):
            return False
        return (self.personal_info[0] == other.personal_info[0] and 
                self.personal_info[1] == other.personal_info[1] and
                self.subject == other.subject)

    def __hash__(self):
        return hash((self.personal_info[0], self.personal_info[1], self.subject))
```