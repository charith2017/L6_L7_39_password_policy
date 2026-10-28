"""Lab 6: tests for statement (line) coverage."""
import pytest
from password_policy import check_password, strength, suggest_fix

@pytest.mark.parametrize("pw, expected", [
    ("Abcdef1!", []),
    ("Aa1!", ["too short"]),
    ("Aa1!" + "x" * 61, ["too long"]),
    ("password", ["common", "no uppercase", "no digit", "no special"]),
    ("ABCDEFG!", ["no lowercase", "no digit"]),
])
def test_password_issues(pw, expected):
    assert check_password(pw) == expected

@pytest.mark.parametrize("pw, expected", [
    ("Abcdef1!", "good"),
    ("Abcdefghijkl1!", "strong"),
    ("Aa1!", "weak"),
    ("password", "very weak"),
])
def test_strength(pw, expected):
    assert strength(pw) == expected

@pytest.mark.parametrize("issues, expected", [
    ([], "none needed"),
    (["too short"], "add more characters"),
    (["common"], "avoid common passwords"),
    (["no uppercase"], "add uppercase"),
    (["too long"], "shorten it"),
])
def test_suggest_fix(issues, expected):
    assert suggest_fix(issues) == expected
