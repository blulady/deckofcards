import pytest

@pytest.fixture(scope="file")
def new_deck():
    """returns a new deck from https://deckofcardsapi.com/"""
    deck_response = requests.get(f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=2")
    return deck_response.json()
