class RegexPatterns:
    """
    Collection of regex patterns for Python identifiers, passwords,
    IPv4 addresses, and Israeli mobile numbers.
    """

    @staticmethod
    def pythonic_name_re() -> str:
        """
        Return a regular expression for a valid Python identifier.

        A valid identifier:
        - starts with a letter or underscore
        - continues with letters, digits, or underscores
        """
        first_character = r"[A-Za-z_]"
        remaining_characters = r"\w*"

        return first_character + remaining_characters

    @staticmethod
    def password_re() -> str:
        """
        Return a regular expression for a strong password.

        A valid password must:
        - Contain at least one uppercase letter
        - Contain at least one lowercase letter
        - Contain at least one special character (#, $, %)
        - Contain at least one digit
        - Be at least 8 characters long
        - May include letters, digits, and special characters (#, $, %, _, -)
        """
        # Positive lookaheads
        has_uppercase = r"(?=.*[A-Z])"
        has_lowercase = r"(?=.*[a-z])"
        has_special = r"(?=.*[#$%])"
        has_digit = r"(?=.*\d)"

        # Allowed characters and minimum length
        allowed_chars = r"[A-Za-z#$%\d_-]{8,}"

        letters = has_uppercase + has_lowercase

        # Combine all parts
        return letters + has_special + has_digit + allowed_chars

    @staticmethod
    def ipv4_address_re() -> str:
        """
        Return a regular expression pattern for matching IPv4 addresses.

        IPv4 addresses consist of four octets separated by dots.
        Each octet is a number from 0 to 255
        (1-3 digits, leading zeros allowed).

        Returns:
            str: Regular expression pattern for an IPv4 address.
        """
        # Define each octet separately
        octet_250_255 = r"25[0-5]"     # 250-255
        octet_200_249 = r"2[0-4]\d"    # 200-249
        octet_100_199 = r"1\d{2}"      # 100-199
        octet_0_99 = r"0?\d{1,2}"       # 0-99, leading zeros allowed

        # Combine all options for a single octet
        octet_200_255 = rf"{octet_250_255}|{octet_200_249}"
        octet = rf"(?:{octet_200_255}|{octet_100_199}|{octet_0_99})"

        # Full IPv4 pattern: four octets separated by dots
        ipv4_pattern = rf"{octet}\.{octet}\.{octet}\.{octet}"

        return ipv4_pattern

    @staticmethod
    def mobile_israeli_number_re() -> str:
        """
        Return a regular expression pattern for Israeli mobile phone numbers.

        Supported formats:
            International:
                +972-XXxxxxxxx
                +972-XX-xxxxxxx
            Local:
                0XXxxxxxxx
                0XX-xxxxxxx

        Operators: 50-59
        Body formats:
            - xxxxxxx
            - xxx-xx-xx
            - x-xx-xx-xx

        Returns:
            str: Regular expression pattern for an Israeli mobile number.
        """
        # Operator prefix (50-59)
        operator_prefix = r"5[0-9]"

        # Different body formats
        body_plain = r"\d{7}"           # xxxxxxx
        body_grouped_3_2_2 = r"\d{3}-\d{2}-\d{2}"  # xxx-xx-xx
        body_grouped_1_2_2_2 = r"\d-\d{2}-\d{2}-\d{2}"  # x-xx-xx-xx

        # Combine all body formats into a single pattern
        body_grouped = rf"{body_grouped_3_2_2}|{body_grouped_1_2_2_2}"
        body_pattern = rf"(?:{body_plain}|{body_grouped})"

        # International format: +972-XXxxxxxxx or +972-XX-xxxxxxx
        intl_pattern = rf"\+972-{operator_prefix}-?{body_pattern}"

        # Local format: 0XXxxxxxxx or 0XX-xxxxxxx
        local_pattern = rf"0{operator_prefix}-?{body_pattern}"

        # Final pattern: either international or local
        full_pattern = rf"(?:{intl_pattern}|{local_pattern})"

        return full_pattern
