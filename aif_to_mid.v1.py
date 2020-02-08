#!/usr/bin/env python3
# coding: utf-8
import argparse, os, sys

parser = argparse.ArgumentParser(description="A file carver that extracts a midi file from apple loop files")
parser.add_argument('-i', dest='input_file', help="path to input file to extract midi from")
parser.add_argument('-d', dest='input_dir', help="path to directory of files to extract midi from")
parser.add_argument('-o', dest='output_dir', default='.', help='path to output directory')
parser.add_argument('-x', dest='extension', default='.aif', help='optional file extension (default .aif)')
parser.add_argument('-v', dest='verbose', default=False, action='store_true', help='provide verbose output')
args = parser.parse_args()

# Some important file magic..
# Ref: https://github.com/colxi/midi-parser-js/wiki/MIDI-File-Format-Specifications
header = b'\x4D\x54\x68\x64'
footer = b'\xFF\x2F\x00'
track_header = b'\x4D\x54\x72\x6B'


def carve_midi(input_file, output_dir):
    # open the file and read it into memory
    try:
        with open(input_file, "rb") as infile:
            blob = infile.read()
    except FileNotFoundError:
        print("File not found: {}".format(input_file))
        sys.exit(1)

    # first things first: find a midi header
    try:
        start_offset = blob.index(header)
        if args.verbose: print("Found midi header at byte offset: {}".format(start_offset))
    except ValueError:
        print("Couldn't find a midi file header anywhere. Skipping file: {}".format(input_file))
        return

    # ok good stuff, got a midi file, get the number of tracks
    ntrack_bytes = blob[start_offset+10:start_offset+12]
    ntrack_count = int.from_bytes(ntrack_bytes, byteorder='big')
    cursor = start_offset

    # iterate through each track and update our spot in the file
    for track_num in range(1, ntrack_count+1):
        if args.verbose: print("scanning for track {}..".format(track_num),end='')

        try:
            t_offset = blob[cursor:].index(track_header)
            if args.verbose: print("found track at byte offset {}..".format(cursor + t_offset))
            cursor += t_offset + 4
        except ValueError:
            print("Wierd. Found a midi header but no tracks. Do not Panic. Skipping file: ()".format(input_file))
            return
    
	# find the offset for the end of the midi file via the footer bytes
    end_offset = cursor + blob[cursor:].index(footer) + len(footer)
    if args.verbose: print("No more tracks. Last byte offset: {}".format(end_offset))

    # replace the original extension with .mid
    output_file = input_file.split("/")[-1]
    output_file = output_file[:-4] + ".mid"

    # create the output directory if one doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # slam your fist on the desk, curse apple for their shitty practices, then claim your prize, victorious!
    output_fullpath = output_dir + "/" + output_file
    with open(output_fullpath, "wb") as outfile:
        print("Processed {}. Midi file found, writing to {}".format(input_file, output_fullpath))
        outfile.write(blob[start_offset:end_offset])

def main():
    if args.input_file:
        carve_midi(args.input_file, args.output_dir)
    elif args.input_dir:
        for root, subFolders, files in os.walk(args.input_dir):
            for file in files:
                if file.endswith(args.extension):
                    carve_midi(os.path.join(root,file), args.output_dir)
    else:
        print("Missing input file. Run with -h to get help/usage instructions.")

if __name__ == "__main__":
    main()


