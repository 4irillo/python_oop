from interfaces import Printable, Comparable
from models import Student, Course, ItemCollection


def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_success(msg):
    print(f"  + {msg}")


print_section("1. CREATING OBJECTS")

s1 = Student("Alice", 20, 3.8)
s2 = Student("Bob", 21, 3.5)
s3 = Student("Charlie", 19, 4.0)

c1 = Course("Calculus", 5, 8)
c2 = Course("History", 3, 4)
c3 = Course("Physics", 6, 10)

print_success(f"Created {s1.name}")
print_success(f"Created {c1.title}")


print_section("2. PRINTABLE INTERFACE")

print_success(s1.to_string())
print_success(s2.to_string())
print_success(c1.to_string())
print_success(c2.to_string())


print_section("3. COMPARABLE INTERFACE")

print_success(f"s1.compare_to(s2): {s1.compare_to(s2)}")
print_success(f"s2.compare_to(s1): {s2.compare_to(s1)}")
print_success(f"s1.compare_to(s1): {s1.compare_to(s1)}")

print_success(f"c1.compare_to(c3): {c1.compare_to(c3)}")
print_success(f"c3.compare_to(c1): {c3.compare_to(c1)}")


print_section("4. ISINSTANCE CHECKS")

print_success(f"isinstance(s1, Printable): {isinstance(s1, Printable)}")
print_success(f"isinstance(s1, Comparable): {isinstance(s1, Comparable)}")
print_success(f"isinstance(c1, Printable): {isinstance(c1, Printable)}")
print_success(f"isinstance(c1, Comparable): {isinstance(c1, Comparable)}")


print_section("5. ITEM COLLECTION")

col = ItemCollection()
col.add(s1)
col.add(s2)
col.add(s3)
col.add(c1)
col.add(c2)
col.add(c3)

print_success(f"Total items: {len(col)}")
print_success(f"Printable items: {len(col.get_printable())}")
print_success(f"Comparable items: {len(col.get_comparable())}")


print_section("6. PRINT ALL")

col.print_all()


print_section("7. SORT BY COMPARISON")

sorted_items = col.sort_by_comparison()
for item in sorted_items:
    print_success(repr(item))


print_section("8. WORKING WITH INTERFACE")

def print_all(items: list):
    for item in items:
        if isinstance(item, Printable):
            print_success(item.to_string())

def find_max(items: list):
    if not items:
        return None
    max_item = items[0]
    for item in items[1:]:
        if isinstance(item, Comparable) and isinstance(max_item, Comparable):
            if item.compare_to(max_item) > 0:
                max_item = item
    return max_item

print_all(col.get_all())

max_student = find_max([s1, s2, s3])
print_success(f"Max student: {max_student}")

max_course = find_max([c1, c2, c3])
print_success(f"Max course: {max_course}")
