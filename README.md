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

## examples
User loops are stored in your home directory in the subdirectory ./Library/Audio/Apple Loops/User Loops/

If you created a loop in garageband named 'Drummer' you could extract that midi file with the following command:

```bash
leela:~ $ ./aif_to_mid.v1.py -i ./Library/Audio/Apple\ Loops/User\ Loops/SingleFiles/Drummer.aif 
Processed ./Library/Audio/Apple Loops/User Loops/SingleFiles/Drummer.aif. Midi file found, writing to ./Drummer.mid
```

Maybe you want to dump all of your user loops out:

```bash
leela:~ $ ./aif_to_mid.v1.py -d ./Library/Audio/Apple\ Loops/User\ Loops/SingleFiles/
Processed ./Library/Audio/Apple Loops/User Loops/SingleFiles/Drummer.aif. Midi file found, writing to ./Drummer.mid
Processed ./Library/Audio/Apple Loops/User Loops/SingleFiles/Drummer_01.aif. Midi file found, writing to ./Drummer_01.mid
Processed ./Library/Audio/Apple Loops/User Loops/SingleFiles/Drummer_02.aif. Midi file found, writing to ./Drummer_02.mid
Processed ./Library/Audio/Apple Loops/User Loops/SingleFiles/testsong_chorus.aif. Midi file found, writing to ./testsong_chorus.mid
Processed ./Library/Audio/Apple Loops/User Loops/SingleFiles/testsong_into.aif. Midi file found, writing to ./testsong_into.mid
Processed ./Library/Audio/Apple Loops/User Loops/SingleFiles/testsong_verse.aif. Midi file found, writing to ./testsong_verse.mid
```

And maybe you wanted to see if there are any midi loops in the stock garageband libraries. (there are located under
/Library/Audio/Apple Loops/Apple/) These are actually .caf files, but they can also contain embedded midi. In this case, 
you will need to use the -x option to specify the file extension .caf to force the script to read caf files. For 
convenience, we can use the -o to specify an output directory to store the results. 

This will generate a lot of output, as many files don't contain midi, but when we get to the drum loops..

```bash
leela:~ $ ./aif_to_mid.v1.py -d /Library/Audio/Apple\ Loops/Apple/ -o /Volumes/evilempire/test/mega/ -x .caf -o output
... output truncated for brevity
Couldn't find a midi file header anywhere. Skipping file: /Library/Audio/Apple Loops/Apple/12 Chinese Traditional/Whimsical Dizi 01.caf
Couldn't find a midi file header anywhere. Skipping file: /Library/Audio/Apple Loops/Apple/12 Chinese Traditional/Whimsical Dizi 02.caf
Processed /Library/Audio/Apple Loops/Apple/13 Drummer/Aidan - Bridge.caf. Midi file found, writing to output/Aidan - Bridge.mid
Processed /Library/Audio/Apple Loops/Apple/13 Drummer/Aidan - Burnside.caf. Midi file found, writing to output/Aidan - Burnside.mid
... etc
```

Enjoy!a