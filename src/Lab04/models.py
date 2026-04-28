from interfaces import Printable, Comparable


class Student(Printable, Comparable):
    def __init__(self, name: str, age: int, gpa: float):
        self.name = name
        self.age = age
        self.gpa = gpa

    def to_string(self) -> str:
        return f"Student: {self.name}, Age: {self.age}, GPA: {self.gpa}"

    def compare_to(self, other) -> int:
        if not isinstance(other, Student):
            raise ValueError("Can only compare with Student.")
        if self.gpa > other.gpa:
            return 1
        if self.gpa < other.gpa:
            return -1
        return 0

    def __repr__(self):
        return f"Student(name='{self.name}', age={self.age}, gpa={self.gpa})"


class Course(Printable, Comparable):
    def __init__(self, title: str, credits: int, difficulty: int):
        self.title = title
        self.credits = credits
        self.difficulty = difficulty

    def to_string(self) -> str:
        return f"Course: {self.title}, Credits: {self.credits}, Difficulty: {self.difficulty}"

    def compare_to(self, other) -> int:
        if not isinstance(other, Course):
            raise ValueError("Can only compare with Course.")
        if self.difficulty > other.difficulty:
            return 1
        if self.difficulty < other.difficulty:
            return -1
        return 0

    def __repr__(self):
        return f"Course(title='{self.title}', credits={self.credits}, difficulty={self.difficulty})"


class ItemCollection:
    def __init__(self):
        self._items = []

    def add(self, item) -> None:
        self._items.append(item)

    def get_all(self) -> list:
        return self._items.copy()

    def get_printable(self) -> list:
        return [x for x in self._items if isinstance(x, Printable)]

    def get_comparable(self) -> list:
        return [x for x in self._items if isinstance(x, Comparable)]

    def print_all(self) -> None:
        for item in self._items:
            if isinstance(item, Printable):
                print(item.to_string())
            else:
                print(f"Not printable: {item}")

    def sort_by_comparison(self) -> list:
        comparable = self.get_comparable()
        if not comparable:
            return []
        return sorted(comparable, key=lambda x: getattr(x, 'gpa', getattr(x, 'difficulty', 0)), reverse=True)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"ItemCollection(count={len(self._items)})"
