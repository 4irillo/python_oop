from model import Teacher

class TeacherValidator:
    """Validator for Teacher class - tests all invariants and edge cases."""
    
    def __init__(self):
        self.passed = 0
        self.failed = 0
    
    def assert_raises(self, func, exception_type, description):
        """Helper to check if function raises expected exception."""
        try:
            func()
            print(f"  ❌ FAIL: {description} - Expected {exception_type.__name__} but no exception raised")
            self.failed += 1
            return False
        except exception_type:
            print(f"  ✅ PASS: {description}")
            self.passed += 1
            return True
        except Exception as e:
            print(f"  ❌ FAIL: {description} - Expected {exception_type.__name__} but got {type(e).__name__}: {e}")
            self.failed += 1
            return False
    
    def assert_equals(self, actual, expected, description):
        """Helper to check equality."""
        if actual == expected:
            print(f"  ✅ PASS: {description}")
            self.passed += 1
            return True
        else:
            print(f"  ❌ FAIL: {description} - Expected {expected}, got {actual}")
            self.failed += 1
            return False
    
    def run_all_tests(self):
        """Run all validation tests."""
        print("=" * 60)
        print("TEACHER CLASS VALIDATION")
        print("=" * 60)
        
        self.test_constructor_invariants()
        self.test_rating_system()
        self.test_group_management()
        self.test_active_state_management()
        self.test_personal_info_management()
        self.test_object_equality()
        
        print("\n" + "=" * 60)
        print(f"RESULTS: {self.passed} passed, {self.failed} failed")
        print("=" * 60)
        return self.failed == 0
    
    # ========== CONSTRUCTOR TESTS ==========
    def test_constructor_invariants(self):
        print("\n📋 Testing Constructor Invariants...")
        
        # Valid creation
        try:
            t = Teacher("John Doe", 35, "Professor", "Mathematics")
            print(f"  ✅ PASS: Valid teacher creation - {t.get_name()}")
            self.passed += 1
        except Exception as e:
            print(f"  ❌ FAIL: Valid teacher creation failed: {e}")
            self.failed += 1
        
        # Invalid name
        self.assert_raises(
            lambda: Teacher("", 35, "Professor", "Math"),
            ValueError, "Empty name raises ValueError"
        )
        self.assert_raises(
            lambda: Teacher(123, 35, "Professor", "Math"),
            ValueError, "Non-string name raises ValueError"
        )
        
        # Invalid age
        self.assert_raises(
            lambda: Teacher("John", 17, "Professor", "Math"),
            ValueError, "Age < 18 raises ValueError"
        )
        self.assert_raises(
            lambda: Teacher("John", 101, "Professor", "Math"),
            ValueError, "Age > 100 raises ValueError"
        )
        self.assert_raises(
            lambda: Teacher("John", "35", "Professor", "Math"),
            ValueError, "Non-int age raises ValueError"
        )
        
        # Invalid rank
        self.assert_raises(
            lambda: Teacher("John", 35, "", "Math"),
            ValueError, "Empty rank raises ValueError"
        )
        
        # Invalid subject
        self.assert_raises(
            lambda: Teacher("John", 35, "Professor", ""),
            ValueError, "Empty subject raises ValueError"
        )
    
    # ========== RATING SYSTEM TESTS ==========
    def test_rating_system(self):
        print("\n⭐ Testing Rating System...")
        
        t = Teacher("Jane Smith", 40, "PhD", "Physics")
        
        # Valid ratings
        t.rate(5.0)
        self.assert_equals(t.get_rating(), 5.0, "First rating of 5.0 gives score 5.0")
        
        t.rate(3.0)
        self.assert_equals(t.get_rating(), 4.0, "Average of 5.0 and 3.0 is 4.0")
        
        t.rate(4.0)
        expected = (5.0 + 3.0 + 4.0) / 3  # = 4.0
        self.assert_equals(t.get_rating(), expected, "Average of three ratings is correct")
        
        # Invalid ratings
        self.assert_raises(lambda: t.rate(5.1), ValueError, "Rating > 5 raises ValueError")
        self.assert_raises(lambda: t.rate(-0.1), ValueError, "Rating < 0 raises ValueError")
        self.assert_raises(lambda: t.rate("5"), ValueError, "String rating raises ValueError")
        
        # Rating inactive teacher
        t.deactivate()
        self.assert_raises(lambda: t.rate(4.0), AttributeError, "Rating inactive teacher raises AttributeError")
    
    # ========== GROUP MANAGEMENT TESTS ==========
    def test_group_management(self):
        print("\n👥 Testing Group Management...")
        
        t = Teacher("Bob Wilson", 45, "Associate Prof", "Chemistry")
        
        # Assign groups
        t.assign_group("Group A")
        self.assert_equals("Group A" in t.groups, True, "Group A assigned successfully")
        
        t.assign_group("Group B")
        self.assert_equals(len(t.groups), 2, "Two groups assigned")
        
        # Duplicate group
        self.assert_raises(
            lambda: t.assign_group("Group A"),
            ValueError, "Duplicate group assignment raises ValueError"
        )
        
        # Invalid group name
        self.assert_raises(
            lambda: t.assign_group(""),
            ValueError, "Empty group name raises ValueError"
        )
        
        # Assign to inactive teacher
        t2 = Teacher("Inactive", 30, "Lecturer", "Bio")
        t2.deactivate()
        self.assert_raises(
            lambda: t2.assign_group("Group X"),
            AttributeError, "Assigning to inactive teacher raises AttributeError"
        )
        
        # Unassign groups
        t.unassign_group("Group A")
        self.assert_equals("Group A" in t.groups, False, "Group A unassigned successfully")
        
        # Unassign non-existent group
        self.assert_raises(
            lambda: t.unassign_group("Group Z"),
            ValueError, "Unassigning non-existent group raises ValueError"
        )
    
    # ========== ACTIVE STATE TESTS ==========
    def test_active_state_management(self):
        print("\n🔘 Testing Active State Management...")
        
        t = Teacher("Alice", 50, "Prof", "CS")
        self.assert_equals(t.active, True, "Teacher starts as active")
        
        # Cannot deactivate with groups
        t.assign_group("CS101")
        self.assert_raises(
            lambda: t.deactivate(),
            AttributeError, "Cannot deactivate with assigned groups"
        )
        
        # Can deactivate after removing groups
        t.unassign_group("CS101")
        t.deactivate()
        self.assert_equals(t.active, False, "Teacher deactivated successfully")
        
        # Reactivate
        t.activate()
        self.assert_equals(t.active, True, "Teacher reactivated successfully")
    
    # ========== PERSONAL INFO TESTS ==========
    def test_personal_info_management(self):
        print("\n📝 Testing Personal Info Management...")
        
        t = Teacher("Old Name", 30, "Lecturer", "Math")
        
        # Update name
        t.update_name("New Name")
        self.assert_equals(t.get_name(), "New Name", "Name updated successfully")
        self.assert_raises(
            lambda: t.update_name(""),
            ValueError, "Empty name update raises ValueError"
        )
        
        # Update age
        t.update_age(35)
        self.assert_equals(t.get_age(), 35, "Age updated successfully")
        self.assert_raises(
            lambda: t.update_age(17),
            ValueError, "Invalid age update raises ValueError"
        )
        
        # Update rank
        t.update_rank("Senior Lecturer")
        self.assert_equals(t.get_rank(), "Senior Lecturer", "Rank updated successfully")
        
        # Cannot update rank when inactive
        t.deactivate()
        self.assert_raises(
            lambda: t.update_rank("Professor"),
            AttributeError, "Cannot update rank when inactive"
        )
    
    # ========== OBJECT EQUALITY TESTS ==========
    def test_object_equality(self):
        print("\n🔄 Testing Object Equality...")
        
        t1 = Teacher("John", 30, "Prof", "Math")
        t2 = Teacher("John", 30, "Prof", "Math")
        t3 = Teacher("John", 30, "Prof", "Physics")  # Different subject
        t4 = Teacher("Jane", 30, "Prof", "Math")      # Different name
        t5 = Teacher("John", 31, "Prof", "Math")      # Different age
        
        self.assert_equals(t1 == t2, True, "Same teachers are equal")
        self.assert_equals(t1 == t3, False, "Different subjects are not equal")
        self.assert_equals(t1 == t4, False, "Different names are not equal")
        self.assert_equals(t1 == t5, False, "Different ages are not equal")
        self.assert_equals(t1 == "not a teacher", False, "Comparison with non-Teacher is False")
        
        # Test __repr__
        repr_str = repr(t1)
        self.assert_equals("Teacher" in repr_str, True, "__repr__ contains class name")
        self.assert_equals("John" in repr_str, True, "__repr__ contains name")


if __name__ == "__main__":
    validator = TeacherValidator()
    success = validator.run_all_tests()
    exit(0 if success else 1)