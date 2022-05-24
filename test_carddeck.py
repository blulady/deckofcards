import pytest
from classes_sandbox import CardDeck


def test_card_deck_response(deck):
    assert deck.deck["success"] is True
    assert isinstance(deck.deck_id, str) is True
    assert deck.deck_remaining == 52
    assert deck.count == 1


def test_two_decks_remaining(two_decks):
    assert two_decks.deck["success"] is True
    assert isinstance(two_decks.deck_id, str) is True
    assert two_decks.deck_remaining == 104
    assert two_decks.count == 2


def test_nineteen_decks(nineteen):
    assert nineteen.deck["success"] is True
    assert isinstance(nineteen.deck_id, str) is True
    assert nineteen.deck_remaining == 988
    assert nineteen.count == 19


def test_count_word_raises():
    match_regex = ".* is not a number, you need to enter a number for count"
    with pytest.raises(AssertionError, match=match_regex):
        CardDeck("Word")


def test_count_0_raises():
    # with pytest.raises(AssertionError) as exc_info:
    #     CardDeck(0)
    #     expected = "tomato tomato "
    #     msg = exc_info.value.args[0]
    #     assert expected == msg
    #     print(msg)
    #next 2 lines work
    with pytest.raises(AssertionError, match='You will need a whole integer of at least 1 for count'):
        CardDeck(0)
    #the following four lines also works
    # with pytest.raises(AssertionError) as exc_info:
    #     raise CardDeck(0)
    # assert exc_info.type is AssertionError
    # assert exc_info.value.args[0] == 'You will whole integer of at least 1 for count'


#write tests to test the assertion error for line 8/9 in carddeck
#write test to test str & repr output
#write test to
#reorganize tests
#test to see if the repr returns the correct count
#write a test
#create a mock to test non 200 responses