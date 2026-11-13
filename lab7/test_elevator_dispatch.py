from hypothesis import given, strategies as st
from elevator_dispatch import parse_request, total_travel, load_percent


@given(st.text() | st.none())
def test_parse_request_no_crash(s):
    try:
        result = parse_request(s)
        assert result is None or (
            isinstance(result, tuple)
            and len(result) == 2
            and isinstance(result[0], int)
            and isinstance(result[1], int)
        )
    except Exception as e:
        assert False, f"parse_request crashed on {s!r} with: {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_total_travel_no_crash(s):
    try:
        result = total_travel(s)
        assert isinstance(result, int) and result >= 0
    except Exception as e:
        assert False, f"total_travel crashed on {s!r} with: {type(e).__name__}: {e}"


@given(st.text() | st.none())
def test_load_percent_no_crash(s):
    try:
        result = load_percent(s)
        assert result is None or (isinstance(result, int) and result >= 0)
    except Exception as e:
        assert False, f"load_percent crashed on {s!r} with: {type(e).__name__}: {e}"