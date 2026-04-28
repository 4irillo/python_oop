import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Lab01'))

from model import Teacher
from collection import TeacherCollection


def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_success(msg):
    print(f"  + {msg}")


def print_error(msg):
    print(f"  - ERROR: {msg}")


print_section("1. CREATING TEACHERS AND COLLECTION")

col = TeacherCollection()

alice = Teacher("Alice Johnson", 35, "Senior Lecturer", "Mathematics")
bob = Teacher("Bob Smith", 42, "Professor", "Physics")
charlie = Teacher("Charlie Brown", 28, "Teaching Assistant", "Computer Science")
diana = Teacher("Diana Prince", 31, "Lecturer", "Mathematics")
eric = Teacher("Eric Cartman", 45, "Professor", "Chemistry")

col.add(alice)
col.add(bob)
col.add(charlie)
col.add(diana)
col.add(eric)

print_success(f"Added {len(col)} teachers to collection")


print_section("2. ADD/REMOVE VALIDATION")

try:
    col.add(alice)
    print_error("Should have raised ValueError for duplicate!")
except ValueError as e:
    print_success(f"Caught duplicate: {e}")

try:
    col.add("not a teacher")
    print_error("Should have raised ValueError for non-teacher!")
except ValueError as e:
    print_success(f"Caught non-teacher: {e}")

removed = col.remove_at(2)
print_success(f"Removed at index 2: {removed.get_name()}")

col.add(charlie)
print_success(f"Re-added Charlie, count={len(col)}")


print_section("3. RATING TEACHERS")

alice.rate(5.0)
alice.rate(4.5)
alice.rate(4.0)

bob.rate(3.0)
bob.rate(3.5)

charlie.rate(5.0)

diana.rate(4.0)
diana.rate(4.5)

eric.rate(2.0)
eric.rate(2.5)

for t in col:
    print_success(f"{t.get_name()}: {t.get_rating():.2f}")


print_section("4. FIND OPERATIONS")

result = col.find_by_name("Alice Johnson")
print_success(f"find_by_name: found {len(result)} teacher(s)")

result = col.find_by_subject("Mathematics")
print_success(f"find_by_subject Mathematics: {len(result)} teacher(s)")

result = col.find_by_rank("Professor")
print_success(f"find_by_rank Professor: {len(result)} teacher(s)")

try:
    col.find_by_name("Nobody")
    print_error("Should have raised ValueError!")
except ValueError as e:
    print_success(f"Caught missing: {e}")


print_section("5. FILTER OPERATIONS")

active = col.get_active()
print_success(f"Active teachers: {len(active)}")

diana.deactivate()
inactive = col.get_inactive()
print_success(f"Inactive teachers after deactivation: {len(inactive)}")

math_teachers = col.get_by_subject("Mathematics")
print_success(f"Math teachers: {len(math_teachers)}")

top3 = col.get_top_rated(3)
print_success("Top 3 rated:")
for i, t in enumerate(top3, 1):
    print(f"    {i}. {t.get_name()} - {t.get_rating():.2f}")


print_section("6. SORT OPERATIONS")

by_name = col.sort_by_name()
print_success("Sorted by name:")
for t in by_name:
    print(f"    {t.get_name()}")

by_age = col.sort_by_age()
print_success("Sorted by age:")
for t in by_age:
    print(f"    {t.get_name()} - {t.get_age()}")

by_score = col.sort_by_score()
print_success("Sorted by score (desc):")
for t in by_score:
    print(f"    {t.get_name()} - {t.get_rating():.2f}")


print_section("7. INDEX ACCESS")

print_success(f"col[0] = {col[0].get_name()}")
print_success(f"col[1] = {col[1].get_name()}")
print_success(f"col[-1] = {col[-1].get_name()}")

try:
    col[100]
    print_error("Should have raised ValueError!")
except ValueError as e:
    print_success(f"Caught out of range: {e}")


print_section("8. ITERATION")

print_success("Iterating collection:")
for teacher in col:
    print(f"    {teacher.get_name()} ({teacher.subject})")


print_section("9. SLICE ACCESS")

slice_result = col[0:2]
print_success(f"Slice [0:2] length: {len(slice_result)}")


print_section("10. COMPLETE WORKFLOW")

new_col = TeacherCollection()
for name, age, rank, subject in [
    ("Frank Castle", 38, "Lecturer", "History"),
    ("Grace Hopper", 50, "Professor", "Computer Science"),
    ("Hank Pym", 33, "PhD", "Physics"),
]:
    t = Teacher(name, age, rank, subject)
    t.rate(4.0 + (age % 5) * 0.2)
    new_col.add(t)

print_success(f"Created new collection with {len(new_col)} teachers")
print_success("Final state:")
for t in new_col.sort_by_name():
    print(f"    {t}")
