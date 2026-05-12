def by_name(teacher):
    """Sort key: alphabetically by teacher name."""
    return teacher.personal_info[0].lower()


def by_age(teacher):
    """Sort key: by teacher age ascending."""
    return teacher.personal_info[1]


def by_subject(teacher):
    """Sort key: alphabetically by subject."""
    return teacher.subject.lower()


def by_score(teacher):
    """Sort key: by rating score (use reverse=True for descending)."""
    return teacher.score


def is_active(teacher):
    """Filter predicate: only active teachers."""
    return teacher.active


def has_groups(teacher):
    """Filter predicate: teachers assigned to at least one group."""
    return len(teacher.groups) > 0


def make_subject_filter(subject: str):
    """Factory: returns a predicate that matches teachers of the given subject."""
    def _predicate(teacher):
        return teacher.subject.lower() == subject.lower()
    return _predicate


def make_min_score_filter(min_score: float):
    """Factory: returns a predicate that matches teachers with score >= min_score."""
    def _predicate(teacher):
        return teacher.score >= min_score
    return _predicate


def to_summary(teacher) -> str:
    """Map transform: teacher to a human-readable summary string."""
    return f"{teacher.personal_info[0]} ({teacher.subject}): {teacher.score:.2f}"


def to_name(teacher) -> str:
    """Map transform: extracts teacher name."""
    return teacher.personal_info[0]


class ByScoreDescStrategy:
    """Callable strategy: sort key that orders teachers by score descending."""

    def __call__(self, teacher):
        return -teacher.score


class ActivateStrategy:
    """Callable strategy: activates a teacher."""

    def __call__(self, teacher):
        teacher.activate()


class DeactivateIfIdleStrategy:
    """Callable strategy: deactivates teachers that have no assigned groups."""

    def __call__(self, teacher):
        if not teacher.groups:
            teacher.deactivate()
