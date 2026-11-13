import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator

def test_up_with_above_and_below():
    assert next_direction(3, "up", [1, 5]) == "up"

def test_up_with_only_below():
    assert next_direction(4, "up", [2]) == "down"

def test_up_with_same_floor_request_only():
    assert next_direction(4, "up", [4]) == "idle"

def test_down_with_below_and_above():
    assert next_direction(3, "down", [1, 5]) == "down"

def test_down_with_only_above():
    assert next_direction(2, "down", [5]) == "up"

def test_down_with_no_valid_requests():
    assert next_direction(3, "down", []) == "idle"

def test_idle_with_above():
    assert next_direction(1, "idle", [4]) == "up"

def test_idle_with_below():
    assert next_direction(5, "idle", [2]) == "down"

def test_idle_with_no_requests():
    assert next_direction(3, "idle", []) == "idle"

def test_door_emergency_overrides_all():
    assert door_action(800, True, True) == "hold_open"

def test_door_overload_above_threshold():
    assert door_action(631, True, False) == "overload"

def test_door_at_exact_limit_not_overloaded():
    assert door_action(630, False, False) == "close"

def test_door_blocked_reopens():
    assert door_action(500, True, False) == "reopen"

def test_door_normal_close():
    assert door_action(0, False, False) == "close"

def test_pick_elevator_all_branches():
    cars = [
        ("E1", 1, False),
        ("E2", 2, True),
        ("E3", 10, True),
    ]
    assert pick_elevator(cars, 3) == "E2"

def test_pick_elevator_empty_list():
    assert pick_elevator([], 3) is None