import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Lab01'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from model import Teacher
from collection import StrategyCollection
from strategies import (
    by_name, by_age, by_subject, by_score,
    is_active, has_groups,
    make_subject_filter, make_min_score_filter,
    to_summary, to_name,
    ByScoreDescStrategy, ActivateStrategy, DeactivateIfIdleStrategy,
)


def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_success(msg):
    print(f"  + {msg}")


print_section("1. CREATING COLLECTION")

col = StrategyCollection()

alice = Teacher("Alice Johnson", 35, "Senior Lecturer", "Mathematics")
bob = Teacher("Bob Smith", 42, "Professor", "Physics")
charlie = Teacher("Charlie Brown", 28, "Teaching Assistant", "Computer Science")
diana = Teacher("Diana Prince", 31, "Lecturer", "Mathematics")
eric = Teacher("Eric Cartman", 45, "Professor", "Chemistry")
frank = Teacher("Frank Castle", 38, "Lecturer", "Physics")

alice.rate(4.5)
alice.rate(4.8)
bob.rate(3.2)
bob.rate(3.5)
charlie.rate(4.9)
diana.rate(4.0)
eric.rate(2.5)
frank.rate(3.8)
frank.rate(4.0)

diana.deactivate()

alice.assign_group("A1")
alice.assign_group("B2")
bob.assign_group("C3")

for t in [alice, bob, charlie, diana, eric, frank]:
    col.add(t)

print_success(f"Collection created with {len(col)} teachers")


print_section("2. THREE SORTING STRATEGIES")

by_name_sorted = sorted(col.get_all(), key=by_name)
print_success("Sorted by name:")
for t in by_name_sorted:
    print(f"    {t.personal_info[0]}")

by_age_sorted = sorted(col.get_all(), key=by_age)
print_success("Sorted by age:")
for t in by_age_sorted:
    print(f"    {t.personal_info[0]} - {t.personal_info[1]}")

by_score_sorted = sorted(col.get_all(), key=by_score, reverse=True)
print_success("Sorted by score (desc):")
for t in by_score_sorted:
    print(f"    {t.personal_info[0]} - {t.score:.2f}")


print_section("3. FILTER() WITH TWO FILTER FUNCTIONS")

active_teachers = list(filter(is_active, col.get_all()))
print_success(f"filter(is_active): {len(active_teachers)} teachers")
for t in active_teachers:
    print(f"    {t.personal_info[0]}")

assigned_teachers = list(filter(has_groups, col.get_all()))
print_success(f"filter(has_groups): {len(assigned_teachers)} teachers")
for t in assigned_teachers:
    print(f"    {t.personal_info[0]} - groups: {t.groups}")


print_section("4. MAP() TRANSFORMATION")

summaries = list(map(to_summary, col.get_all()))
print_success("map(to_summary):")
for s in summaries:
    print(f"    {s}")

names_named = list(map(to_name, col.get_all()))
names_lambda = list(map(lambda t: t.personal_info[0], col.get_all()))
print_success(f"map(to_name) == map(lambda): {names_named == names_lambda}")


print_section("5. FUNCTION FACTORIES")

math_filter = make_subject_filter("Mathematics")
math_teachers = list(filter(math_filter, col.get_all()))
print_success(f"make_subject_filter('Mathematics'): {len(math_teachers)} found")
for t in math_teachers:
    print(f"    {t.personal_info[0]}")

high_score_filter = make_min_score_filter(4.0)
high_rated = list(filter(high_score_filter, col.get_all()))
print_success(f"make_min_score_filter(4.0): {len(high_rated)} found")
for t in high_rated:
    print(f"    {t.personal_info[0]} - {t.score:.2f}")


print_section("6. SORT_BY() AND FILTER_BY() COLLECTION METHODS")

sorted_col = col.sort_by(by_name)
print_success(f"col.sort_by(by_name): {[t.personal_info[0] for t in sorted_col]}")

active_col = col.filter_by(is_active)
print_success(f"col.filter_by(is_active): {len(active_col)} teachers")

summaries_via_col = col.map_to(to_summary)
print_success(f"col.map_to(to_summary): {len(summaries_via_col)} items")


print_section("SCENARIO 1: FULL CHAIN filter_by -> sort_by -> apply")

activate_all = ActivateStrategy()

result = (col
    .filter_by(is_active)
    .sort_by(by_score)
    .apply(activate_all))

print_success(f"After chain: {len(result)} active teachers, sorted by score:")
for t in result:
    print(f"    {t.personal_info[0]} - {t.score:.2f} - active: {t.active}")


print_section("SCENARIO 2: STRATEGY REPLACEMENT")

print_success("Same collection, different sort strategy — result changes:")

by_subject_result = col.filter_by(is_active).sort_by(by_subject)
print_success("sort_by(by_subject):")
for t in by_subject_result:
    print(f"    {t.personal_info[0]} ({t.subject})")

by_age_result = col.filter_by(is_active).sort_by(by_age)
print_success("sort_by(by_age):")
for t in by_age_result:
    print(f"    {t.personal_info[0]} ({t.personal_info[1]})")

by_score_desc_strategy = ByScoreDescStrategy()
by_desc_result = col.filter_by(is_active).sort_by(by_score_desc_strategy)
print_success("sort_by(ByScoreDescStrategy()):")
for t in by_desc_result:
    print(f"    {t.personal_info[0]} ({t.score:.2f})")


print_section("SCENARIO 3: CALLABLE OBJECT AS STRATEGY")

deactivate_idle = DeactivateIfIdleStrategy()

print_success("Before DeactivateIfIdleStrategy:")
for t in col:
    print(f"    {t.personal_info[0]} - groups: {t.groups} - active: {t.active}")

col.apply(deactivate_idle)

print_success("After DeactivateIfIdleStrategy:")
for t in col:
    print(f"    {t.personal_info[0]} - groups: {t.groups} - active: {t.active}")

col.apply(ActivateStrategy())
print_success("After ActivateStrategy() restores all:")
print_success(f"Active count: {len(col.get_active())}")
