# Coordinate Cipher

## How It Works

Coordinate Cipher is a custom encryption method that maps characters to coordinate pairs on a grid, similar to the classic Polybius square cipher. The grid is defined with a specific layout, and each character in the message corresponds to a pair of coordinates representing its position in the grid.

The main logic is contained in `coordLib.py`, which handles both encryption and decryption. Characters are mapped to and from their respective coordinate representations, allowing reversible transformation of messages.

## How to Use

### Prerequisites

- Python 3.x installed on your machine

### Clone the Repository

```bash
git clone https://github.com/Scaarliege/Coordinate-Cipher.git
cd Coordinate-Cipher
```

### Run The Program:

```bash
python CoordExec
```

## Future Plans

- Implement a GUI for interactive encryption/decryption
- Support batch file encryption
- Add unit tests and improve error handling
