import tkinter as tk

class CalculatorModel:
    def __init__(self):
        self.expression = ""

    def add_to_expression(self, value):
        self.expression += str(value)

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.expression = str(result)
            return result
        except Exception as e:
            self.expression = ""
            return "Error"

    def clear_expression(self):
        self.expression = ""

class CalculatorView:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.expression_field = tk.Entry(root, width=25, font=('Arial', 14))
        self.expression_field.grid(row=0, column=0, columnspan=4)
        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', 'C', '=', '+'
        ]
        row = 1
        col = 0
        for button in buttons:
            action = lambda x=button: self.button_click(x)
            tk.Button(self.root, text=button, width=5, height=2, command=action).grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def button_click(self, value):
        self.on_button_click(value)

    def set_on_button_click_listener(self, listener):
        self.on_button_click = listener

    def update_expression(self, expression):
        self.expression_field.delete(0, tk.END)
        self.expression_field.insert(tk.END, expression)

class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.set_on_button_click_listener(self.handle_button_click)

    def handle_button_click(self, value):
        if value == "=":
            result = self.model.evaluate_expression()
            self.view.update_expression(result)
        elif value == "C":
            self.model.clear_expression()
            self.view.update_expression("")
        else:
            self.model.add_to_expression(value)
            self.view.update_expression(self.model.expression)

if __name__ == "__main__":
    root = tk.Tk()
    model = CalculatorModel()
    view = CalculatorView(root)
    controller = CalculatorController(model, view)
    root.mainloop()