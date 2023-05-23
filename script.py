import re


def lowercase_letters(string):
    """
    Write a regular expression to match a string that contains only lowercase letters.
    """
    return string.islower()


def contains_digit(string):
    """
    Write a regular expression to match a string that contains at least one digit.
    """
    return any(c.isdigit() for c in string)


def word_length(string):
    """
    Write a regular expression to match a string that contains a word with exactly five letters.
    """
    return re.match(r"^\w{5}$", string)


def url_regex(string):
    """
    Write a regular expression to match a valid URL.
    """
    return re.match(r"^https?://(www\.)?\w+\.(com|org)$", string)


def mixed_case_letters(string):
    """
    Write a regular expression to match a string that contains a word with both uppercase and lowercase letters.
    """
    # look ahead more complex - pattern = r'^(?=.*[a-z])(?=.*[A-Z]).+$'
    has_lowercase = bool(re.search("[a-z]", string))
    has_uppercase = bool(re.search("[A-Z]", string))
    is_word = bool(re.match("^[A-Za-z]+$", string))
    return has_lowercase and has_uppercase and is_word


def phone_number_regex(string):
    """
    Write a regular expression to match a phone number in a specific format, such as (123)456-7890.
    """
    return re.match(r"^\(\d{3}\)\d{3}-\d{4}$", string)


def consecutive_consonants(string):
    """
    Write a regular expression to match a string that contains a word with three or more consecutive consonants.
    """
    return re.search(r"[^aeiou]{3,}", string)


def hello_world(string):
    """
    Write a regular expression to match a string that starts with "hello" and ends with "world".
    """
    return string.startswith("hello") and string.endswith("world")


def consecutive_vowels(string):
    """
    Write a regular expression to match a string that contains three consecutive vowels.
    """
    return re.search(r"[aeiou]{3}", string)


def word_start_end_ae_noz(string):
    """
    Write a regular expression to match a string that contains a word that starts with "a" and ends with "e" and may have any number of characters in between, excluding "z".
    """
    return re.match(r"^a[^z]+e$", string)


def email_regex(string):
    """
    Write a regular expression to match an email address.
    """
    return re.match(r"[A-Za-z.]+@(\w+\.)+\w+", string)


def vowel_start_length(string):
    """
    Write a regular expression to match a string that contains a word with a length of 7 or more characters and starts with a vowel.
    """
    return re.match(r"^[aeiou]\w{6,}$", string, re.I)


def consecutive_repeating_characters(string):
    """
    Write a regular expression to match a string that contains a word with two or more consecutive repeating characters.
    """
    return re.search(r"(\w)\1", string)


def repeated_word(string):
    """
    Write a regular expression to match a string that contains a word that is repeated consecutively at least twice.
    """
    return re.search(r"([\w ?]+)\s\1", string)


def word_start_end_az_and_one_digit(string):
    """
    Write a regular expression to match a string that contains a word starting
    with "a" and ending with "z", with at least one digit in between.
    """
    return re.match(r"^a.*\d+.*z$", string)
