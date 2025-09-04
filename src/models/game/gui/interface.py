"""GUI interface for Draw of Faith game."""

import tkinter as tk
from tkinter import messagebox
from ..models.card import FusionCard
from ..models.player import Player
from ..game.deck import create_deck


class DrawOfFaithGUI:
    """Main GUI class for the Draw of Faith game."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Draw of Faith")
        self.root.geometry("800x600")
        
        # Game state
        self.deck = create_deck()
        self.player = Player("Jakub")
        self.ai = Player("AI", is_ai=True)
        self.turn = 1
        
        # Initialize hands
        for _ in range(5):
            self.player.draw_card(self.deck)
            self.ai.draw_card(self.deck)
        
        self._build_layout()
        self.render_all()
    
    def _build_layout(self):
        """Create the main GUI layout."""
        # AI Field
        self.ai_field_frame = tk.LabelFrame(
            self.root, text="AI Field", padx=10, pady=5
        )
        self.ai_field_frame.pack(pady=5)
        
        # Middle section with fusion zone and graveyards
        self.middle_frame = tk.Frame(self.root)
        self.middle_frame.pack()
        
        self.fusion_frame = tk.LabelFrame(
            self.middle_frame, text="Fusion Zone", padx=10, pady=5
        )
        self.fusion_frame.grid(row=0, column=0, padx=10)
        
        self.ai_graveyard_frame = tk.LabelFrame(
            self.middle_frame, text="AI Graveyard", padx=10, pady=5
        )
        self.ai_graveyard_frame.grid(row=0, column=1, padx=10)
        
        self.player_graveyard_frame = tk.LabelFrame(
            self.middle_frame, text="Player Graveyard", padx=10, pady=5
        )
        self.player_graveyard_frame.grid(row=0, column=2, padx=10)
        
        # Player Field
        self.player_field_frame = tk.LabelFrame(
            self.root, text="Player Field", padx=10, pady=5
        )
        self.player_field_frame.pack(pady=5)
        
        # Player Hand
        self.hand_frame = tk.LabelFrame(
            self.root, text="Your Hand", padx=10, pady=5
        )
        self.hand_frame.pack(pady=5)
        
        # Status and info
        self._create_status_widgets()
        
        # Combo log
        self.combo_log = tk.Text(
            self.root, height=6, width=60, state='disabled', bg="#f0f0f0"
        )
        self.combo_log.pack(pady=10)
    
    def _create_status_widgets(self):
        """Create status display widgets."""
        self.status = tk.Label(
            self.root, text="Your Turn", font=("Arial", 14)
        )
        self.status.pack()
        
        self.score_label = tk.Label(
            self.root, text="Score: Jakub 0 - AI 0", font=("Arial", 12)
        )
        self.score_label.pack()
        
        self.turn_label = tk.Label(
            self.root, text="Turn: 1", font=("Arial", 12)
        )
        self.turn_label.pack()
    
    def render_all(self):
        """Render all game zones."""
        self.render_zone(self.ai_field_frame, self.ai.field, "red")
        self.render_zone(self.player_field_frame, self.player.field, "blue")
        self.render_zone(self.hand_frame, self.player.hand, "white", clickable=True)
        self.render_zone(self.ai_graveyard_frame, self.ai.graveyard, "gray")
        self.render_zone(self.player_graveyard_frame, self.player.graveyard, "gray")
    
    def render_zone(self, frame, cards, color, clickable=False):
        """Render cards in a specific zone."""
        # Clear existing widgets
        for widget in frame.winfo_children():
            widget.destroy()
        
        # Create card labels
        for i, card in enumerate(cards):
            bg_color = "gold" if isinstance(card, FusionCard) else color
            
            lbl = tk.Label(
                frame,
                text=str(card),
                bg=bg_color,
                fg="black",
                font=("Arial", 12),
                width=10,
                relief="raised",
                borderwidth=2
            )
            
            if clickable:
                lbl.bind("<Button-1>", lambda e, i=i: self.summon_card(i))
                lbl.config(cursor="hand2")
            
            lbl.pack(side=tk.LEFT, padx=5)
    
    def summon_card(self, index):
        """Handle player summoning a card."""
        if index < len(self.player.hand):
            card = self.player.hand.pop(index)
            self.player.field.append(card)
            self.status.config(text=f"You summoned {card}")
            self.render_all()
            self.root.after(1000, self.ai_turn)
    
    def ai_turn(self):
        """Handle AI turn."""
        action, cards = self.ai.summon()
        self.status.config(text=f"AI performed {action}!")
        self.log_combo("AI", action, cards)
        self.render_all()
        self.root.after(1500, self.battle)
    
    def log_combo(self, player_name, fusion_type, cards):
        """Log fusion/combo actions to the combo log."""
        self.combo_log.config(state='normal')
        card_names = ', '.join(str(c) for c in cards)
        log_entry = f"Turn {self.turn}: {player_name} activated {fusion_type} with {card_names}\n"
        self.combo_log.insert(tk.END, log_entry)
        self.combo_log.see(tk.END)
        self.combo_log.config(state='disabled')
    
    def battle(self):
        """Handle battle phase."""
        result = self.player.battle(self.ai)
        self._update_score_display()
        self.turn += 1
        self.turn_label.config(text=f"Turn: {self.turn}")
        
        messagebox.showinfo("Battle", result)
        self.render_all()
        self.check_game_end()
    
    def _update_score_display(self):
        """Update the score display."""
        self.score_label.config(
            text=f"Score: Jakub {self.player.points} - AI {self.ai.points}"
        )
    
    def check_game_end(self):
        """Check if the game has ended."""
        if not self.player.hand and not self.ai.hand:
            if self.player.points > self.ai.points:
                winner = "Jakub"
            elif self.ai.points > self.player.points:
                winner = "AI"
            else:
                winner = "It's a tie!"
            
            messagebox.showinfo("Game Over", f"{winner} wins the duel!")
            self.root.quit()
        else:
            # Continue game - player draws if possible
            if self.deck:
                self.player.draw_card(self.deck)
                if self.deck:
                    self.ai.draw_card(self.deck)
            self.status.config(text="Your Turn")


def main():
    """Main function to run the game."""
    root = tk.Tk()
    app = DrawOfFaithGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
