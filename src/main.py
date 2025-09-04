"""
Draw of Faith - A Card Fusion Battle Game

Main entry point for the Draw of Faith game.
"""

import tkinter as tk
from gui.interface import DrawOfFaithGUI


def main():
    """Initialize and run the Draw of Faith game."""
    root = tk.Tk()
    
    # Configure root window
    root.resizable(True, True)
    root.minsize(800, 600)
    
    # Create and run the game
    app = DrawOfFaithGUI(root)
    
    try:
        root.mainloop()
    except KeyboardInterrupt:
        print("\nGame interrupted by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        root.quit()


if __name__ == "__main__":
    main()
