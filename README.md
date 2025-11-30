# Motivational Sentence Extraction from Wings of Fire

## Description
This project extracts motivational sentences from the book *Wings of Fire* using Python and regular expressions. It identifies sentences containing motivational words, saves them to CSV and SQLite databases, and visualizes word frequency in a bar chart.

## How it Works
1. Load the PDF file of the book.
2. Clean the text and split it into sentences.
3. Filter sentences that contain motivational words.
4. Save the results to:
   - CSV file (`true_motivational_sentences.csv`)
   - SQLite database (`motivational_sentences.db`)
5. Count frequency of motivational words and plot a bar chart.
6. Save the chart in the `charts/` folder.

## Requirements
- Python 3.x
- Libraries:
  - pypdf
  - matplotlib

## Steps to Run
1. Open terminal or command prompt.
2. Install required libraries:

```bash
pip install -r requirements.txt
