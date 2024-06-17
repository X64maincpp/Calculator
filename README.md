# Calculator

A sleek and modern calculator application built with Python and Tkinter. This project focuses on providing a clean and intuitive user interface while ensuring only valid mathematical expressions are allowed.

## Features

- **Minimalist Design**: The calculator has a modern and minimalist design with a dark theme.
- **Valid Input Only**: Ensures that only valid characters (numbers, operators, parentheses, and decimal points) are entered.
- **Responsive Layout**: The buttons and display resize smoothly with the window.
- **Keyboard Support**: Pressing Enter evaluates the expression.

## Technologies Used

- **Python**: The programming language used for developing the application.
- **Tkinter**: The standard GUI library for Python, used to create the user interface.

## How to Run

1. **Install Python**: Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Tkinter**: Tkinter usually comes with Python, but if you need to install it separately:
    - **Windows**: Typically included with Python installation.
    - **macOS**: Included with Python installation.
    - **Linux (Debian/Ubuntu)**: Install using the following commands:
      ```sh
      sudo apt update
      sudo apt install python3-tk
      ```

3. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/modern-calculator.git
    cd modern-calculator
    ```

4. **Run the Application**:
    ```sh
    python calculator.py
    ```

## Code Overview

The main code for the calculator is organized in a class for better structure and reusability. The `ModernCalculator` class handles the creation of the user interface, validation of input, and evaluation of expressions.

### Main Components

- **`__init__`**: Initializes the main window and calls the method to create widgets.
- **`create_widgets`**: Creates and styles the entry field and buttons.
- **`create_button`**: Helper method to create buttons with the appropriate command.
- **`evaluate_expression`**: Evaluates the mathematical expression entered by the user.
- **`append_to_expression`**: Appends a character to the current expression.
- **`clear_entry`**: Clears the entry field.
- **`validate_entry`**: Validates the input to ensure only valid characters are entered.

## Contributing

Feel free to fork the repository and submit pull requests. Any contributions to improve the project are welcome!

## Acknowledgments

- Thanks to the Python and Tkinter communities for providing excellent resources and support.

---

By following these instructions, you should be able to run and explore the Calculator project easily. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.
