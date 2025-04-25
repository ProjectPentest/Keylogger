# Inhaltsverzeichnis / Table of Contents
- [Keylogger 🇩🇪](#deutsch-)
- [Keylogger 🇬🇧](#english-)

---

# Keylogger 🇩🇪

Ein einfacher Keylogger, der in Python unter Verwendung der Bibliothek 'pynput' geschrieben wurde. Dieser Python-Keylogger demonstriert, wie Tastenanschläge erfasst und in einer Datei ('keyfile.txt') protokolliert werden können. Innerhalb des Skripts werden spezielle Tasten (wie 'Enter', 'Tab' und Modifikatortasten wie 'Strg' und 'Shift') besonders behandelt, um die Ausgabe lesbarer zu machen und ein Beispiel für ereignisgesteuerte Programmierung zu geben.

## Ethische Erwägungen und rechtliche Hinweise

⚠️ **Wichtig**: Dieses Projekt ist ausschließlich für pädagogische Zwecke bestimmt und sollte nur in kontrollierten Umgebungen mit Zustimmung aller Beteiligten verwendet werden. Unerlaubtes Keylogging ist illegal und unethisch.

## Features

- **Tastenanschläge werden aufgezeichnet**: Protokolliert jeden Tastendruck in einem Puffer
- **Sondertastenbehandlung**: Enthält Belegungen für Sondertasten wie 'Enter', 'Tab', 'Backspace' und Modifikatortasten ('Strg', 'Shift', etc.).
- **Steuerung der Protokollierung**: Stoppt die Protokollierung, wenn der Benutzer eine vordefinierte Tastenkombination drückt ('Strg + Alt + Entf').
- **Gepufferte Protokollierung**: Puffert Tastenanschläge und schreibt sie in eine Datei, wenn bestimmte Tasten gedrückt werden ('Enter' oder 'Tab').

## Gelernte Fähigkeiten
- Verständnis der ereignisgesteuerten Programmierung und der Behandlung von Tastenereignissen.
- Beherrschung der Verwendung von Python-Bibliotheken wie „pynput“ zur Erfassung von Tastatureingaben.
- Kenntnis spezieller Tastenhandhabungs- und Protokollierungsmechanismen.
- Vertrautheit mit dem Schreiben von und dem Anhängen an Dateien zur Protokollierung von Daten.
- Bewusstsein für die ethischen und rechtlichen Implikationen von Keylogging-Software.

## Verwendete Tools

- Python 3.13.2 für die Implementierung des Keyloggers.
- pynput-Bibliothek zum Abhören von Tastaturereignissen und zur Verarbeitung von Tastendrücken.
- VSCode zum Codieren und Testen.

## Vorgehensweise

1. Repository klonen:

```bash
git clone https://github.com/ProjectPentest/Keylogger.git
cd Keylogger
```

2. Erstellen und aktivieren der virtuellen Umgebung (Windows):

```python
python -m venv .venv
.venv/Scripts/activate
```

3. Keylogger-Skript starten:

```python
python keylogger.pyw
```

4. Beenden des Keyloggers:

   Drücken Sie `Strg + Alt + Entf`.

5. Prüfen der Aufzeichnungen:

   Prüfen Sie „keyfile.txt“ im aktuellen Verzeichnis, um die protokollierten Tastenanschläge zu sehen.

## Potenzielle Erweiterungen und Möglichkeiten

Im Folgenden werden hypothetische Möglichkeiten aufgezeigt, was geändert werden könnte. Der Fokus dieser Änderungen liegt immer auf dem ethischen Teil der Erkennung dieser Mechanismen und wie man verhindern kann, dass diese Mechanismen ausgenutzt werden.

1. Versenden von Logdateien per E-Mail/ HTTP POST-Request
   - Implementieren Sie eine Funktion, bei der Protokolle an eine vordefinierte E-Mail Adresse/einen
     Remote-Server gesendet werden, anstatt in eine Datei geschrieben zu werden
   - Gewährleistung einer sicheren Übertragung
2. Datenverschlüsselung und Sicherheit
   - Tastenanschläge könnten verschlüsselt werden, bevor sie gespeichert oder übertragen werden.
  
## Beispiel Screenshots:

**Ref 1: Beispielhafte Ausgabe der Logdatei des Keyloggers**

![Keylogger Output](https://i.imgur.com/UAr31dR.png)

---

# Keylogger 🇬🇧

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

**Ref 1: Example Output from the Keylogger**

![Keylogger Output](https://i.imgur.com/UAr31dR.png)
