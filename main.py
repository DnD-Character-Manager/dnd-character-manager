import sys

quit_list = ["quit", "q", "exit"]

def main():
    print("Welcome to the DnD Character Manager! Type 'quit' to exit.")
    while True:
        try:
            main_loop()
        except KeyboardInterrupt:
            print("\nDetected keyboard interrupt. Exiting gracefully.")
            break
        except EOFError:
            print("\nEOF detected. Exiting.")
            break

def check_exit(user_input):
    if user_input.lower() in quit_list:
        print("Exiting the DnD Character Manager. Goodbye!")
        sys.exit()

def load_characters():
    print("Loading existing characters...")
    # Add logic to load characters here

def create_character():
    print("Creating a new character...")
    # Add logic to create a new character here

def main_loop():
    while True:
        user_input = input("What would you like to do:\n1 - Load existing characters.\n2 - Create a new character.\n> ")
        check_exit(user_input)
        match user_input:
            case "1":
                load_characters()
                break
            case "2":
                create_character()
                break
            case _:
                print("Invalid input. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
