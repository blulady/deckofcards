import pytest
from classes_sandbox import CardDeck


@pytest.fixture(scope="session")
def deck():
    deck = CardDeck()
    return deck


@pytest.fixture(scope="session")
def two_decks():
    return CardDeck(2)


@pytest.fixture(scope="session")
def nineteen():
    return CardDeck(19)