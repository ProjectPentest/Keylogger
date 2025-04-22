# Keylogger-Detection

A simple keylogger written in python using the 'pynput' library. This Python Keylogger demonstrates how to capture and log keystrokes into a file ('keyfile.txt'). Within the script special keys (like 'Enter', 'Tab', and modifier keys like 'Ctrl' and 'Shift') are handled specially to make the output more human readable and provides an example of event-driven programming.

## Ethical Considerations and Legal Warning

⚠️ **Important**: This project is intended solely for educational purposes and should only be used in controlled environments with the proper consent of all parties involved. Unauthorized keylogging is illegal and unethical.

## Features

- **Key pressures captured**: Logs each key press to a buffer
- **Special key handling**: Includes mappings for special keys like 'Enter', 'Tab', 'Backspace' and modifier keys ('Ctr', 'Shift', etc.).
- **Logging control**: Stops logging when the user presses a predefined combination of keys ('Ctrl + Alt + Delete').
- **Buffered logging**: Buffer key presses and write them into a file when specific keys are pressed ('Enter' or 'Tab').

## Skills Learned

- Understanding of event-driven programming and key event handling.
- Proficiency in using Python libraries like 'pynput' for capturing keyboard input.
- Knowledge of special key handling and logging mechanisms.
- Familiarity with writing and appending to files for logging data.
- Awareness of ethical and legal implications of keylogging software.

## Tools Used

- Python 3.13.2 for the implementation of the keylogger.
- pynput library for listening to keyboard events and handling keypresses.
- VSCode for coding and testing.

## Steps

1. Clone the repository:

```bash
git clone https://github.com/ProjectPentest/Keylogger.git
cd Keylogger
```

2. Create and activate virtual environment (Windows):

```python
python -m venv .venv
.venv/Scripts/activate
```

3. Run the keylogger script:

```python
python keylogger.pyw
```

4. Exit the Keylogger:

   Press `Ctrl + Alt + Delete`

5. Check the logs:

   Check 'keyfile.txt' in the current directory to view the logged keystrokes.

## Potential Enhancements and Possibilities

The following are theoretical possibilities on what could be changed. The focus of these changes is always the ethickal part on detecting these prevention mechanisms and how to prevent tools from exloiting these.

1. Sending Logs via Email/ HTTP POST request
   - Implement a feature where logs are sent to a predefined email address/
     remote server instead of being written to a file
   - Ensure secure transmission
2. Data Encryption and Security
   - keystrokes could be encrypted before being stored or transmitted.

## Example Screenshots:

Ref1: Keylogger Output File
![Logged Keyfile Output](https://imgur.com/a/hASoyv7)
