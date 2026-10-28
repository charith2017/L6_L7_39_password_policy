"""Lab 6: tests for branch coverage, boundaries and decision outcomes."""
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

@pytest.mark.parametrize("pw, expected", [
    ("", ["too short", "no uppercase", "no lowercase", "no digit", "no special"]),
    ("Aa1!xxx", ["too short"]),
    ("Aa1!xxxx", []),
    ("Aa1!" + "x" * 60, []),
    ("PASSWORD", ["common", "no lowercase", "no digit", "no special"]),
    ("abcdef1!", ["no uppercase"]),
    ("ABCDEF1!", ["no lowercase"]),
    ("Abcdefg!", ["no digit"]),
    ("Abcdef12", ["no special"]),
])
def test_boundaries_and_character_classes(pw, expected):
    assert check_password(pw) == expected

@pytest.mark.parametrize("pw, expected", [
    ("Aa1!" + "x" * 9, "good"),
    ("Aa1!" + "x" * 10, "strong"),
    ("abcdefgh", "very weak"),
    ("Abcdefgh", "weak"),
])
def test_strength_thresholds(pw, expected):
    assert strength(pw) == expected

@pytest.mark.parametrize("issue", ["uppercase", "lowercase", "digit", "special"])
def test_each_missing_class_suggestion(issue):
    assert suggest_fix(["no " + issue]) == "add " + issue

def test_suggestion_uses_first_issue_only():
    assert suggest_fix(["common", "too short"]) == "avoid common passwords"
