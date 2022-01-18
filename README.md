# Captain-s-Log
## Introduction
An audio transcription program utilizing IBM's Watson Speech to Text tool

One of my favorite Sci-Fi Series of all time in Star Trek and one of the iconic features of a Star Trek show is personal logs. In a Star Trek series, characters maintain audio logs of things that they are doing and can search through their personal logs for keywords or date. While recording an audio file can be done on most computers, getting a transcription with dates can be a bit more complicated. The purpose of this project is to create a python script that can take personal logs and transcribe it into text.

As of now this project takes a wemb file (which is the file format my personal logs are in) and converts it into a written transcription with confidence scores sent from Watson. This program is designed to function with any length audio file and will not be capped by the file size limit imposed by ibm.


## Dependencies
Each of the following packages for python are used. Please ensure that all are installed for the program to work as intended
 1. SpeechToTextV1 from ibm_watson
 2. IAMAuthenticator from ibm_cloud_sdk_core.authenticators
 3. subprocess
 4. os
 5. ffmpeg


## Quickstart
 1. Download all dependencies
 2. Sign up for an IBM account and start and start a Speech to Text service: https://www.ibm.com/cloud/watson-speech-to-text
 3. Set your credentials in the Python Script
 4. Place audio file titled audio.webm into Captain's Log Folder
 5. Run python script
 6. the final transcription can be found in the output.txt file


## TODO
modify command to take user input for file name
Allow the program to record the audio for you?
Have output to a markdown file for usage in Obsidian Notes
