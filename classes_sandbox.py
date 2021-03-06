import requests
from functools import total_ordering


class CardDeck:
    """a class so we can check the accuracy of remaining cards in a deck
    count is the number of decks we want to pull"""
    class API_EXCEPTION(Exception):
        pass

    def __init__(self, count=1):
        self.count = count
        response = requests.get(f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={count}")
        if response.status_code != 200:
            raise CardDeck.API_EXCEPTION(f"Unable to access API. Code: {response.status_code}")
        # API will return a 200 if you send too many decks so check for a success
        if not response.json()["success"]:
            raise Exception("You pulled too many decks, the number of decks you can pull is 20")
        self.deck = response.json()
        self.deck_id = self.deck["deck_id"]
        self.deck_remaining = self.deck["remaining"]
        self.deck_shuffled = self.deck["shuffled"]
        self.card_count = 0
        self.card_list = []
        self.card_json = {}
        self.cards = []

    def __repr__(self):
        return f'CardDeck({self.count})'

    @total_ordering
    def __eq__(self, other):
        return {self.deck_remaining} == {other.deck_remaining}

    def __lt__(self, other):
        return self.deck_remaining < other.deck_remaining

    def draw_cards(self, count):
        """count is the number of cards you want to draw
        returns the json for the cards you drew from the deck"""
        card_response = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count={count}")
        # try:
        #     card_response.raise_for_status()
        # except card_response.exceptions as e:
        #     return e
        self.card_json = card_response.json()
        self.deck['remaining'] = self.card_json['remaining']
        self.deck_remaining = self.card_json['remaining']
        self.cards = self.card_json["cards"]
        self.card_count += count
        self.card_list = [(item["value"], item["suit"].lower()) for item in self.cards]

    def __str__(self):
        # corrrect grammer for single card
        return f'You drew {self.card_count} cards and you have {self.deck_remaining} cards remaining in your deck.'

    @property
    def show_cards(self):
        return 'You drew ' + ', '.join(f"the {card[0]} of {card[1]}" for card in self.card_list)
