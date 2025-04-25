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

### Encrypt a Message

Run the following command to encrypt a plaintext message:

```bash
python coordExec.py --mode encrypt --message "Hello World"
```

### Decrypt a Message

To decrypt a message (provide coordinate pairs as the input):

```bash
python coordExec.py --mode decrypt --message "0,1 1,2 2,3 ..."
```

> **Note:** The exact coordinate format expected will depend on how the encryption output is structured.

## Future Plans

- Add support for customizable grid layouts and alphabets
- Implement a GUI for interactive encryption/decryption
- Support batch file encryption
- Add unit tests and improve error handling
- Include support for punctuation and non-alphabetic characters
