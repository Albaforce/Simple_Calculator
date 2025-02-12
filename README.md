# PyQt6 Calculator Application

## Overview
This is a modern calculator application built with PyQt6, featuring both standard and scientific calculation modes. The application provides a user-friendly interface with a clean, modern design and responsive buttons.

## Features

### Standard Mode
- Basic arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (×)
  - Division (÷)
- Clear function
- Decimal number support

### Scientific Mode
- All standard mode features
- Advanced mathematical operations:
  - Trigonometric functions (sin, cos)
  - Square root (√)
  - Power (^)
- Prefix operations (sin, cos, √) work in the format: operation followed by number

## Requirements
- Python 3.x
- PyQt6

## Installation

1. Make sure you have Python installed on your system
2. Install PyQt6 using pip:
```bash
pip install PyQt6
```

## Running the Application
1. Save the calculator code in a file (e.g., `calculator.py`)
2. Run the application:
```bash
python calculator.py
```

## Usage Instructions

### Basic Usage
1. Launch the application
2. Use the mode selector at the top to switch between Standard and Scientific modes
3. Click number buttons to input values
4. Click operation buttons to perform calculations
5. Click '=' to see the result
6. Click 'clear' to reset the calculator

### Standard Mode Operations
- Enter first number
- Select operation (+, -, ×, ÷)
- Enter second number
- Press '=' for result

### Scientific Mode Operations
For regular operations (+, -, ×, ÷):
- Same as Standard mode

For prefix operations (sin, cos, √):
1. Click the operation button (sin, cos, or √)
2. Enter the number
3. Result is calculated automatically

## Features Details

### UI Elements
- Mode selector dropdown
- Digital display
- Numeric keypad (0-9)
- Operation buttons
- Clear button
- Equals button

### Styling
- Modern dark theme
- Color-coded buttons:
  - Light gray for numbers
  - Blue for operations
- Rounded button corners
- Hover effects on buttons

## Error Handling
The calculator includes error handling for:
- Division by zero
- Invalid operations
- Malformed expressions
- Complex number results

## Project Structure
```
calculator.py
├── Calculator class (main application)
│   ├── Standard calculator implementation
│   ├── Scientific calculator implementation
│   └── Operation handling methods
└── Main execution block
```

## Future Enhancements
Potential improvements could include:
- Memory functions (M+, M-, MR, MC)
- History panel for past calculations
- Additional scientific functions (tan, log, etc.)
- Keyboard input support
- Copy/paste functionality

## Contributing
Feel free to fork this project and submit pull requests for any improvements or bug fixes.

## License
This project is available for free use and modification.

## Support
For issues or questions, please create an issue in the project repository.
