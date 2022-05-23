import requests


class CardDeck:
    """a class so we can check the accuracy of remaining cards in a deck
    count is the number of decks we want to pull"""
    def __init__(self, count=1):
        assert isinstance(count, int), f"{count} is not a number, you need to enter a number for count"
        assert count > 0, 'You will need a whole integer of at least 1 for count'
        self.count = count
        response = requests.get(f"https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={count}")
        if response.status_code != 200:
            raise(SystemError, f"Unable to access api. Code: {response.status_code}")
        if not response.json()["success"]:
            raise Exception("You pulled too many decks, the number of decks you can pull is 20")
        # write an except method
        self.deck = response.json()
        self.deck_id = self.deck["deck_id"]
        self.deck_remaining = self.deck["remaining"]
        self.deck_shuffled = self.deck["shuffled"]
        self.card_count = 0
        self.card_list = []
        self.card_json = {}
        self.cards = []

    def __str__(self):
        return f'You drew {self.card_count} cards and you have {self.deck_remaining} cards remaining in your deck.'

    def __repr__(self):
        return f'CardDeck({self.count})'

    def draw_cards(self, count):
        """count is the number of cards you want to draw
        returns the json for the cards you drew from the deck"""
        card_response = requests.get(f"https://deckofcardsapi.com/api/deck/{self.deck_id}/draw/?count={count}")
        self.card_json = card_response.json()
        self.deck_remaining = self.card_json["remaining"]
        self.cards = self.card_json["cards"]
        self.card_count += count
        self.card_list = [(item["value"], item["suit"].lower()) for item in self.cards]

    @property
    def show_cards(self):
        return 'You drew ' + ', '.join(f"the {card[0]} of {card[1]}"for card in self.card_list)



    
