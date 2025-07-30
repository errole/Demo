from app.rps import determine_winner

def test_example():
    assert 2+2 == 4

def test_winner():
    assert determine_winner('rock', 'rock') == 'TIE GAME'
    assert determine_winner('paper', 'paper') == 'TIE GAME'
    assert determine_winner('scissor', 'scissor') == 'TIE GAME'

    assert determine_winner('rock', 'scissor') == 'USER WIN'
    assert determine_winner('scissor', 'paper') == 'USER WIN'
    assert determine_winner('paper', 'rock') == 'USER WIN'

    assert determine_winner('rock', 'paper') == 'COMP WIN'
    assert determine_winner('scissor', 'rock') == 'COMP WIN'
    assert determine_winner('paper', 'scissor') == 'COMP WIN'

