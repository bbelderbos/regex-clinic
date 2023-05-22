import re

"""
[A-Z] character classes
* = 0 or more
+ = 1 or more
() = group stuff
\. = escape a character
\w = word character (todo: what does it include?)
? = optional
{3} = match 3 of ...
^$ = begin and end
"""

def email_regex(string):
    return re.match(r"[A-Za-z.]+@(\w+\.)+\w+", string)


def url_regex(string):
    return re.match(r"^(https?|ftp)://.*\.(org|com)", string)


def phone_number_regex(string):
    return re.match(r"^\(\d{3}\)\d{3}-\d{4}$", string)


def hello_world(string):
    pass


def lowercase_letters(string):
    pass


def contains_digit(string):
    pass


def consecutive_vowels(string):
    pass


def word_length(string):
    pass


def consecutive_consonants(string):
    pass


def consecutive_repeating_characters(string):
    pass


def mixed_case_letters(string):
    pass


def vowel_start_length(string):
    pass


def repeated_word(string):
    pass


def word_start_end_az(string):
    pass


def word_start_end_ae_noz(string):
    pass
