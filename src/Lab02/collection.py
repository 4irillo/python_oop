class ValidationError(ValueError):
    pass


import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Lab01'))

from model import Teacher

class TeacherCollection:
    def __init__(self):
        self._items = []

    def add(self, teacher: Teacher) -> None:
        if not isinstance(teacher, Teacher):
            raise ValidationError("Item must be a Teacher instance.")
        if teacher in self._items:
            raise ValidationError("This teacher is already in the collection.")
        self._items.append(teacher)

    def remove(self, teacher: Teacher) -> None:
        if teacher not in self._items:
            raise ValidationError("Teacher not found in collection.")
        self._items.remove(teacher)

    def remove_at(self, index: int) -> Teacher:
        if not isinstance(index, int):
            raise ValidationError("Index must be an integer.")
        try:
            return self._items.pop(index)
        except IndexError:
            raise ValidationError(f"Index {index} out of range.")

    def get_all(self) -> list:
        return self._items.copy()

    def get(self, index: int) -> Teacher:
        if not isinstance(index, int):
            raise ValidationError("Index must be an integer.")
        try:
            return self._items[index]
        except IndexError:
            raise ValidationError(f"Index {index} out of range.")

    def find_by_name(self, name: str) -> list:
        name = name.strip()
        if not name:
            raise ValidationError("Name cannot be empty.")
        result = [t for t in self._items if t.personal_info[0].lower() == name.lower()]
        if not result:
            raise ValidationError(f"No teacher with name '{name}' found.")
        return result

    def find_by_subject(self, subject: str) -> list:
        subject = subject.strip()
        if not subject:
            raise ValidationError("Subject cannot be empty.")
        result = [t for t in self._items if t.subject.lower() == subject.lower()]
        if not result:
            raise ValidationError(f"No teacher teaching '{subject}' found.")
        return result

    def find_by_rank(self, rank: str) -> list:
        rank = rank.strip()
        if not rank:
            raise ValidationError("Rank cannot be empty.")
        result = [t for t in self._items if t.personal_info[2].lower() == rank.lower()]
        if not result:
            raise ValidationError(f"No teacher with rank '{rank}' found.")
        return result

    def get_active(self) -> list:
        return [t for t in self._items if t.active]

    def get_inactive(self) -> list:
        return [t for t in self._items if not t.active]

    def get_by_subject(self, subject: str) -> list:
        subject = subject.strip()
        if not subject:
            raise ValidationError("Subject cannot be empty.")
        return [t for t in self._items if t.subject.lower() == subject.lower()]

    def get_top_rated(self, n: int = 3) -> list:
        if not isinstance(n, int) or n <= 0:
            raise ValidationError("n must be a positive integer.")
        sorted_teachers = sorted(self._items, key=lambda t: t.score, reverse=True)
        return sorted_teachers[:n]

    def sort_by_name(self) -> list:
        return sorted(self._items, key=lambda t: t.personal_info[0].lower())

    def sort_by_age(self) -> list:
        return sorted(self._items, key=lambda t: t.personal_info[1])

    def sort_by_score(self) -> list:
        return sorted(self._items, key=lambda t: t.score, reverse=True)

    def sort(self, key=None, reverse=False) -> list:
        if key is None:
            return sorted(self._items, reverse=reverse)
        return sorted(self._items, key=key, reverse=reverse)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            return self._items[index]
        if not isinstance(index, int):
            raise ValidationError("Index must be an integer or slice.")
        try:
            return self._items[index]
        except IndexError:
            raise ValidationError(f"Index {index} out of range.")

    def __repr__(self):
        return f"TeacherCollection(count={len(self._items)}, teachers={self._items})"

    def __contains__(self, teacher):
        return teacher in self._items
