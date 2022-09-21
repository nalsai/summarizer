#!/usr/bin/env python3

"""
A program to summarize text, I guess.
"""

import argparse
import sys
try:
    from summarizer.text_summarize import do_stuff
except ImportError:
    from text_summarize import do_stuff


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
    try:
        sentences_number = int(args.number)
    except TypeError:
        sentences_number = -1
    except ValueError:
        print("Did you specify the number of sentences correctly? Using default value.")
        sentences_number = -1
    return input_file, output_file, sentences_number


def main():
    """main"""
    try:
        input_f, output_f, sentences_n = parse_command_line()
        if input_f == "-":
            text_input = sys.stdin.read()
        else:
            with open(input_f, "r", encoding="utf8") as file:
                text_input = file.read()

    except FileNotFoundError:
        print("An error occured.")
        print("Did you input the correct path?")
    except TypeError:
        print("An error occured.")
        print("Did you specify an input path?")
        print("Check -h or --help for options.")

    if text_input:
        summarized_text = do_stuff(text_input, sentences_n)
        if output_f:
            try:
                with open(output_f, "w", encoding="utf8") as file:
                    file.write(summarized_text)
            except (IsADirectoryError, PermissionError, FileNotFoundError) as ex:
                print(str.format("An error occured ({}).", type(ex).__name__))
                print("Is your output path correct?")
        else:
            print(summarized_text)


if __name__ == '__main__':
    main()
