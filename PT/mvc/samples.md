# Exemplo MVC

Para explicar a implementação de uma aplicação de calculadora simples usando o padrão MVC (Model-View-Controller), vamos detalhar cada componente do padrão e as decisões de projeto envolvidas. A implementação será feita em Python usando a biblioteca Tkinter para criar uma aplicação desktop.

## Estrutura do Projeto:  
- Modelo (Model): Gerencia os dados e a lógica da calculadora.
- Visão (View): Responsável pela interface do usuário.
- Controlador (Controller): Interpreta as entradas do usuário e atualiza o modelo e a visão.

## Implementação
### Modelo (Model)
O modelo é responsável por manter o estado da aplicação e realizar cálculos. Ele não interage diretamente com a interface do usuário.

```python
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
        except Exception:
            self.expression = ""
            return "Error"

    def clear_expression(self):
        self.expression = ""
```

### Visão (View)
A visão é responsável por apresentar a interface ao usuário e capturar suas interações. No Tkinter, usamos widgets para criar a interface gráfica.

```python
import tkinter as tk

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
```

### Controlador (Controller)
O controlador recebe as entradas do usuário da visão e as processa através do modelo. Ele atua como um intermediário entre a visão e o modelo.

```python
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
```

### Main
A função principal inicializa o modelo, a visão e o controlador, e inicia o loop principal da interface gráfica.

```python
if __name__ == "__main__":
    root = tk.Tk()
    model = CalculatorModel()
    view = CalculatorView(root)
    controller = CalculatorController(model, view)
    root.mainloop()
```

### Explicação
- Separação de Responsabilidades: O padrão MVC pode ser escolhido para separar claramente a lógica de negócios (modelo), a interface do usuário (visão) e a lógica de controle (controlador). Isso facilita a manutenção e evolução do código.