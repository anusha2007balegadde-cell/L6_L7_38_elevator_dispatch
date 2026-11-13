import pytest
from elevator_dispatch import next_direction, door_action, pick_elevator

def test_direction_up_continues_up():
    assert next_direction(2, "up", [5]) == "up"

def test_direction_up_reverses_down():
    assert next_direction(5, "up", [2]) == "down"

def test_direction_up_becomes_idle():
    assert next_direction(5, "up", []) == "idle"

def test_direction_down_continues_down():
    assert next_direction(5, "down", [2]) == "down"

def test_direction_down_reverses_up():
    assert next_direction(2, "down", [5]) == "up"

def test_direction_down_becomes_idle():
    assert next_direction(5, "down", []) == "idle"

def test_direction_idle_goes_up():
    assert next_direction(2, "idle", [6]) == "up"

def test_direction_idle_goes_down():
    assert next_direction(6, "idle", [2]) == "down"

def test_direction_idle_stays_idle():
    assert next_direction(3, "idle", []) == "idle"

def test_door_emergency():
    assert door_action(100, False, True) == "hold_open"

def test_door_overload():
    assert door_action(700, False, False) == "overload"

def test_door_blocked():
    assert door_action(100, True, False) == "reopen"

def test_door_normal_close():
    assert door_action(100, False, False) == "close"

def test_pick_elevator_basic():
    cars = [("E1", 5, False), ("E2", 2, True)]
    assert pick_elevator(cars, 3) == "E2"