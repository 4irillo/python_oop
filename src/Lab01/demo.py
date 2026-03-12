"""
Teacher Class Demo
==================
This script demonstrates all capabilities of the Teacher class
alongside intentional errors that trigger the validation system.
"""

from model import Teacher

def print_section(title):
    """Helper to print formatted section headers."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def print_success(msg):
    """Helper for success messages."""
    print(f"  ✓ {msg}")

def print_error(msg):
    """Helper for error messages."""
    print(f"  ✗ ERROR: {msg}")

# =============================================================================
# SECTION 1: VALID TEACHER CREATION
# =============================================================================
print_section("1. CREATING VALID TEACHERS")

try:
    # Create a valid teacher
    alice = Teacher("Alice Johnson", 35, "Senior Lecturer", "Mathematics")
    print_success(f"Created: {alice.get_name()}, {alice.get_age()} years old")
    print(f"    Details: {alice}")
except Exception as e:
    print_error(f"Unexpected error: {e}")

try:
    # Another valid teacher
    bob = Teacher("Bob Smith", 42, "Professor", "Physics")
    print_success(f"Created: {bob.get_name()}, teaching {bob.subject}")
except Exception as e:
    print_error(f"Unexpected error: {e}")

# =============================================================================
# SECTION 2: INVALID TEACHER CREATION (Error Prevention)
# =============================================================================
print_section("2. INVALID CREATION ATTEMPTS (Should Fail)")

# Empty name
try:
    invalid = Teacher("", 30, "Teacher", "Chemistry")
    print_error("Should have raised ValueError for empty name!")
except ValueError as e:
    print_success(f"Caught empty name: {e}")

# Invalid age (too young)
try:
    invalid = Teacher("Young Teacher", 17, "Assistant", "Biology")
    print_error("Should have raised ValueError for age < 18!")
except ValueError as e:
    print_success(f"Caught underage: {e}")

# Invalid age (too old)
try:
    invalid = Teacher("Old Teacher", 101, "Emeritus", "History")
    print_error("Should have raised ValueError for age > 100!")
except ValueError as e:
    print_success(f"Caught overage: {e}")

# Non-integer age
try:
    invalid = Teacher("Bad Age", "thirty", "Teacher", "English")
    print_error("Should have raised ValueError for non-int age!")
except ValueError as e:
    print_success(f"Caught non-integer age: {e}")

# Empty rank
try:
    invalid = Teacher("No Rank", 45, "   ", "Art")
    print_error("Should have raised ValueError for empty rank!")
except ValueError as e:
    print_success(f"Caught empty rank: {e}")

# Empty subject
try:
    invalid = Teacher("No Subject", 38, "Instructor", "")
    print_error("Should have raised ValueError for empty subject!")
except ValueError as e:
    print_success(f"Caught empty subject: {e}")

# =============================================================================
# SECTION 3: RATING SYSTEM
# =============================================================================
print_section("3. RATING SYSTEM")

print("  Adding ratings for Alice (Mathematics)...")
alice.rate(4.5)
print_success(f"Rated 4.5 → Current score: {alice.get_rating():.2f}")
alice.rate(5.0)
print_success(f"Rated 5.0 → Current score: {alice.get_rating():.2f}")
alice.rate(3.5)
print_success(f"Rated 3.5 → Current score: {alice.get_rating():.2f}")
print(f"    Final average: {alice.get_rating():.2f}/5.0")

# Invalid ratings
print("\n  Attempting invalid ratings...")

# Rating too high
try:
    alice.rate(5.5)
    print_error("Should have raised ValueError for score > 5!")
except ValueError as e:
    print_success(f"Caught high score: {e}")

# Rating too low (negative)
try:
    alice.rate(-1)
    print_error("Should have raised ValueError for negative score!")
except ValueError as e:
    print_success(f"Caught negative score: {e}")

# Non-numeric rating
try:
    alice.rate("excellent")
    print_error("Should have raised ValueError for non-numeric score!")
except ValueError as e:
    print_success(f"Caught non-numeric: {e}")

# =============================================================================
# SECTION 4: GROUP MANAGEMENT
# =============================================================================
print_section("4. GROUP MANAGEMENT")

print("  Assigning groups to Alice...")
alice.assign_group("Group A")
print_success(f"Assigned 'Group A' → Groups: {alice.groups}")
alice.assign_group("Group B")
print_success(f"Assigned 'Group B' → Groups: {alice.groups}")
alice.assign_group("Advanced Calculus")
print_success(f"Assigned 'Advanced Calculus' → Groups: {alice.groups}")

# Invalid group assignments
print("\n  Attempting invalid group operations...")

# Duplicate group
try:
    alice.assign_group("Group A")
    print_error("Should have raised ValueError for duplicate group!")
except ValueError as e:
    print_success(f"Caught duplicate: {e}")

# Empty group name
try:
    alice.assign_group("   ")
    print_error("Should have raised ValueError for empty group!")
except ValueError as e:
    print_success(f"Caught empty group: {e}")

# Unassign non-existent group
try:
    alice.unassign_group("NonExistent")
    print_error("Should have raised ValueError for non-existent group!")
except ValueError as e:
    print_success(f"Caught unassign missing: {e}")

# Valid unassign
print("\n  Unassigning 'Group B'...")
alice.unassign_group("Group B")
print_success(f"Unassigned 'Group B' → Groups: {alice.groups}")

# =============================================================================
# SECTION 5: ACTIVE STATE MANAGEMENT
# =============================================================================
print_section("5. ACTIVE STATE MANAGEMENT")

print(f"  Alice active status: {alice.active}")

# Try to deactivate with groups assigned
print("\n  Attempting to deactivate Alice with active groups...")
try:
    alice.deactivate()
    print_error("Should have raised AttributeError with groups assigned!")
except AttributeError as e:
    print_success(f"Caught deactivate with groups: {e}")

# Unassign all groups first
print("\n  Unassigning remaining groups...")
alice.unassign_group("Group A")
alice.unassign_group("Advanced Calculus")
print_success(f"All groups removed → Groups: {alice.groups}")

# Now deactivate
print("\n  Deactivating Alice...")
alice.deactivate()
print_success(f"Deactivated → Active: {alice.active}")

# Try operations on inactive teacher
print("\n  Attempting operations on inactive teacher...")

try:
    alice.rate(4.0)
    print_error("Should have raised AttributeError for rating inactive teacher!")
except AttributeError as e:
    print_success(f"Caught rating inactive: {e}")

try:
    alice.assign_group("New Group")
    print_error("Should have raised AttributeError for assigning to inactive!")
except AttributeError as e:
    print_success(f"Caught assign inactive: {e}")

try:
    alice.update_rank("Dean")
    print_error("Should have raised AttributeError for updating inactive!")
except AttributeError as e:
    print_success(f"Caught rank update inactive: {e}")

# Reactivate
print("\n  Reactivating Alice...")
alice.activate()
print_success(f"Reactivated → Active: {alice.active}")

# =============================================================================
# SECTION 6: PERSONAL INFO MANAGEMENT
# =============================================================================
print_section("6. PERSONAL INFO MANAGEMENT")

print(f"  Current info: Name='{alice.get_name()}', Age={alice.get_age()}, Rank='{alice.get_rank()}'")

# Update name
print("\n  Updating name...")
alice.update_name("Dr. Alice Johnson")
print_success(f"Name updated → '{alice.get_name()}'")

# Invalid name updates
try:
    alice.update_name("")
    print_error("Should have raised ValueError for empty name!")
except ValueError as e:
    print_success(f"Caught empty name update: {e}")

# Update age (valid - increasing)
print("\n  Updating age (36)...")
alice.update_age(36)
print_success(f"Age updated → {alice.get_age()}")

# Invalid age updates
try:
    alice.update_age(35)  # Decreasing
    print_error("Should have raised ValueError for decreasing age!")
except ValueError as e:
    print_success(f"Caught age decrease: {e}")

try:
    alice.update_age(15)  # Too young
    print_error("Should have raised ValueError for age < 16!")
except ValueError as e:
    print_success(f"Caught underage update: {e}")

try:
    alice.update_age(101)  # Too old
    print_error("Should have raised ValueError for age > 100!")
except ValueError as e:
    print_success(f"Caught overage update: {e}")

# Update rank
print("\n  Updating rank...")
alice.update_rank("Department Head")
print_success(f"Rank updated → '{alice.get_rank()}'")

# Invalid rank
try:
    alice.update_rank("   ")
    print_error("Should have raised ValueError for empty rank!")
except ValueError as e:
    print_success(f"Caught empty rank update: {e}")

# =============================================================================
# SECTION 7: MAGIC METHODS
# =============================================================================
print_section("7. MAGIC METHODS (Representation & Equality)")

# __repr__
print(f"  __repr__ output:")
print(f"    {repr(alice)}")

# Create another Alice with same key attributes
print("\n  Testing equality...")
alice_clone = Teacher("Alice Johnson", 35, "Senior Lecturer", "Mathematics")  # Same as original Alice
alice_clone.update_name("Dr. Alice Johnson")  # Match current alice name
alice_clone.update_age(36)  # Match current alice age

print(f"  Alice: name='{alice.get_name()}', age={alice.get_age()}, subject='{alice.subject}'")
print(f"  Clone: name='{alice_clone.get_name()}', age={alice_clone.get_age()}, subject='{alice_clone.subject}'")

if alice == alice_clone:
    print_success("Equality check passed (same name, age, subject)")
else:
    print_error("Equality check failed unexpectedly")

# Different teacher
if alice != bob:
    print_success("Inequality check passed (different teachers)")
else:
    print_error("Inequality check failed unexpectedly")

# Compare with non-Teacher
if alice != "Not a teacher":
    print_success("Type safety check passed (not equal to string)")
else:
    print_error("Type safety check failed")

# =============================================================================
# SECTION 8: COMPLETE WORKFLOW DEMO
# =============================================================================
print_section("8. COMPLETE WORKFLOW DEMO")

print("  Creating a new teacher and running full lifecycle...")

# Create
charlie = Teacher("Charlie Brown", 28, "Teaching Assistant", "Computer Science")
print_success(f"Created: {charlie.get_name()}")

# Assign groups
charlie.assign_group("CS101")
charlie.assign_group("CS202")
print_success(f"Assigned groups: {charlie.groups}")

# Get rated
charlie.rate(4.0)
charlie.rate(4.5)
charlie.rate(5.0)
print_success(f"Received ratings: {charlie.get_rating():.2f}/5.0")

# Get promoted
charlie.update_rank("Lecturer")
print_success(f"Promoted to: {charlie.get_rank()}")

# Birthday
charlie.update_age(29)
print_success(f"Happy birthday! Now {charlie.get_age()}")

# End of semester - remove groups
charlie.unassign_group("CS101")
charlie.unassign_group("CS202")
print_success("Semester ended, groups cleared")

# Take sabbatical
charlie.deactivate()
print_success(f"On sabbatical: active={charlie.active}")

# Return from sabbatical
charlie.activate()
charlie.update_rank("Senior Lecturer")
charlie.assign_group("CS303")
print_success(f"Returned! New rank: {charlie.get_rank()}, teaching: {charlie.groups}")

print(f"\n  Final state: {repr(charlie)}")

# =============================================================================
# SUMMARY
# =============================================================================
print_section("DEMO COMPLETED SUCCESSFULLY")
print("  All class capabilities demonstrated:")
print("    • Teacher creation with validation")
print("    • Rating system with bounds checking")
print("    • Group assignment/unassignment")
print("    • Active/inactive state management")
print("    • Personal info updates with validation")
print("    • Object representation and equality")
print("\n  All error prevention systems verified:")
print("    • Type checking (strings, integers)")
print("    • Range validation (ages, scores)")
print("    • Empty/whitespace string prevention")
print("    • State-dependent operation restrictions")
print("    • Duplicate prevention")
print("    • Business logic enforcement (no age decrease, etc.)")