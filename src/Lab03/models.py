from base import BaseTeacher


class Professor(BaseTeacher):
    def __init__(self, name: str, age: int, rank: str, subject: str, research_area: str, publication_count: int):
        super().__init__(name, age, rank, subject)
        self.research_area = research_area
        self.publication_count = publication_count

    def calculate_salary(self) -> float:
        base = 50000.0
        bonus = self.publication_count * 500.0
        return base + bonus

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Research: {self.research_area}, Publications: {self.publication_count}"

    def __repr__(self):
        return f"Professor(name='{self.name}', age={self.age}, rank='{self.rank}', subject='{self.subject}', research_area='{self.research_area}', publications={self.publication_count})"


class Lecturer(BaseTeacher):
    def __init__(self, name: str, age: int, rank: str, subject: str, hours_per_week: int, contract_type: str):
        super().__init__(name, age, rank, subject)
        self.hours_per_week = hours_per_week
        self.contract_type = contract_type

    def calculate_salary(self) -> float:
        rate = 25.0 if self.contract_type == "part-time" else 40.0
        return self.hours_per_week * rate * 52

    def get_info(self) -> str:
        base = super().get_info()
        return f"{base}, Hours: {self.hours_per_week}, Contract: {self.contract_type}"

    def __repr__(self):
        return f"Lecturer(name='{self.name}', age={self.age}, rank='{self.rank}', subject='{self.subject}', hours={self.hours_per_week}, contract='{self.contract_type}')"


class MixedCollection:
    def __init__(self):
        self._items = []

    def add(self, item: BaseTeacher) -> None:
        if not isinstance(item, BaseTeacher):
            raise ValueError("Item must be a BaseTeacher instance.")
        self._items.append(item)

    def get_all(self) -> list:
        return self._items.copy()

    def get_only_professors(self) -> list:
        return [x for x in self._items if isinstance(x, Professor)]

    def get_only_lecturers(self) -> list:
        return [x for x in self._items if isinstance(x, Lecturer)]

    def get_only_base(self) -> list:
        return [x for x in self._items if type(x) is BaseTeacher]

    def process_all(self) -> list:
        results = []
        for item in self._items:
            if hasattr(item, "calculate_salary"):
                results.append((item.name, item.calculate_salary()))
            else:
                results.append((item.name, 0.0))
        return results

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"MixedCollection(count={len(self._items)})"
