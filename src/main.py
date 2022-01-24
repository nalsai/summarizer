#!/usr/bin/env python3

"""A Program to summarize text, I guess."""

import argparse


def parse_command_line():
    """Function to parse user input."""
    parser = argparse.ArgumentParser(description="""Program to summarize text.
    Please provide an input file.""")
    parser.add_argument("-i", "--input", help="path of input text file.")
    parser.add_argument("-o", "--output", help="path of output text file.")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    return input_file, output_file

if __name__ == "__main__":
    try:
        input_f, output_f = parse_command_line()

        with open(input_f) as file:
            text = file.read()
            print(text)

    except FileNotFoundError:
        print("An error occured.")
        print("Did you input the correct path?")
    except TypeError:
        print("An error occured.")
        print("Did you specify an input path?")
        print("Check -h or --help for options.")
