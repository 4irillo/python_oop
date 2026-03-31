
class ValidationError(ValueError):
    pass


class StateError(AttributeError):

    pass


# ========== STRING VALIDATION ==========

def validate_non_empty_string(value: str, field_name: str) -> None:
    if not isinstance(value, str):
        raise ValidationError(f"{field_name} must be a string, got {type(value).__name__}.")
    if len(value.strip()) == 0:
        raise ValidationError(f"{field_name} cannot be empty or whitespace only.")


def validate_string_length(value: str, field_name: str, min_length: int = 1, max_length: int = None) -> None:
    validate_non_empty_string(value, field_name)
    
    stripped = value.strip()
    if len(stripped) < min_length:
        raise ValidationError(f"{field_name} must be at least {min_length} characters long.")
    if max_length is not None and len(stripped) > max_length:
        raise ValidationError(f"{field_name} must not exceed {max_length} characters.")


# ========== NUMERIC VALIDATION ==========

def validate_integer(value, field_name: str, min_value: int = None, max_value: int = None) -> None:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValidationError(f"{field_name} must be an integer, got {type(value).__name__}.")
    
    if min_value is not None and value < min_value:
        raise ValidationError(f"{field_name} must be at least {min_value}.")
    if max_value is not None and value > max_value:
        raise ValidationError(f"{field_name} must not exceed {max_value}.")


def validate_positive_number(value, field_name: str) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValidationError(f"{field_name} must be a number, got {type(value).__name__}.")
    if value <= 0:
        raise ValidationError(f"{field_name} must be positive.")


def validate_number_in_range(value, field_name: str, min_value: float, max_value: float) -> None:
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        raise ValidationError(f"{field_name} must be a number, got {type(value).__name__}.")
    if value < min_value or value > max_value:
        raise ValidationError(f"{field_name} must be between {min_value} and {max_value}.")


# ========== TEACHER-SPECIFIC VALIDATION ==========

def validate_teacher_name(name: str) -> None:
    validate_non_empty_string(name, "Name")


def validate_teacher_age(age: int, min_age: int = 18, max_age: int = 100) -> None:
    validate_integer(age, "Age", min_age, max_age)


def validate_teacher_age_update(new_age: int, current_age: int) -> None:
    validate_teacher_age(new_age, min_age=16, max_age=100)
    if new_age < current_age:
        raise ValidationError("Age cannot decrease.")


def validate_teacher_rank(rank: str) -> None:
    validate_non_empty_string(rank, "Rank")


def validate_teacher_subject(subject: str) -> None:
    validate_non_empty_string(subject, "Subject")


def validate_rating_score(score) -> None:
    validate_number_in_range(score, "Score", 0, 5)


def validate_group_name(group: str) -> None:
    validate_non_empty_string(group, "Group name")


# ========== STATE VALIDATION ==========

def validate_teacher_active(is_active: bool, operation: str) -> None:
    if not is_active:
        raise StateError(f"Teacher must be active in order to {operation}.")


def validate_teacher_can_deactivate(groups: set) -> None:
    if len(groups) != 0:
        raise StateError("Teacher must have no assigned groups in order to deactivate.")


def validate_group_not_assigned(group: str, groups: set) -> None:
    if group in groups:
        raise ValidationError("This group is already assigned to this teacher.")


def validate_group_is_assigned(group: str, groups: set) -> None:
    if group not in groups:
        raise ValidationError("This group is not assigned to this teacher.")
