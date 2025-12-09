Motivational Text Extraction Processor
(Developed for Wings of Fire – APJ Abdul Kalam)
💡 Project Overview

Motivational Text Extraction Processor is an intelligent NLP-powered system designed to automatically identify and extract motivational sentences from the book Wings of Fire.
The system processes the full book using regular expressions, sentence filtering, text cleaning, keyword-based NLP rules, and parallel processing to produce clean, high-quality motivational content.

It also generates:

✔ True motivational sentences

✔ CSV report

✔ SQLite database

✔ Word frequency analysis

✔ Motivational bar chart

This provides a structured, fast, and automated way to analyze large inspirational texts.

❓ Problem Statement

Manually searching for motivational lines in a large book like Wings of Fire is time-consuming and inaccurate.
Motivational ideas—such as dream, hope, courage, perseverance, ambition, success—are scattered across many chapters.

Key challenges:

Important sentences are buried inside huge paragraphs

Manual identification is slow and inconsistent

Motivational keywords may appear in different forms

Non-motivational or technical lines must be filtered out

This project solves these challenges by building an automated NLP pipeline that extracts only the most relevant and positive motivational sentences.

* How the Solution Works

The system follows a multi-stage NLP pipeline, and all outputs (CSV, database, charts) are generated automatically after execution.

The 5-Module NLP Pipeline
| Module                             | Description                                                                 | Key Techniques Used                 |
| ---------------------------------- | --------------------------------------------------------------------------- | ----------------------------------- |
| **1. PDF Reader**                  | Loads the *Wings of Fire* PDF and extracts complete raw text.               | PyPDF                               |
| **2. Cleaner & Splitter**          | Removes noise, unwanted symbols, and splits text into meaningful sentences. | Regex, Text Normalization           |
| **3. Motivational Rule Checker**   | Applies thematic rules to detect only positive, motivational sentences.     | Regex, Keyword Matching             |
| **4. Parallel Sentence Processor** | Runs sentence cleaning and classification using multithreading.             | ThreadPoolExecutor, Regex Filtering |
| **5. Output Builder**              | Generates CSV, database tables, and motivational word-frequency bar chart.  | SQLite, CSV, Matplotlib             |


Libraries / Tools Used
External Libraries
Library	Purpose	Install Command
pypdf	PDF- extraction	pip install pypdf
matplotlib	Plotting word frequency charts-pip install matplotlib
Python Standard Libraries

re → Regex matching and text cleaning

csv → Exporting motivational sentences

sqlite3 → Database storage

collections → Word frequency counting

concurrent.futures → Parallel processing

os / io → File handling
Steps to Run the Program
1️⃣ Install Python

Ensure Python 3.8+ is installed:

python --version

2️⃣ Install Required Libraries
pip install pypdf matplotlib

3️⃣ Place the Required Files

Put these files in the same directory:

main.py
wings of fire.pdf

4️⃣ Run the Program
python main.py

5️⃣ View Output Files

After execution, the following files are generated:

Output File	Purpose	Type
| Output File                         | Purpose                                          | Type               |
| ----------------------------------- | ------------------------------------------------ | ------------------ |
| **true_motivational_sentences.csv** | All extracted motivational sentences             | CSV                |
| **motivational_sentences.db**       | Stores each motivational sentence                | SQLite DB          |
| **true_motivational_output.txt**    | Raw motivational sentences                       | Text File          |
| **Word Frequency Chart**            | Visual representation of motivational word usage | PNG / Inline Chart |

🧾 Sample Output & Visualizations
Terminal Output Example
Extracting text...

✓ PDF loaded successfully  
✓ Text cleaned  
✓ Sentences split: 4850  
✓ Parallel processing started...

Filtering motivational sentences...

✓ True motivational sentences found: 72  
✓ Saved to CSV  
✓ Saved to Database  

Counting motivational words...

✓ Frequency plot generated  

🔢 Sample Motivational Word Count (From Book)
dream: 27
success: 18
courage: 14
hope: 12
determination: 11
vision: 9
strength: 8
perseverance: 6
believe: 5
mission: 4

📊 Motivational Word Frequency Chart

A bar chart is automatically generated, showing the most commonly occurring motivational words throughout Wings of Fire.

Example categories:

Dream

Success

Hope

Courage

Faith

Strength

📘 Sentence Categorization Example
✓ 142 motivational sentences found
✓ Stored in motivational_sentences.db
✓ Exported to true_motivational_sentences.csv

🎯 Why This Project Is Useful

✔ Extracts high-quality motivational quotes
✔ Automates complex text analysis
✔ Provides structured insights into inspirational literature
✔ Helps students, researchers, and readers understand theme distribution
✔ Fast and scalable due to parallel processing

 Final Outcome

The final pipeline transforms the Wings of Fire PDF into:

A clean dataset of motivational sentences

A database of filtered content

A frequency-based motivational analysis

A bar chart visualization
