class BaseTeacher:
    def __init__(self, name: str, age: int, rank: str, subject: str):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(age, int) or age < 18 or age > 100:
            raise ValueError("Age must be an integer between 18 and 100.")
        if not isinstance(rank, str) or not rank.strip():
            raise ValueError("Rank must be a non-empty string.")
        if not isinstance(subject, str) or not subject.strip():
            raise ValueError("Subject must be a non-empty string.")

        self._name = name.strip()
        self._age = age
        self._rank = rank.strip()
        self._subject = subject.strip()
        self._active = True

    @property
    def name(self) -> str:
        return self._name

    @property
    def age(self) -> int:
        return self._age

    @property
    def rank(self) -> str:
        return self._rank

    @property
    def subject(self) -> str:
        return self._subject

    @property
    def active(self) -> bool:
        return self._active

    def activate(self) -> None:
        self._active = True

    def deactivate(self) -> None:
        self._active = False

    def get_info(self) -> str:
        return f"{self._name}, {self._age}, {self._rank}, {self._subject}"

    def __repr__(self):
        return f"BaseTeacher(name='{self._name}', age={self._age}, rank='{self._rank}', subject='{self._subject}')"

    def __eq__(self, other):
        if not isinstance(other, BaseTeacher):
            return False
        return self._name == other._name and self._age == other._age and self._subject == other._subject
