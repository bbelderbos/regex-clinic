import re


def split_lines(text):
    """Split by regex"""
    return re.split(r"[^\w\d. ]", text)


def get_course_times(text):
    """Extract a pattern"""
    return re.findall(r"\((\d{1,2}:\d{1,2})\)", text)


def parse_log_entry(text):
    """Parse a log entry, use verbose"""
    m = re.match(
        r"""
        (?P<datetime>\d{4}-\d{2}-\d{2}
        \s
        \d{2}:\d{2}:\d{2})   # time
        \s
        \[(?P<alert>\w+)\]
        \sUser\s
        '(?P<user>\w+)'
        \s
        (?P<message>.*)
    """,
        text,
        re.VERBOSE,
    )
    if m is not None:
        return m.groups()
    else:
        return (None, None, None, None)


def non_greedy_match(text):
    """Watch out for greediness"""
    m = re.match(r"(.*?)[.?]", text)
    if m is not None:
        return m.group(1)
    else:
        return None


def convert_usa_date(date_str):
    """Backreference example"""
    return re.sub(
        r"(?P<month>\d{2}-)(?P<day>\d{2}-)(?P<year>\d{4})",
        r"\g<day>\g<month>\g<year>",
        date_str,
    )


def find_at_and_hashtags(text):
    """Non capturing grouping"""
    # return re.findall(r"(https?\S+|#\S+)", text)
    return re.findall(r"((?:#|http)\S+)", text)
