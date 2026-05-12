import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'Lab01'))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from model import Teacher
from container import (
    TypedCollection,
    Displayable, Scorable,
    TDisplayable, TScorable,
    print_displayable, find_top_scorer,
)


def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_success(msg):
    print(f"  + {msg}")


print_section("1. TYPED COLLECTION — ADD / REMOVE / GET_ALL")

col: TypedCollection[Teacher] = TypedCollection()

alice = Teacher("Alice Johnson", 35, "Senior Lecturer", "Mathematics")
bob = Teacher("Bob Smith", 42, "Professor", "Physics")
charlie = Teacher("Charlie Brown", 28, "Teaching Assistant", "Computer Science")
diana = Teacher("Diana Prince", 31, "Lecturer", "Mathematics")
eric = Teacher("Eric Cartman", 45, "Professor", "Chemistry")

alice.rate(4.5)
alice.rate(4.8)
bob.rate(3.2)
bob.rate(3.5)
charlie.rate(4.9)
diana.rate(4.0)
eric.rate(2.5)

for t in [alice, bob, charlie, diana, eric]:
    col.add(t)

print_success(f"TypedCollection[Teacher] created with {len(col)} items")
print_success(f"get_all() returns {len(col.get_all())} items")

col.remove(eric)
print_success(f"After remove(eric): {len(col)} items")
col.add(eric)
print_success(f"After re-add(eric): {len(col)} items")


print_section("2. FIND() AND FILTER()")

found = col.find(lambda t: t.personal_info[0] == "Alice Johnson")
print_success(f"find(name == 'Alice Johnson'): {found.personal_info[0]}")

not_found = col.find(lambda t: t.personal_info[0] == "Nobody")
print_success(f"find(name == 'Nobody'): {not_found}")

high_rated: TypedCollection[Teacher] = col.filter(lambda t: t.score >= 4.0)
print_success(f"filter(score >= 4.0): {len(high_rated)} teachers")
for t in high_rated:
    print(f"    {t.personal_info[0]} — {t.score:.2f}")

math_col: TypedCollection[Teacher] = col.filter(
    lambda t: t.subject == "Mathematics"
)
print_success(f"filter(subject == 'Mathematics'): {len(math_col)} teachers")
for t in math_col:
    print(f"    {t.personal_info[0]}")


print_section("3. MAP() — TYPE TRANSFORMATION")

name_col: TypedCollection[str] = col.map(lambda t: t.personal_info[0])
print_success(f"map(name): TypedCollection[str] with {len(name_col)} items")
for name in name_col:
    print(f"    {name}")

summary_col: TypedCollection[str] = col.map(
    lambda t: f"{t.personal_info[0]} ({t.subject}): {t.score:.2f}"
)
print_success("map(summary):")
for s in summary_col:
    print(f"    {s}")

score_col: TypedCollection[float] = col.map(lambda t: t.score)
print_success(f"map(score): TypedCollection[float] -> {[round(s, 2) for s in score_col]}")


print_section("4. PROTOCOL — DISPLAYABLE (structural typing)")

print_success(f"isinstance(alice, Displayable): {isinstance(alice, Displayable)}")
print_success(f"isinstance(bob, Displayable): {isinstance(bob, Displayable)}")
print_success(f"isinstance('string', Displayable): {isinstance('string', Displayable)}")
print_success(f"isinstance(42, Displayable): {isinstance(42, Displayable)}")

print_success("print_displayable(col) — works through Displayable protocol:")
print_displayable(col)


print_section("5. PROTOCOL — SCORABLE (structural typing)")

print_success(f"isinstance(alice, Scorable): {isinstance(alice, Scorable)}")
print_success(f"isinstance(bob, Scorable): {isinstance(bob, Scorable)}")
print_success(f"isinstance('string', Scorable): {isinstance('string', Scorable)}")

top = find_top_scorer(col)
print_success(f"find_top_scorer(col): {top.personal_info[0]} with {top.score:.2f}")


print_section("6. BOUNDED TYPEVAR — TDisplayable AND TScorable")

display_col: TypedCollection[TDisplayable] = TypedCollection()
score_col2: TypedCollection[TScorable] = TypedCollection()

for t in [alice, bob, charlie]:
    display_col.add(t)
    score_col2.add(t)

print_success(f"TypedCollection[TDisplayable] with {len(display_col)} items")
print_displayable(display_col)

top_scorer = find_top_scorer(score_col2)
print_success(f"find_top_scorer(TypedCollection[TScorable]): {top_scorer.personal_info[0]}")


print_section("7. CHAINED OPERATIONS")

result: TypedCollection[str] = (
    col
    .filter(lambda t: t.score >= 3.5)
    .filter(lambda t: t.active)
    .map(lambda t: f"{t.personal_info[0]}: {t.score:.2f}")
)

print_success(f"filter(score>=3.5).filter(active).map(summary): {len(result)} items")
for item in result:
    print(f"    {item}")
