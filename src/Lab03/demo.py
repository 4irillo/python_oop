from base import BaseTeacher
from models import Professor, Lecturer, MixedCollection


def print_section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


def print_success(msg):
    print(f"  + {msg}")


print_section("1. CREATING OBJECTS")

p1 = Professor("Alice", 45, "Professor", "Physics", "Quantum Mechanics", 12)
p2 = Professor("Bob", 50, "Senior Professor", "Mathematics", "Topology", 8)
l1 = Lecturer("Charlie", 30, "Lecturer", "CS", 20, "part-time")
l2 = Lecturer("Diana", 35, "Senior Lecturer", "Biology", 40, "full-time")
t1 = BaseTeacher("Eve", 40, "Instructor", "Chemistry")

print_success(f"Professor: {p1.name}")
print_success(f"Lecturer: {l1.name}")
print_success(f"BaseTeacher: {t1.name}")


print_section("2. CUSTOM FIELDS")

print_success(f"Alice research_area: {p1.research_area}")
print_success(f"Alice publications: {p1.publication_count}")
print_success(f"Charlie hours: {l1.hours_per_week}")
print_success(f"Charlie contract: {l1.contract_type}")


print_section("3. CALCULATE SALARY")

print_success(f"Alice salary: {p1.calculate_salary()}")
print_success(f"Bob salary: {p2.calculate_salary()}")
print_success(f"Charlie salary: {l1.calculate_salary()}")
print_success(f"Diana salary: {l2.calculate_salary()}")


print_section("4. GET INFO")

print_success(p1.get_info())
print_success(l1.get_info())
print_success(t1.get_info())


print_section("5. ISINSTANCE CHECKS")

print_success(f"isinstance(p1, BaseTeacher): {isinstance(p1, BaseTeacher)}")
print_success(f"isinstance(l1, BaseTeacher): {isinstance(l1, BaseTeacher)}")
print_success(f"isinstance(t1, Professor): {isinstance(t1, Professor)}")
print_success(f"isinstance(t1, Lecturer): {isinstance(t1, Lecturer)}")
print_success(f"type(t1) is BaseTeacher: {type(t1) is BaseTeacher}")


print_section("6. MIXED COLLECTION")

col = MixedCollection()
col.add(p1)
col.add(p2)
col.add(l1)
col.add(l2)
col.add(t1)

print_success(f"Total items: {len(col)}")
print_success(f"Professors: {len(col.get_only_professors())}")
print_success(f"Lecturers: {len(col.get_only_lecturers())}")
print_success(f"BaseTeachers: {len(col.get_only_base())}")


print_section("7. POLYMORPHISM")

results = col.process_all()
for name, salary in results:
    print_success(f"{name}: {salary}")


print_section("8. REPR")

print_success(repr(p1))
print_success(repr(l1))
print_success(repr(t1))
