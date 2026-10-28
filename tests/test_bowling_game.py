from src.bowling_game import BowlingGame
import pytest

def test_gutter_game_scores_zero():
    game = BowlingGame()

    for i in range(20):
        game.roll(0)

    assert game.score() == 0

def test_score_without_spares_or_strikes():
    game = BowlingGame()

    for i in range(10):
        game.roll(3)
        game.roll(4)

    assert game.score() == 70


def test_spare_adds_next_roll_as_bonus():
    game = BowlingGame()

    game.roll(7)
    game.roll(3)
    game.roll(4)

    for i in range(17):
        game.roll(0)

    assert game.score() == 18


def test_strike_adds_next_two_rolls_as_bonus():
    game = BowlingGame()

    game.roll(10)
    game.roll(3)
    game.roll(4)

    for i in range(16):
        game.roll(0)

    assert game.score() == 24

def test_consecutive_strikes():
    game = BowlingGame()

    game.roll(10)
    game.roll(10)
    game.roll(3)
    game.roll(4)

    for i in range(14):
        game.roll(0)

    assert game.score() == 47

def test_perfect_game_scores_300():
    game = BowlingGame()

    for i in range(12):
        game.roll(10)

    assert game.score() == 300

def test_spare_in_tenth_frame_allows_extra_roll():
    game = BowlingGame()

    for i in range(18):
        game.roll(0)

    game.roll(7)
    game.roll(3)
    game.roll(5)

    assert game.score() == 15

def test_strike_in_tenth_frame_allows_two_extra_rolls():
    game = BowlingGame()

    for i in range(18):
        game.roll(0)

    game.roll(10)
    game.roll(7)
    game.roll(2)

    assert game.score() == 19


def test_score_in_incomplete_game():
    game = BowlingGame()

    game.roll(3)
    game.roll(4)

    assert game.score() == 7

def test_incomplete_spare_does_not_add_unknown_bonus():
    game = BowlingGame()

    game.roll(7)
    game.roll(3)

    assert game.score() == 10

def test_incomplete_strike_does_not_add_unknown_bonus():
    game = BowlingGame()

    game.roll(10)

    assert game.score() == 0

def test_mixed_game_scores_correctly():
    game = BowlingGame()

    rolls = [
        1, 4,
        4, 5,
        6, 4,
        5, 5,
        10,
        0, 1,
        7, 3,
        6, 4,
        10,
        2, 8, 6
    ]

    for pins in rolls:
        game.roll(pins)

    assert game.score() == 133

def test_roll_cannot_knock_down_more_than_ten_pins():
    game = BowlingGame()

    with pytest.raises(ValueError):
        game.roll(11)