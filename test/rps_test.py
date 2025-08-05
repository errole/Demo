from app.rps import determine_winner

def test_example():
    assert 2+2 == 4

def test_winner():
    assert determine_winner('rock', 'rock') == 'TIE GAME'
    assert determine_winner('paper', 'paper') == 'TIE GAME'
    assert determine_winner('scissors', 'scissors') == 'TIE GAME'

    assert determine_winner('rock', 'scissors') == 'USER WIN'
    assert determine_winner('scissors', 'paper') == 'USER WIN'
    assert determine_winner('paper', 'rock') == 'USER WIN'

    assert determine_winner('rock', 'paper') == 'COMP WIN'
    assert determine_winner('scissors', 'rock') == 'COMP WIN'
    assert determine_winner('paper', 'scissors') == 'COMP WIN'

