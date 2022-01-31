#!/usr/bin/env python3

"""A program to summarize text, I guess."""

import argparse
import sys
try:
    import summarizer.text_summarize
except ImportError:
    import text_summarize


def parse_command_line():
    """Function to parse user input."""
    parser = argparse.ArgumentParser(
        description="A program to summarize text. Please provide an input file or text.")
    parser.add_argument(
        "-i", "--input", help="path of input text file (use - to read from stdin)")
    parser.add_argument(
        "-o", "--output", help="path of output text file (prints to stdout if not specified)")
    parser.add_argument("-n", "--number", help="number of sentences")

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    sentences_number = int(args.number)
    return input_file, output_file, sentences_number


def main():
    """main"""
    try:
        input_f, output_f, sentences_n = parse_command_line()

        text_input = ""

        if input_f == "-":
            text_input = sys.stdin.read()
        else:
            with open(input_f, "r") as file:
                text_input = file.read()

    except FileNotFoundError:
        print("An error occured.")
        print("Did you input the correct path?")
    except TypeError:
        print("An error occured.")
        print("Did you specify an input path?")
        print("Check -h or --help for options.")

    if text_input:
        summarized_text = text_summarize.do_stuff(text_input, sentences_n)
        if output_f:
            with open(output_f, "w") as file:
                file.write(summarized_text)
        else:
            print(summarized_text)


if __name__ == '__main__':
    main()
