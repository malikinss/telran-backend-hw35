# tests/test_regex_patterns.py

import re
from unittest import TestCase, main
from src import RegexPatterns


class TestRegexPatterns(TestCase):
    """
    Unit tests for RegexPatterns class.

    Tests all supported regular expressions:
    - Pythonic identifiers
    - Strong passwords
    - IPv4 addresses
    - Israeli mobile phone numbers
    """

    def setUp(self):
        """
        Compile regex patterns once for all tests.
        """
        self.pythonic_name = RegexPatterns.pythonic_name_re()
        self.password = RegexPatterns.password_re()
        self.ipv4 = RegexPatterns.ipv4_address_re()
        self.mobile_israel = RegexPatterns.mobile_israeli_number_re()

    def _check_regex(
        self,
        regex: str,
        valid_list: list[str],
        invalid_list: list[str]
    ):
        """
        Helper function to test regex patterns against valid and
        invalid examples.

        Args:
            regex (str): Regex pattern to test.
            valid_list (list[str]): List of strings that should match.
            invalid_list (list[str]): List of strings that should not match.
        """
        for val in valid_list:
            with self.subTest(val=val):
                self.assertTrue(re.fullmatch(regex, val))
        for inval in invalid_list:
            with self.subTest(val=inval):
                self.assertFalse(re.fullmatch(regex, inval))

    def test_pythonic_name(self):
        """
        Test valid and invalid Python identifiers.
        """
        self._check_regex(
            self.pythonic_name,
            valid_list=["__", "a", "_aA12", "__a__"],
            invalid_list=["1_", "a b", "$a12", "a*b"]
        )

    def test_password(self):
        """
        Test strong password regex.
        """
        self._check_regex(
            self.password,
            valid_list=["Aa123#57", "Aa123#57--"],
            invalid_list=[
                "aa123#57", "Aa123#57 ", "Aa123#5",
                "AaBBB###", "aa12357CD1"
            ]
        )

    def test_ipv4_address(self):
        """
        Test IPv4 address regex.
        """
        self._check_regex(
            self.ipv4,
            valid_list=[
                "0.0.0.0", "0.01.002.000",
                "000.1.249.59", "250.255.199.9"
            ],
            invalid_list=[
                "0.0.0", "0000.0.0.2", "0.0.0.256",
                "0.0 0.2", "0.0.0.280", "0.0.0.0001",
                "0.0.0. 190", "0.0.0.+1", "0.0.0.a"
            ]
        )

    def test_mobile_israel(self):
        """
        Test Israeli mobile number regex.
        """
        self._check_regex(
            self.mobile_israel,
            valid_list=[
                "+972-54-1234567", "+972-541234567", "059123-45-67",
                "054-1-23-45-67", "0571-23-45-67"
            ],
            invalid_list=[
                "+972-054-1234567", "+972-54-1-234-567",
                "+972-54123456", "059123-45-677",
                "054-1-2-3-45-67", "0571-23-45-6-7"
            ]
        )


if __name__ == "__main__":
    main()
