import coordLib as cl

def menu():
    print("---------------")
    print("1: Encrypt\n")
    print("2: Decrypt\n")
    print("3: Generate a New Key\n")
    print("4: Quit")
    print("---------------")
    def selection():
        global key
        inp = input("Select a menu option: ")
        if inp == "1":
            print(f"\nThe current key is:\n{key}")
            text = input("\nInput text to encrypt: ")
            encText = cl.enc(text, key)
            print(f"\nThe output is:\n{encText}")
        elif inp == "2":
            def main():
                inpKey = input('\nInput key (type "standard" or "stand" to use a-z): ')
                if inpKey.lower() == "standard" or inpKey.lower() == "stand":
                    inpKey = "abcdefghijklmnopqrstuvwxyz"
                elif len(inpKey) != 26:
                    print("\nSorry, thats not a valid key\n"), main()
                return inpKey
            inpKey = main()
            text = input("\nInput encrypted text: ")
            decText = cl.dec(text, inpKey)
            print(f"\nThe output is:\n{decText}")
        elif inp == "3":
            print(f"\nOld key was:\n{key}")
            newKey = cl.genkey(key)
            print(f"\nNew key is:\n{newKey}")
            key = newKey
        elif inp == "4":
            quit()
        else:
            print("\nSorry, thats not a valid menu option")
            print("---------------")
            selection()
    selection()
    menu()

print("Coordinate Cypher\nV 1.0\nBy: Oliver Daniel\nDefault key is a-z")
key = "abcdefghijklmnopqrstuvwxyz"
menu()