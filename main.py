from google.colab import drive
drive.mount('/content/drive')

!ls drive/MyDrive/

# Step 2: Install PyPDF (if not installed)
!pip install pypdf

# Step 3: Extract text from PDF
from pypdf import PdfReader

pdf_path = "/content/drive/MyDrive/wings of fire.pdf"  # your PDF path
reader = PdfReader(pdf_path)

text = ""
for page in reader.pages:
    text += page.extract_text() + "\n"

print("PDF loaded successfully!")
print("Number of characters extracted:", len(text))

import re

# Step 1: Remove unwanted characters/symbols
# Keep letters, numbers, punctuation (.?!), and spaces
clean_text = re.sub(r'[^A-Za-z0-9\s.,?!]', ' ', text)

# Step 2: Replace multiple spaces/newlines with single space
clean_text = re.sub(r'\s+', ' ', clean_text).strip()

print("Text cleaned successfully!")
print("Number of characters after cleaning:", len(clean_text))

import re

# Split text into sentences
sentences = re.split(r'[.?!]\s*', text)

print("Total sentences found:", len(sentences))
sentences = re.split(r'(?<=[.?!])\s+', clean_text)

print("Total sentences found:", len(sentences))

def clean_text(s):
    # Keep letters, numbers, punctuation (.?!), and spaces
    s = re.sub(r'[^A-Za-z0-9\s.,?!]', ' ', s)
    # Replace multiple spaces with single space
    s = re.sub(r'\s+', ' ', s).strip()
    return s
from concurrent.futures import ThreadPoolExecutor

cleaned_sentences = []

# Parallel processing using ThreadPoolExecutor
with ThreadPoolExecutor() as executor:
    results = executor.map(clean_text, sentences)

# Combine results
cleaned_sentences = list(results)

print("Total cleaned sentences:", len(cleaned_sentences))

import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect("/content/motivational_words.db")
cursor = conn.cursor()

# Create table for motivational words
cursor.execute("""
CREATE TABLE IF NOT EXISTS motivational_words (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    word TEXT UNIQUE
)
""")

conn.commit()
print("Database and table created successfully!")

# Example list of motivational words (from Wings of Fire style)
words = [
    "dream", "dreams", "believe", "belief", "hope", "fire", "wings", "goal", "vision", "succeed",
    "success", "determination", "hard work", "commitment", "dedication", "perseverance", "faith",
    "desire", "courage", "confidence", "strength", "growth", "struggle", "overcome", "challenge",
    "opportunity", "learning", "knowledge", "talent", "potential", "responsibility", "service",
    "mission", "ambition", "passion", "future", "greatness", "excellence", "sacrifice", "help",
    "humanity", "humility", "wisdom", "fail", "failure", "try", "attempt", "move forward", "never give up",
    "destiny"
]


for w in words:
    try:
        cursor.execute("INSERT OR IGNORE INTO motivational_words (word) VALUES (?)", (w,))
    except Exception as e:
        print("Error inserting:", w, e)

conn.commit()
print("Motivational words stored successfully!")


cursor.execute("SELECT * FROM motivational_words")
rows = cursor.fetchall()
print("Total words stored:", len(rows))
print(rows[:50])  # show first 10 words


import re
from concurrent.futures import ThreadPoolExecutor

# ------------------- WORD LISTS -------------------

motiv_keywords = [
    "success", "succeed", "achieve", "goal", "dream", "hard work", "devotion",
    "mission", "commitment", "belief", "believe", "inspiration", "inspire",
    "hope", "courage", "wisdom", "vision", "perseverance", "determination",
    "positive", "strength", "progress", "overcome"
]

positive_emotion = [
    "believe", "belief", "hope", "inspiration", "inspire", "courage", "wisdom",
    "faith", "devotion", "dream", "dreams", "self confident", "encouraged",
    "optimistic", "positive", "motivation"
]

reject_negative = [
    "fail", "failure", "problem", "mistake", "anger", "worry", "fear",
    "hate", "wrong", "loss", "lost", "pain", "difficulty"
]

reject_technical = [
    "rocket", "missile", "launch", "test", "trial", "project",
    "engineer", "technology", "program", "flight", "satellite",
    "system", "stage", "vehicle", "subsystem", "payload"
]

# ------------------- REGEX -------------------

motiv_pattern = r'\b(?:' + '|'.join(map(re.escape, motiv_keywords)) + r')\b'
positive_pattern = r'\b(?:' + '|'.join(map(re.escape, positive_emotion)) + r')\b'
neg_pattern = r'\b(?:' + '|'.join(map(re.escape, reject_negative)) + r')\b'
tech_pattern = r'\b(?:' + '|'.join(map(re.escape, reject_technical)) + r')\b'

# ------------------- CLEAN TEXT -------------------

def clean_text(s):
    s = re.sub(r'[^A-Za-z0-9\s.,?!-]', ' ', s)
    s = re.sub(r'\s+', ' ', s).strip()
    return s

# ------------------- TRUE MOTIVATIONAL FILTER -------------------

def extract_true_motivational(paragraph):
    paragraph = clean_text(paragraph)
    sentences = re.split(r'[.?!]\s*', paragraph)

    selected = []

    for s in sentences:
        s_clean = s.strip()

        if len(s_clean.split()) < 6:
            continue

        # Must have motivational keyword
        if not re.search(motiv_pattern, s_clean, re.IGNORECASE):
            continue

        # Must have positive-emotional keyword
        if not re.search(positive_pattern, s_clean, re.IGNORECASE):
            continue

        # Reject technical lines
        if re.search(tech_pattern, s_clean, re.IGNORECASE):
            continue

        # Reject negative context
        if re.search(neg_pattern, s_clean, re.IGNORECASE):
            continue

        selected.append(s_clean)

    return selected

# ------------------- PARALLEL EXECUTION -------------------

true_motivational_sentences = []

with ThreadPoolExecutor() as executor:
    results = executor.map(extract_true_motivational, paragraphs)

for r in results:
    true_motivational_sentences.extend(r)

# ------------------- OUTPUT -------------------

for i, s in enumerate(true_motivational_sentences, 1):
    print(f"{i}. {s}")

with open("true_motivational_output.txt", "w", encoding="utf-8") as f:
    for s in true_motivational_sentences:
        f.write(s + "\n")

print("\nTotal true motivational sentences found:", len(true_motivational_sentences))
# ------------------- SAVE TO CSV -------------------
csv_file = "true_motivational_sentences.csv"
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Sentence Number", "Sentence"])
    for i, s in enumerate(true_motivational_sentences, start=1):
        writer.writerow([i, s])

print(f"Saved {len(true_motivational_sentences)} sentences to CSV file: {csv_file}")

# ------------------- SAVE TO SQLITE DATABASE -------------------
db_file = "motivational_sentences.db"
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create table if it does not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS motivational_sentences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sentence TEXT NOT NULL
)
""")

# Insert sentences into the table
for s in true_motivational_sentences:
    cursor.execute("INSERT INTO motivational_sentences (sentence) VALUES (?)", (s,))

conn.commit()
conn.close()
print(f"Saved {len(true_motivational_sentences)} sentences to database: {db_file}")

import matplotlib.pyplot as plt
from collections import Counter
import re

# ------------------- Motivational Words -------------------
# Use the 'words' variable from previous steps, converting to lowercase for consistency
motivational_words = [w.lower() for w in words]

# ------------------- Read the Book -------------------
# The 'text' variable already holds the full content of the PDF from previous steps.
# Convert it to lowercase for consistent matching.
text_content = text.lower()

# ------------------- Count Frequencies -------------------
word_counter = Counter()

for word in motivational_words:
    # Use regex for whole word match, handling multi-word phrases correctly
    if ' ' in word: # Check for phrases like "hard work" or "never give up"
        # re.escape() is used to escape any special characters in the word to treat them literally
        count = len(re.findall(r'\b' + re.escape(word) + r'\b', text_content))
    else:
        count = len(re.findall(r'\b' + word + r'\b', text_content))
    word_counter[word] = count

# Remove words that don't appear in the text
word_counter = {k: v for k, v in word_counter.items() if v > 0}

# Sort the words by frequency in descending order for better visualization
sorted_word_counter = dict(sorted(word_counter.items(), key=lambda item: item[1], reverse=True))

# ------------------- Plot Bar Graph -------------------
plt.figure(figsize=(18,7))
plt.bar(sorted_word_counter.keys(), sorted_word_counter.values(), color='skyblue')
plt.xticks(rotation=90)
plt.xlabel("Motivational Words")
plt.ylabel("Frequency in Wings of Fire")
plt.title("Frequency of Motivational Words in Wings of Fire")
plt.tight_layout() # Adjust layout to prevent labels from overlapping
plt.show()


