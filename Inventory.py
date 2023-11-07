import tkinter as tk
from tkinter import ttk, messagebox

class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry(f"{self.root.winfo_screenwidth()}x{self.root.winfo_screenheight()}+0+0")

        self.inventory = {
            'tomatoes': 20,
            'salad': 20,
            'wrap': 20,
            'tea': 20,
            'coffee': 20,
            'apple juice': 20,
            'meat': 20,
            'mayonnaise': 20,
        }

        self.setup_ui()

    def setup_ui(self):
        # Frames
        self.action_frame = ttk.Frame(self.root)
        self.action_frame.pack(side='top', fill='x')

        self.inventory_frame = ttk.Frame(self.root)
        self.inventory_frame.pack(fill='both', expand=True)

        # Buttons
        self.sell_wrap_button = ttk.Button(
            self.action_frame,
            text="Sell Wrap",
            command=lambda: self.sell_product('wrap')
        )
        self.sell_wrap_button.pack(side='left', padx=10, pady=10)

        self.sell_tea_button = ttk.Button(
            self.action_frame,
            text="Sell Tea",
            command=lambda: self.sell_product('tea')
        )
        self.sell_tea_button.pack(side='left', padx=10, pady=10)

        self.sell_coffee_button = ttk.Button(
            self.action_frame,
            text="Sell Coffee",
            command=lambda: self.sell_product('coffee')
        )
        self.sell_coffee_button.pack(side='left', padx=10, pady=10)

        self.sell_juice_button = ttk.Button(
            self.action_frame,
            text="Sell Apple Juice",
            command=lambda: self.sell_product('apple juice')
        )
        self.sell_juice_button.pack(side='left', padx=10, pady=10)

        # Suggestions button
        self.suggestions_button = ttk.Button(
            self.action_frame,
            text="See Suggestions",
            command=self.show_suggestions
        )
        self.suggestions_button.pack(side='left', padx=10, pady=10)

        # Inventory display
        self.update_inventory_display()

    def sell_product(self, product):
        # Special case for selling wraps
        if product == 'wrap':
            required_ingredients = {'tomatoes': 0.5, 'salad': 0.1, 'meat': 0.001, 'mayonnaise': 0.001}
            if all(self.inventory[ingredient] >= required_ingredients[ingredient] for ingredient in required_ingredients):
                for ingredient, quantity in required_ingredients.items():
                    self.inventory[ingredient] -= quantity
                self.inventory['wrap'] -= 1  # Assuming selling one wrap
            else:
                messagebox.showerror("Error", "Not enough ingredients for a wrap!")
                return
        else:  # For tea, coffee, and apple juice
            if self.inventory[product] > 0:
                self.inventory[product] -= 1  # Selling one unit
            else:
                messagebox.showerror("Error", f"{product.title()} is sold out!")
                return

        # Update display and check for low inventory
        self.update_inventory_display()
        if self.inventory[product] <= 10:
            messagebox.showwarning("Warning", f"Low inventory on {product}. Please restock!")

    def update_inventory_display(self):
        for widget in self.inventory_frame.winfo_children():
            widget.destroy()

        for product, quantity in self.inventory.items():
            label = ttk.Label(self.inventory_frame, text=f"{product.title()}: {quantity:.3f} units")
            label.pack()

    def show_suggestions(self):
        suggestions_window = tk.Toplevel(self.root)
        suggestions_window.title("Restock Suggestions")
        suggestions_window.geometry("400x400")  # Set the suggestions window size

        for product, quantity in self.inventory.items():
            if quantity <= 30:  # Considered 30 units as the threshold
                suggestion_label = ttk.Label(suggestions_window, text=f"Consider restocking {product.title()}")
                suggestion_label.pack()

def main():
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
é
