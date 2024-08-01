# ROT Encoder/Decoder

A Python script for encoding and decoding text using the ROT cipher (rotation cipher), with support for colorized terminal output and a user-friendly command-line interface.

# Features

- **Encode**: Shift characters in text by a specified rotation key
- **Decode**: Revert encoded text using the same rotation key
- **Customizable Key**: Set the rotation key for both encoding and decoding
- **Colorized Output**: Uses colorama for color-coded terminal output
- **Command-Line Interface**: Built with click for intuitive command-line interaction

# Requirements

- Python 3.x
- ```colorama``` library
- ```click``` library

  # Installation

  ```sh
  pip install colorama click
  ```

  # Usage

  1. **Run the Script**: Start the script in your terminal.
  2. **Select Operation**: Choose the operation (*e* for encode, *d* for decode).
  3. Provide **Text** and **Key**: Enter the text and rotation key as prompted.
 
  # Commands

  - **Encoding**: *e* (Encodes the provided text)
      - **Command**: *e*
      - **Text**: *Hello, World!*
      - **Key**: *13*
      - **Output**: *Uryyb, Jbeyq!*
   
  - **Decoding**: *d* (Decodes the provided text)
      - **Command**: *d*
      - **Text**: *Uryyb, Jbeyq!*
      - **Key**: *13*
      - **Output**: *Hello, World!*

  # Additional Information

  - ```colorama``` : Adds color to terminal output, enhancing readability
  - ```click``` : Used the *pause* function to avoid script exiting immediately after printing the result
