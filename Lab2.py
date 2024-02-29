import tkinter as tk
from tkmacosx import Button



class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Apple Calculator")

        # Entry widget to display the result
        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.result_entry = tk.Entry(root, textvariable=self.result_var, font=('Helvetica', 36), bd=1, insertwidth=4, width=20, justify='right', bg='gray17')
        self.result_entry.grid(row=0, column=0, columnspan=4)

        # Buttons layout
        buttons = [
            ('C', 'DarkOrange1'), ('+/-', 'darkorange1'), ('%', 'darkorange1'), ('/', 'darkorange1'),
            ('7', 'cyan'), ('8', '#d4d4d2'), ('9', '#d4d4d2'), ('*', 'darkorange1'),
            ('4', '#d4d4d2'), ('5', '#d4d4d2'), ('6', '#d4d4d2'), ('-', 'darkorange1'),
            ('1', '#d4d4d2'), ('2', '#d4d4d2'), ('3', '#d4d4d2'), ('+', 'DarkOrange1'),
            ('0', '#d4d4d2'), ('.', '#d4d4d2'), ('=', 'darkorange1')
        ]
        button_color = 'cyan'
        row_val = 1
        col_val = 0

        for button_text, button_color in buttons:
            btn = tk.Button(root, text=button_text, padx=20, pady=20, font=('Helvetica', 18), command=lambda b=button_text: self.on_button_click(b), bg = button_color, fg = 'black')
            btn.grid(row=row_val, column=col_val, sticky="nsew")

            
            col_val += 1

            if col_val > 3:
                col_val = 0
                row_val += 1

            # Configure row and column weights for resizing
            root.grid_rowconfigure(row_val, weight=1)
            root.grid_columnconfigure(col_val, weight=1)

    def on_button_click(self, value):
        if value == '=':
            self.calculate_result()
        elif value == 'C':
            self.clear_result()
        elif value == '+/-':
            self.negate_result()
        elif value == '%':
            self.calculate_percentage()
        else:
            self.append_to_result(value)

    def append_to_result(self, value):
        current_result = self.result_var.get()

        # Check for consecutive operators
        if value in "+-*/" and current_result[-1] in "+-*/":
            return

        # Check for leading zero
        if current_result == "0":
            self.result_var.set(value)
        else:
            self.result_var.set(current_result + value)

    def clear_result(self):
        self.result_var.set("0")

    def negate_result(self):
        current_result = self.result_var.get()
        if current_result != "0":
            if current_result[0] == '-':
                self.result_var.set(current_result[1:])
            else:
                self.result_var.set('-' + current_result)

    def calculate_percentage(self):
        current_result = self.result_var.get()
        try:
            result = str(float(current_result) / 100)
            self.result_var.set(result)
        except ValueError:
            self.result_var.set("Error")

    def calculate_result(self):
        current_result = self.result_var.get()
        try:
            result = str(eval(current_result))
            self.result_var.set(result)
        except ZeroDivisionError:
            self.result_var.set("Error")
        except Exception as e:
            self.result_var.set("Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()