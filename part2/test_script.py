import pytest

from script import (
    split_lines,
    get_course_times,
    parse_log_entry,
    non_greedy_match,
    convert_usa_date,
    find_at_and_hashtags,
)


def test_split_lines():
    text = "Inception,2010;Christopher Nolan|8.8"
    expected = ["Inception", "2010", "Christopher Nolan", "8.8"]
    text = "Inception^2010+Christopher Nolan-8.8"
    expected = ["Inception", "2010", "Christopher Nolan", "8.8"]
    assert split_lines(text) == expected


def test_get_course_times():
    text = """
    What is Practical JavaScript? (3:47)
    The voice in your ear (40:41)
    Is this course right for you? 9:99 (1:21)
    What you'll build (5:32)
    The development process (2:23)
    (2:222)
    """
    expected = ["3:47", "40:41", "1:21", "5:32", "2:23"]
    assert get_course_times(text) == expected


@pytest.mark.parametrize(
    "log_entry, expected_result",
    [
        pytest.param(
            "2023-05-30 15:24:32 [INFO] User 'John' logged in.",
            ("2023-05-30 15:24:32", "INFO", "John", "logged in."),
            id="Valid log entry",
        ),
        pytest.param(
            "2023-05-30 15:30:45 [ERROR] User 'Alice' failed to authenticate.",
            ("2023-05-30 15:30:45", "ERROR", "Alice", "failed to authenticate."),
            id="Valid log entry with different log level",
        ),
        pytest.param(
            "2023-05-30 16:42:12 [DEBUG] User 'Robert' performed a complex operation successfully.",
            (
                "2023-05-30 16:42:12",
                "DEBUG",
                "Robert",
                "performed a complex operation successfully.",
            ),
            id="Valid log entry with longer message",
        ),
        pytest.param(
            "30-05-2023 10:15:20 [INFO] User 'Emily' accessed the system.",
            (None, None, None, None),
            id="Invalid log entry with different timestamp format",
        ),
        pytest.param(
            "2023-05-30 14:55:28 [INFO] User 'john_doe123' updated the user profile.",
            ("2023-05-30 14:55:28", "INFO", "john_doe123", "updated the user profile."),
            id="Valid log entry with username containing numbers and special characters",
        ),
    ],
)
def test_parse_log_entry(log_entry, expected_result):
    result = parse_log_entry(log_entry)
    assert result == expected_result


def test_non_greedy_match():
    text = "This is the first sentence. And this is the second sentence. What about a third sentence?"
    assert non_greedy_match(text) == "This is the first sentence"
    text = "This is the first sentence? And this is the second sentence. What about a third sentence?"
    assert non_greedy_match(text) == "This is the first sentence"


def test_convert_usa_date():
    assert convert_usa_date("11-30-2022") == "30-11-2022"
    assert convert_usa_date("30-11-2022") == "11-30-2022"


def test_find_at_and_hashtags():
    tweet = "New PyBites article: Module of the Week - Requests-cache for Repeated API Calls - http://pybit.es/requests-cache.html ... #python #APIs"
    expected = ["http://pybit.es/requests-cache.html", "#python", "#APIs"]
    assert find_at_and_hashtags(tweet) == expected
