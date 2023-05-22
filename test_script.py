import pytest

from script import (
    email_regex,
    url_regex,
    phone_number_regex,
    hello_world,
    lowercase_letters,
    contains_digit,
    consecutive_vowels,
    word_length,
    consecutive_consonants,
    consecutive_repeating_characters,
    mixed_case_letters,
    vowel_start_length,
    repeated_word,
    word_start_end_az,
    word_start_end_ae_noz,
)

# Exercise 1
def test_email_regex():
    assert email_regex("test@example.com")
    assert email_regex("user.name@example.co.uk")
    assert not email_regex("invalid.email")
    assert not email_regex("test@example")
    assert not email_regex("test@example..com")

# Exercise 2
def test_url_regex():
    assert url_regex("https://www.example.com")
    assert url_regex("http://example.org")
    assert url_regex("ftp://ftp.example.com")
    assert not url_regex("www.example.com")
    assert not url_regex("http:/example.org")
    assert not url_regex("example.org")

# Exercise 3
def test_phone_number_regex():
    assert phone_number_regex("(123)456-7890")
    assert not phone_number_regex("(123)4567890")
    assert not phone_number_regex("123456-7890")
    assert not phone_number_regex("(123)456-7890abc")

# Exercise 4
def test_hello_world():
    assert hello_world("hello world")
    assert hello_world("hello123 world")
    assert not hello_world("hello123world")
    assert not hello_world("helloworld")

# Exercise 5
def test_lowercase_letters():
    assert lowercase_letters("abcd")
    assert not lowercase_letters("abcD")
    assert not lowercase_letters("1234")

# Exercise 6
def test_contains_digit():
    assert contains_digit("abc123")
    assert contains_digit("abcd")
    assert not contains_digit("efgh")

# Exercise 7
def test_consecutive_vowels():
    assert consecutive_vowels("aiou")
    assert consecutive_vowels("aeiou")
    assert not consecutive_vowels("aeio")

# Exercise 8
def test_word_length():
    assert word_length("apple")
    assert not word_length("pear")
    assert not word_length("grapefruit")

# Exercise 9
def test_consecutive_consonants():
    assert consecutive_consonants("xyzbcdfg")
    assert consecutive_consonants("bcd")
    assert not consecutive_consonants("aeiou")

# Exercise 10
def test_consecutive_repeating_characters():
    assert consecutive_repeating_characters("hello")
    assert consecutive_repeating_characters("goooood")
    assert not consecutive_repeating_characters("world")

# Exercise 11
def test_mixed_case_letters():
    assert mixed_case_letters("HelloWorld")
    assert mixed_case_letters("helloworld")
    assert not mixed_case_letters("HELLO")

# Exercise 12
def test_vowel_start_length():
    assert vowel_start_length("apple")
    assert vowel_start_length("elephant")
    assert not vowel_start_length("orange")

# Exercise 13
def test_repeated_word():
    assert repeated_word("Hello Hello")
    assert repeated_word("How are you? How are you?")
    assert not repeated_word("No repetition here")

# Exercise 14
def test_word_start_end_az():
    assert word_start_end_az("apple")
    assert word_start_end_az("aardvark")
    assert not word_start_end_az("banana")

# Exercise 15
def test_word_start_end_ae_noz():
    assert word_start_end_ae_noz("apple")
    assert word_start_end_ae_noz("ape")
    assert not word_start_end_ae_noz("aze")

# Run the tests
if __name__ == '__main__':
    pytest.main()

