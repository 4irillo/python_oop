# Python OOP Laboratory Works

This repository contains laboratory works for the Object-Oriented Programming in Python course.

## Repository Structure

```
python_oop/
├─ README.md                 # This file
├─ src/                      # Source code
│  ├─ Lab01/                 # Laboratory Work 1
│  │   ├─ __init__.py
│  │   ├─ model.py           # Teacher class implementation
│  │   ├─ validation.py      # Input validation module
│  │   ├─ demo.py            # Demonstration script
│  │   ├─ validate.py        # Test suite
│  │   └─ README.md          # Lab01 report
│  └─ Lab02/                 # Laboratory Work 2
│      ├─ model.py
│      ├─ demo.py
│      └─ validate.py
```

## Laboratory Work 1: Class and Encapsulation

**Topic:** Implementation of a `Teacher` class with encapsulation and validation.

**Key Features:**
- ✅ Encapsulation with private attributes
- ✅ Comprehensive input validation
- ✅ Business methods (rating system, group management)
- ✅ State management (active/inactive)
- ✅ Magic methods (`__repr__`, `__eq__`, `__hash__`)
- ✅ Validation extracted to separate module (`validation.py`)

**Grade:** 5 (all requirements met)

### Running Lab01

```bash
cd src/Lab01

# Run demonstration
python demo.py

# Run test suite
python validate.py
```

### Lab01 Files

| File | Description |
|------|-------------|
| `model.py` | Teacher class with all business logic |
| `validation.py` | Reusable validation functions |
| `demo.py` | Interactive demonstration of all features |
| `validate.py` | Comprehensive test suite (39 tests) |
| `README.md` | Detailed report with answers to questions |

## Laboratory Work 2

See `src/Lab02/README.md` for details.

## Requirements

- Python 3.8+
- No external dependencies (standard library only)

## Author

Student repository for OOP Python course.
