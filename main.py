import streamlit as st
from nltk.sentiment import SentimentIntensityAnalyzer
import glob
from pathlib import Path

# Header
header = st.header("Dairy Tone")

# Subheader
subheader_positivity = st.subheader("Positivity")

# Create dictionary of daily posts
# Create a list of files
filepaths = glob.glob("diary/*.txt")

# Sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Iterate through the daily input for positive analyze
positive_daily_inputs = {}
for filepath in filepaths:
    # Read the daily input
    with open(filepath, "r") as file:
        book = file.read()
    # Get the date
    filename = Path(filepath).stem
    # Analyzer
    scores = analyzer.polarity_scores(book)
    pos_score = scores["pos"]
    # Write the data to dictionary
    if filename in positive_daily_inputs.keys():
        continue
    else:
        positive_daily_inputs[filename] = pos_score

# Iterate through the daily input for negative analyze
negative_daily_inputs = {}
for filepath in filepaths:
    # Read the daily input
    with open(filepath, "r") as file:
        book = file.read()
    # Get the date
    filename = Path(filepath).stem
    # Analyzer
    scores = analyzer.polarity_scores(book)
    neg_score = scores["neg"]
    # Write the data to dictionary
    if filename in negative_daily_inputs.keys():
        continue
    else:
        negative_daily_inputs[filename] = neg_score

# Plot the chart with positive scores
st.line_chart(positive_daily_inputs)

# Subheader
subheader_negativity = st.subheader("Negativity")

# Plot the chart with negative scores
st.line_chart(negative_daily_inputs)
