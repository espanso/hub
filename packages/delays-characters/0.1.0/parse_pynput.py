# Intended for use with the delays-characters package.yml file.
# Uses the Python pynput library to inject text, instead of Espanso. Enables the 
# addition of pauses (sleep) and <Tab> etc. keys and can include Espanso {{variables}}
# See https://pynput.readthedocs.io/en/latest/keyboard.html#controlling-the-keyboard
# Supports type, tap, press, release, and sleep

import argparse, time
try:
    from pynput.keyboard import Controller, Key
except ImportError:
    import sys
    print("Error: The 'pynput' library is not installed.", file=sys.stderr)
    print("Install it using: pip install pynput", file=sys.stderr)
    sys.exit(1)  # Exit with a non-zero status code to indicate failure


# Initialize the keyboard controller
keyboard = Controller()

def parse_and_execute_commands(commands):
    lines = commands.strip().splitlines()

    for line in lines:
        line = line.strip()
        if line.startswith('type'):
            text = line[len('type '):].strip()
            keyboard.type(text)
        
        elif line.startswith('tap'):
            key_name = line[len('tap '):].strip().lower()
            key = getattr(Key, key_name, key_name)
            keyboard.tap(key)
        
        elif line.startswith('press'):
            key_name = line[len('press '):].strip().lower()
            key = getattr(Key, key_name, key_name)
            keyboard.press(key)

        elif line.startswith('release'):
            key_name = line[len('release '):].strip().lower()
            key = getattr(Key, key_name, key_name)
            keyboard.release(key)
        
        elif line.startswith('sleep'):
            time_to_sleep = float(line[len('sleep '):].strip())
            time.sleep(time_to_sleep)

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Execute keyboard automation commands.")
    parser.add_argument('trig', type=str, help='The trigger key to simulate.')
    parser.add_argument('input', type=str, help='The input commands to execute.')
    args = parser.parse_args()

    # Press backspace key as many times as the length of the trigger
    for _ in args.trig: keyboard.tap(Key.backspace)

    # Parse and execute the input commands
    if args.input:
        parse_and_execute_commands(args.input)
    else:
        print("No input provided.")

    # Replace trigger for Espanso to remove after the script
    keyboard.type(args.trig)

if __name__ == "__main__":
    main()
