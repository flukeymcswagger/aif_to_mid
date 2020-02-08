# aif_to_mid
A  file carving tool to extract embedded midi from another file

## introduction
Once upon a time, one could allegedly export loops and drummer tracks from garageband into midi files for use in 
other programs. This appears to no longer be the case, and midi data is instead embedded in the metadata of the loop
.aif or .caf file. This utility will search one or more files for such embedded midi data, isolate the midi file,
then write it out to a directory of your choice. 

## requirements
Python 3. Get the installer for your platform of choice here: https://www.python.org/downloads/

## installation
It's just a python script, download it and put it somewhere handy, in your path, whatever..

## usage
usage: aif_to_mid.v1.py [-h] [-v] [-x EXTENSION] [-i INPUT_FILE] [-d INPUT_DIR] [-o OUTPUT_DIR]

A file carver that extracts a midi file from apple loop files

optional arguments:
* -h             show this help message and exit
* -i INPUT_FILE  path to input file to extract midi from
* -d INPUT_DIR   path to directory of files to extract midi from
* -o OUTPUT_DIR  path to output directory (default: .)
* -x EXTENSION   optional file extension (default: .aif)
* -v             provide verbose output

You can point this script at a single file using '-i {path to input file}' OR

You can point this script at a directory to recurse through using '-d {path to input directory' 

By default, this script will assume a file extension of .aif and skip other files, namely because this is the format
that user custom loops are saved as. If you wanted to, for example, try this script against the stock garageband 
loop library, you might consider using the '-x .caf' option since the stock library uses the .caf format. 