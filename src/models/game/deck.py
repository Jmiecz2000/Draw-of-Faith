"""Deck creation and management for Draw of Faith game."""

import random
from ..models.card import Card


def create_deck():
    """Create and shuffle a standard 52-card deck."""
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    
    deck = [Card(rank, suit) for suit in suits for rank in ranks]
    random.shuffle(deck)
    return deck


def create_custom_deck(suits=None, ranks=None, shuffle=True):
    """Create a custom deck with specified suits and ranks."""
    if suits is None:
        suits = ['♠', '♥', '♦', '♣']
    if ranks is None:
        ranks = ['A', 'K', 'Q', 'J', '10', '9', '8', '7', '6', '5', '4', '3', '2']
    
    deck = [Card(rank, suit) for suit in suits for rank in ranks]
    
    if shuffle:
        random.shuffle(deck)
    
    return deck


class DeckManager:
    """Manages deck operations and statistics."""
    
    def __init__(self, deck=None):
        self.deck = deck if deck is not None else create_deck()
        self.original_size = len(self.deck)
    
    def draw(self):
        """Draw a card from the deck."""
        return self.deck.pop() if self.deck else None
    
    def cards_remaining(self):
        """Get number of cards remaining in deck."""
        return len(self.deck)
    
    def is_empty(self):
        """Check if deck is empty."""
        return len(self.deck) == 0
    
    def shuffle(self):
        """Shuffle the current deck."""
        random.shuffle(self.deck)
    
    def peek_top(self, n=1):
        """Peek at the top n cards without removing them."""
        return self.deck[-n:] if n <= len(self.deck) else self.deck[:]
    
    def add_card(self, card):
        """Add a card to the bottom of the deck."""
        self.deck.insert(0, card)
    
    def reset(self):
        """Reset to a fresh shuffled deck."""
        self.deck = create_deck()
        self.original_size = len(self.deck)
