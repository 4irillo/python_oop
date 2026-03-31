"""
Teacher class implementation for Lab01.

This module implements a Teacher class with encapsulation, properties,
business methods, and magic methods for object representation and comparison.

All input validation is delegated to the validation module.
"""

from validation import (
    validate_teacher_name,
    validate_teacher_age,
    validate_teacher_age_update,
    validate_teacher_rank,
    validate_teacher_subject,
    validate_rating_score,
    validate_group_name,
    validate_teacher_active,
    validate_teacher_can_deactivate,
    validate_group_not_assigned,
    validate_group_is_assigned,
    ValidationError,
    StateError
)


class Teacher:
    # Public vars
    subject: str
    groups: set
    personal_info: list  # [name: str, age: int, rank: str]
    score: float
    active: bool
    
    # Private vars
    __number_of_rates: int
    
    def __init__(self, name: str, age: int, rank: str, subject: str):
        # Validate all inputs using validation module
        validate_teacher_name(name)
        validate_teacher_age(age)
        validate_teacher_rank(rank)
        validate_teacher_subject(subject)

        self.personal_info = [name, age, rank]
        self.subject = subject
        self.groups = set()
        self.score = 0.0
        self.active = True
        self.__number_of_rates = 0
    
    # ========== RATING SYSTEM ==========
    def rate(self, x: float) -> None:
        validate_rating_score(x)
        validate_teacher_active(self.active, "rate")
        
        self.score = (self.score * self.__number_of_rates + float(x)) / (self.__number_of_rates + 1)
        self.__number_of_rates += 1
    
    def get_rating(self) -> float:
        return self.score
    
    # ========== GROUP MANAGEMENT ==========
    def assign_group(self, group: str) -> None:
        validate_group_name(group)
        validate_group_not_assigned(group, self.groups)
        validate_teacher_active(self.active, "assign groups")
        
        self.groups.add(group)
    
    def unassign_group(self, group: str) -> None:
        validate_group_name(group)
        validate_group_is_assigned(group, self.groups)
        
        self.groups.remove(group)
    
    # ========== ACTIVE STATE MANAGEMENT ==========
    def activate(self) -> None:
        self.active = True
    
    def deactivate(self) -> None:
        validate_teacher_can_deactivate(self.groups)
        self.active = False
    
    # ========== PERSONAL INFO MANAGEMENT ==========
    def update_name(self, new_name: str) -> None:
        validate_teacher_name(new_name)
        self.personal_info[0] = new_name
    
    def update_age(self, new_age: int) -> None:
        validate_teacher_age_update(new_age, self.personal_info[1])
        self.personal_info[1] = new_age
    
    def update_rank(self, new_rank: str) -> None:
        validate_teacher_rank(new_rank)
        validate_teacher_active(self.active, "update rank")
        self.personal_info[2] = new_rank
    
    def get_name(self) -> str:
        return self.personal_info[0]
    
    def get_age(self) -> int:
        return self.personal_info[1]
    
    def get_rank(self) -> str:
        return self.personal_info[2]
    
    # ========== MAGIC METHODS (Object Equality & Representation) ==========
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
