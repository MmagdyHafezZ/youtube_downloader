---

# YouTube Video Downloader

This script is a simple command-line tool for downloading YouTube videos.

## Description

The YouTube Video Downloader is a Python script that uses the `pytube` library to download videos from YouTube. Users can input a YouTube URL, and the script will download the video in its highest available resolution.

## Installation

1. Ensure you have Python 3.x installed on your system. If not, download and install it from the [official Python website](https://www.python.org/).

2. Clone this repository or download the script to your local machine.

3. The script is set up with a virtual environment in the `venv` directory containing all the necessary dependencies.

## Usage

If you're on Windows, you can simply use the `runner.bat` file to run the script. This batch file automatically activates the virtual environment and runs the script for you. Just double-click on `runner.bat`, or run it from the command line:
```
runner.bat
```

When prompted, enter the URL of the YouTube video you want to download. The video will be saved in the `downloads` directory in the script's root folder.

If you're not on Windows, navigate to the script's directory in the command line, activate the virtual environment, and run the script:
```
source venv/bin/activate
python script_name.py
```
Replace `script_name.py` with the actual name of the script.

## Disclaimer

This script is for educational purposes only. Users are responsible for using the YouTube Video Downloader in accordance with YouTube's terms of service, including any relevant copyright and intellectual property regulations. Use at your own risk.

---

