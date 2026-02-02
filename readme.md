# Homework 35: Regular Expressions in Python

## Task Definition

The goal of this assignment is to implement **two regular expression patterns** using Python that satisfy a predefined specification and fully pass all provided unit tests.

You are required to complete the following methods inside the `RegexPatterns` class:

- `ipv4_address_re`
- `mobile_israeli_number_re`

The implementation must strictly follow the rules described in the docstrings and comply with all test cases defined in `test_regular_expressions.py`.

Key requirements:

- Only **regular expressions** may be used (no additional logic or parsing)
- The returned value of each method must be a **string representing a regex pattern**
- All tests must pass using `re.fullmatch`
- The solution must correctly distinguish between **valid** and **invalid** inputs

---

## 📝 Description

This project is focused on practicing **advanced regular expressions** and validating them using automated unit tests.

The `RegexPatterns` class serves as a centralized collection of regex patterns for validating:

- Python identifiers
- Strong passwords
- IPv4 addresses
- Israeli mobile phone numbers

While some patterns are already implemented, this homework specifically targets **network-related and locale-specific validation**, which are common real-world use cases for regular expressions.

---

## 🎯 Purpose

The purpose of this assignment is to:

- Develop a deeper understanding of **regex composition**
- Practice writing **readable and maintainable** regular expressions
- Learn how to encode **business rules** directly into regex patterns
- Gain experience with **test-driven development (TDD)**
- Understand how `re.fullmatch` enforces full-string validation

These skills are essential for backend development, input validation, and data sanitization.

---

## 🔍 How It Works

### 1. RegexPatterns Class

The `RegexPatterns` class exposes static methods that return regex strings.

Each method is responsible for **one specific validation rule**, and the returned regex is later tested using Python’s `re.fullmatch` function.

```py
RegexPatterns.ipv4_address_re()
RegexPatterns.mobile_israeli_number_re()
```

---

### 2. IPv4 Address Validation

The `IPv4` regex must match addresses consisting of:

- Exactly **four octets**
- Octets separated by dots (`.`)
- Each octet must be a number between **0 and 255**
- Leading zeros **are allowed**, but:
    - More than 3 digits per octet is forbidden
    - Values above 255 are invalid

#### Valid Examples

```
0.0.0.0
0.01.002.000
000.1.249.59
250.255.199.9
```

#### Invalid Examples

```
0.0.0
0.0.0.256
0.0.0.280
0.0.0.0001
0.0.0.a
```

The solution achieves this by splitting octets into logical numeric ranges and combining them into a single reusable pattern.

---

### 3. Israeli Mobile Phone Number Validation

The Israeli mobile number regex must support **both international and local formats**.

#### Supported Formats

**International**

```
+972-54-1234567
+972-541234567
```

**Local**

```
054-1-23-45-67
059123-45-67
```

#### Rules

- Operator prefixes: **50–59**
- Optional dashes depending on format
- Several valid body groupings:
    - `xxxxxxx`
    - `xxx-xx-xx`
    - `x-xx-xx-xx`
- No extra digits or misplaced separators allowed

#### Invalid Examples

```
+972-054-1234567
+972-54-1-234-567
059123-45-677
054-1-2-3-45-67
```

This regex demonstrates how complex formatting rules can be encoded using **alternation, grouping, and optional segments**.

---

## 📜 Output Example

```py
import re
from src import RegexPatterns

pattern = RegexPatterns.ipv4_address_re()

re.fullmatch(pattern, "192.168.1.1")   # Match
re.fullmatch(pattern, "256.1.1.1")     # No match
```

---

## 📦 Usage

```py
from src import RegexPatterns
import re

ipv4_regex = RegexPatterns.ipv4_address_re()
mobile_regex = RegexPatterns.mobile_israeli_number_re()

print(re.fullmatch(ipv4_regex, "127.0.0.1"))
print(re.fullmatch(mobile_regex, "+972-54-1234567"))
```

---

## 🧪 Tests

All validation is done through **unit tests** located in:

```
tests/test_regex_patterns.py
```

The tests:

- Use `re.fullmatch` for strict matching
- Validate both **positive and negative** cases
- Ensure no partial matches slip through
- Cover edge cases and formatting pitfalls

To run the tests:

```bash
python -m unittest
```

---

## ✅ Dependencies

- Python 3.10+
- Standard library only:
    - `re`
    - `unittest`
    - `typing`

No external dependencies are required.

---

## 📊 Project Status

**Status:** Completed ✅

- All required regex patterns implemented
- All unit tests passing
- Code follows clean, readable, and maintainable style
- Fully compliant with task requirements

---

## 📄 License

MIT License

---

## 🧮 Conclusion

This homework demonstrates how **complex validation logic** can be implemented using pure regular expressions while maintaining clarity and correctness.

The project highlights the importance of:

- Well-defined specifications
- Test-driven development
- Regex readability and structure

These skills are directly applicable to backend validation, APIs, and production-grade systems.

---

Made with ❤️ and `Python` by **Sam-Shepsl Malikin** 🎓
