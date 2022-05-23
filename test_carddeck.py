import pytest
from classes_sandbox import CardDeck


def test_card_deck_response():
    deck = CardDeck(1)
    assert deck.deck["success"] is True


def test_deck_id():
    deck = CardDeck(1)
    assert isinstance(deck.deck_id, str) is True


def test_one_deck_remaining():
    deck = CardDeck(1)
    assert deck.deck_remaining == 52


def test_two_decks_remaining():
    two_decks = CardDeck(2)
    assert two_decks.deck_remaining == 104


#write tests to test the assertion error for line 8/9 in carddeck
#write test to test str & repr output
#write a conftest file
#reorganize tests
#test to see if the repr returns the correct count
#write a test
#create a mock to test non 200 responses