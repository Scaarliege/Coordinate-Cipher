# Coordinate Cipher

## How It Works

This cipher is based on a couple of very old ciphers, namely the Vigenere and Polybius Square, but differers from those two in the way its set up

### Encryption

1. First you make a grid that is 26 by 26 and looks like  (we'll use a-z for this example)

   A B C ... Z<br>
   B A B<br>
   C B A<br>
   ...<br>
   Z
   > You can randomly shuffle this a-z key to make a new key so a-z is not the only option

3. Second you select any instance of the letter you're trying to encrypt (for this example we will use the letter "A")

   A B C ... Z<br>
   B **A** B<br>
   C B A<br>
   ...<br>
   Z

4. Third you derive the x-most and y-most points corresponding to your letter

   A **B** C ... Z<br>
   **B** A B<br>
   C B A<br>
   ...<br>
   Z

   in our case these points are B and B so A = BB
### Decryption

1. Setup your grid using the key (we'll use a-z for this example):
   
   A B C ... Z<br>
   B A B<br>
   C B A<br>
   ...<br>
   Z

2. Get your two letter string and locate them in the key (in this case we'll use "BB"):
   
   A **B** C ... Z<br>
   **B** A B<br>
   C B A<br>
   ...<br>
   Z
   > The first letter corresponds to the x position and the second letter corresponds to the y

3. Find the crossing point of those two letters:

   A B C ... Z<br>
   B **A** B<br>
   C B A<br>
   ...<br>
   Z
   
### Key Image:

![Screenshot_20250425-143123](https://github.com/user-attachments/assets/7d143468-51d1-47a1-a949-e1c0a3ce5f73)

## How to Use

### Prerequisites

- Python 3.x installed on your machine

### Clone the Repository

```bash
git clone https://github.com/Scaarliege/Coordinate-Cipher.git
```

### Run The Program:

```bash
python CoordExec
```

## Future Plans

- Implement a GUI for interactive encryption/decryption
- Support batch file encryption
- Add unit tests and improve error handling
