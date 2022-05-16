import requests
import json
import pytest

BASE_URL = "https://deckofcardsapi.com/api/deck"


def shuffle_new_deck(BASE_URL, COUNT):
    """count equals the query variable for how many decks you want and the url is the api url
        returns deck"""
    deck_response = requests.get(f"{BASE_URL}/new/shuffle/?deck_count={COUNT}")
    return deck_response.json()

def get_deck_id(deck):
    """takes deck json from shuffle_new_deck()
    returns deck_id for drawing from deck"""
    return deck['deck_id']

def deal_new_cards(deck_id, num_of_cards):
    """takes the deck_id and number of cards you want
    deal new cards from the same deck"""
    new_cards = requests.get(f'https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count={num_of_cards}')
    return new_cards.json()["cards"]

def get_cards(deck_id):
    """takes a deck json and
    returns the cards the api dealt us"""
    return deck_cards.json()["cards"]

    

def test_items_in_json():
    """test to make sure that the api has returned the correct data"""
    things = [item for item in deck_cards.json()]
    check_things = ['success', 'deck_id', 'cards', 'remaining']
    things == check things

def test_card_value(cards):
    """ make sure the value of the card is a number or facecard,
    returns True if so and false if not"""
        face_cards = ["JACK", "KING", "QUEEN", "ACE"]
        are_valid_values = []
        for item in cards:
            if item["value"] in face_cards:
                are_valid_values.append(True)
            else:
                are_valid_values.append(type(int(item["value"])) == int)
        if False in are_valid_values:
            return False
        else:
            return True

def test_card_suit(cards):
    """make sure the suit string is one of the four suits"""
    suits = ["DIAMONDS", "SPADES", "HEARTS", "CLUBS"]
    for item in cards:
             if item["suit"] not in suits:
                 return False
    return True
    
