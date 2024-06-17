import tkinter as tk
from tkinter import ttk

class ModernCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)
        self.root.configure(bg="#2e2e2e")

        # Constants for styling
        self.BUTTON_STYLE = {
            'font': ("Helvetica", 18),
            'padding': 10,
            'borderwidth': 0,
            'relief': "flat"
        }
        self.COLORS = {
            'bg': "#2e2e2e",
            'btn_bg': "#4f4f4f",
            'btn_fg': "#ffffff",
            'btn_active_bg': "#5a5a5a",
            'btn_pressed_bg': "#6b6b6b",
            'entry_bg': "#3e3e3e",
            'entry_fg': "#ffffff"
        }

        self.create_widgets()

    def create_widgets(self):
        # Create and style entry
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TEntry", foreground=self.COLORS['entry_fg'], background=self.COLORS['entry_bg'],
                        fieldbackground=self.COLORS['entry_bg'], borderwidth=0, font=("Helvetica", 18))
        style.configure("TButton", **self.BUTTON_STYLE, background=self.COLORS['btn_bg'], foreground=self.COLORS['btn_fg'])
        style.map("TButton", background=[('pressed', self.COLORS['btn_pressed_bg']), ('active', self.COLORS['btn_active_bg'])])

        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(self.root, textvariable=self.entry_var, style="TEntry", justify='right', validate='key')
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=20)
        self.entry.bind("<Return>", self.evaluate_expression)

        # Validation to allow only numbers and valid operators
        self.entry['validatecommand'] = (self.entry.register(self.validate_entry), '%P')

        # Button text and positions
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
            if i < 4:
                self.root.grid_columnconfigure(i, weight=1)

    def create_button(self, text, row, col):
        command = None
        if text == '=':
            command = self.evaluate_expression
        elif text == 'C':
            command = self.clear_entry
        else:
            command = lambda t=text: self.append_to_expression(t)

        btn = ttk.Button(self.root, text=text, command=command)
        btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)

    def evaluate_expression(self, event=None):
        try:
            expression = self.entry.get()
            result = eval(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, 'Error')

    def append_to_expression(self, char):
        current_text = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, current_text + char)

    def clear_entry(self):
        self.entry.delete(0, tk.END)

    def validate_entry(self, new_value):
        if new_value == "":
            return True
        allowed_chars = "0123456789+-*/()."
        for char in new_value:
            if char not in allowed_chars:
                return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ModernCalculator(root)
    root.mainloop()
