# src/__init__.py
"""
Draw of Faith - A Card Fusion Battle Game
"""

__version__ = "1.0.0"
__author__ = "Your Name"
__email__ = "your.email@example.com"

# src/models/__init__.py
"""
Game models for Draw of Faith.
"""

from .card import Card, FusionCard
from .player import Player

__all__ = ['Card', 'FusionCard', 'Player']

# src/game/__init__.py
"""
Game logic and mechanics for Draw of Faith.
"""

from .deck import create_deck, create_custom_deck, DeckManager

__all__ = ['create_deck', 'create_custom_deck', 'DeckManager']

# src/gui/__init__.py
"""
GUI components for Draw of Faith.
"""

from .interface import DrawOfFaithGUI

__all__ = ['DrawOfFaithGUI']

# tests/__init__.py
"""
Test suite for Draw of Faith.
"""
