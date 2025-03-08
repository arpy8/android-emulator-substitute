import os
import eel
import argparse
from constants import dimensions


def start_app(port=8081, device="iphone-11", html_file_path="emulator.html"):
    width = dimensions[device]["width"]
    height = dimensions[device]["height"]
    
    print(f"Starting app with device: {device}, dimensions: {width}x{height}")
    
    html_dir = os.path.dirname(os.path.abspath(html_file_path))
    html_filename = os.path.basename(html_file_path)
    
    eel.init(html_dir)
    eel.start(html_filename, 
              mode='chrome',
              port=2907,
              block=True,
              cmdline_args=[
                  f'--app=http://localhost:{port}',
                  '--new-window',
                  '--disable-features=RendererAppWindow',
                  f'--window-size={width},{height}',
                  '--window-position=center'
              ],
              size=(width, height))
    
def main():
    parser = argparse.ArgumentParser(description="A lightweight Python-based Android emulator alternative for developing and testing Expo apps.")
    parser.add_argument("-p", "--port", type=int, default=8081, help="Port number to run the server on.")
    parser.add_argument("-d", "--device", type=str, default="iphone-11", help="Specify the device to emulate.")
    parser.add_argument("-f", "--html-file", type=str, default="emulator.html", help="Path to your HTML file.")
    parser.add_argument("-l", "--list-devices", action="store_true", help="List all available devices.")

    args = parser.parse_args()
    
    if args.list_devices:
        print("Available devices:")
        for device in dimensions.keys():
            print(f"  {device}: {dimensions[device]['width']}x{dimensions[device]['height']}")
        return
    
    if args.device not in dimensions:
        print(f"Error: Unknown device '{args.device}'")
        print("Use --list-devices to see available options")
        return
    
    start_app(args.port, args.device, args.html_file)
    
if __name__ == "__main__":
    main()