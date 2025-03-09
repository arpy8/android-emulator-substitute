# Python Android Emulator Alternative for Expo App Development

A lightweight Python-based Android emulator alternative for developing and testing Expo apps.

## Example Usage
![alt text](misc/image.png)

## Installation

### Prerequisites
Ensure you have the following installed:
- Python (>=3.7)
- Node.js & Expo CLI
- Eel (for UI integration)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/arpy8/android-emulator-substitute.git
   cd android-emulator-substitute
   ```
2. Install dependencies:
   ```bash
   pip install eel
   ```
3. Start the emulator:
   ```bash
   python main.py
   ```

## Usage
1. Run your Expo project in development mode:
   ```bash
   expo start
   ```
2. Launch the emulator using 
    ```python
    python main.py
    ```
3. Connect the Expo app to the emulator.

## Command-line Arguments
The emulator supports the following flags:
- `-p`, `--port` : Set the port number (default: `8081`).
- `-d`, `--device` : Specify the device to emulate (default: `iphone-11`).
- `-l`, `--list-devices` : List all available devices.
