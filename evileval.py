#evileval.py 
import os
import shutil

def welcome():
    os.system('clear')
    print("\033[1;31;40m") # Red colored ANSI text
    print("********************************")
    print("*********** EVIL-EVAL **********")
    print("********************************")
    print("\033[0;37;40m") # Reset to default text color

def evil_eval():
    print("\033[1;31;40m") # Red colored ANSI text
    print("********* Let's see how evil **********")
    print("\033[0;37;40m") # Reset to default text color

    text = input("Enter your text: ")
    reversed_text = text[::-1] # Reverse the input text

    print("\nReversed Text: ")
    print(reversed_text)

    # Write the reversed text into a file
    with open('reversed_text.txt', 'w') as f:
        f.write(reversed_text)

    print("\nThe reversed text has been saved to 'reversed_text.txt'.")

    # Ask the user for a location to move the file
    new_location = input("\nEnter the directory to move 'reversed_text.txt' to (or leave blank to keep it here): ")

    if new_location:
        try:
            shutil.move('reversed_text.txt', new_location)
            print("\nThe file has been moved to the specified directory.")
        except Exception as e:
            print(f"\nAn error occurred while moving the file: {e}")

def main():
    while True:
        welcome()
        evil_eval()
        
        # Ask the user if they want to continue
        continue_choice = input("\nDo you want to continue? (Y/N): ").lower()
        if continue_choice != 'y':
            break

if __name__ == "__main__":
    main()
