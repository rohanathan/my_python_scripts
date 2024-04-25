# URL Extractor

## Overview
URL Extractor is a Python script that extracts URLs from a text file and saves them into another text file. This can be useful for tasks such as extracting URLs from chat logs, documents, or any other text-based files.

## Features
- Extracts URLs from a text file using regular expressions.
- Saves the extracted URLs into another text file.

## Usage
1. Clone this repository to your local machine.
2. Ensure you have Python installed on your machine.
3. Open a terminal or command prompt and navigate to the directory containing the Python script (`extract_urls.py`).
4. Run the script by executing the following command:

       python extract_urls.py
5. Follow the prompts to provide the path to the input text file and the path to the output directory.
6. The script will extract the URLs from the input text file and save them into `output.txt` in the specified output directory.

## Example
Suppose you have a text file named `chat.txt` containing the following text:

Hey, check out this website: https://www.example.com
I found another interesting article: http://www.example.org/article.html


Running the script and providing `chat.txt` as the input file and `C:\temp` as the output directory will result in the following output:



    Enter the path to the input text file: chat.txt
    Enter the path to the output directory where you want to save the 
    output file: C:\temp
    URLs found in the file:
    https://www.example.com
    http://www.example.org/article.html
    Extracted URLs saved to C:\temp\output.txt



## Requirements
- Python 3.x

