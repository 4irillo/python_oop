"""
Lab01 package - Teacher class implementation with validation.

This package contains:
- model.py: Teacher class implementation
- validation.py: Input validation functions
- demo.py: Demonstration of Teacher class functionality
- validate.py: Test suite for Teacher class
"""

from .model import Teacher
from .validation import (
    ValidationError,
    StateError,
    validate_teacher_name,
    validate_teacher_age,
    validate_teacher_rank,
    validate_teacher_subject,
    validate_rating_score,
    validate_group_name,
)

__all__ = [
    'Teacher',
    'ValidationError',
    'StateError',
    'validate_teacher_name',
    'validate_teacher_age',
    'validate_teacher_rank',
    'validate_teacher_subject',
    'validate_rating_score',
    'validate_group_name',
]