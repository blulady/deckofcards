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


