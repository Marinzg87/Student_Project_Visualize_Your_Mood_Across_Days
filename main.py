import streamlit as st
import re
from nltk.sentiment import SentimentIntensityAnalyzer

# Header
header = st.header("Dairy Tone")

# Subheader
subheader_positivity = st.subheader("Positivity")

# Read the diary input
with open("diary/2023-10-21.txt", "r") as file:
    book = file.read()

# Create pattern for each word in dairy input
pattern = re.compile("[a-zA-Z]+")
findings = re.findall(pattern, book.lower())

# Calculate quantity of words
d = {}
for word in findings:
    if word in d.keys():
        d[word] = d[word] + 1
    else:
        d[word] = 1

# Plot the line chart with words and quantities
word_chart = d
st.line_chart(word_chart)

# Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(book)

# Plot the chart with scores
st.line_chart(scores)

subheader_negativity = st.subheader("Negativity")

# st.line_chart(negativity_chart)
