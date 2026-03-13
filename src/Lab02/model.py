from Lab01. model import Teacher as Teacher

class TeacherManagement:
    _collection: set 

    def __init__(self):
        self._collection = set()

    def update(self, teacher: Teacher) -> None:
        if teacher in self._collection:
            raise ValueError("This teacher is already present in this set.")
        if not isinstance(teacher, Teacher):
            raise ValueError("This is NOT a teacher.")
        self._collection.add(teacher)
    def remove(self, teacher: Teacher) -> None:
        if teacher in self._collection:
            self._collection.remove(teacher)
        else:
            raise ValueError("No such teacher present in this set.")
    def get_all(self) -> set:
        return self._collection

    def find_by_name(self, s: str) -> list:
        ans = []
        for teacher in self._collection:
            if teacher.personal_info[0].lower() == s.lower():
                ans.append(teacher)
        if (len(ans) != 0):
            return ans
        raise ValueError('No such teacher present in this set.')

    def __repr__(self):
        return f"TeacherManagement(teachers={self._collection})"

    def __len__(self):
        return len(self._collection)
    
    def __iter__(self):
        return iter(self._collection)

