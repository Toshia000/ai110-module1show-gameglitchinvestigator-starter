from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert message == "🎉 Correct!"

def test_guess_too_high():
    # If secret is 50 and guess is 60, the player should be told to go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message == "📉 Go LOWER!"

def test_guess_too_low():
    # If secret is 50 and guess is 40, the player should be told to go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"

def test_numeric_not_lexicographic_comparison():
    # 9 < 10 numerically, even though "9" > "10" as strings
    outcome, message = check_guess(9, 10)
    assert outcome == "Too Low"
    assert message == "📈 Go HIGHER!"
