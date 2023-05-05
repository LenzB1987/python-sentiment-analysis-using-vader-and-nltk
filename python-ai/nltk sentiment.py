import nltk
import tkinter as tk
from tkinter import scrolledtext
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Define a function to analyze the sentiment of the text
def analyze_sentiment():
    # Get the text from the text box
    text = text_box.get("1.0", "end-1c")
    # Analyze the sentiment of the text
    scores = sia.polarity_scores(text)
    # Display the sentiment analysis results
    sentiment = "Positive" if scores["compound"] > 0 else "Negative"
    result_box.delete("1.0", "end")
    result_box.insert("end", f"Sentiment: {sentiment}\n")
    result_box.insert("end", f"Positive: {scores['pos']:.2f}\n")
    result_box.insert("end", f"Negative: {scores['neg']:.2f}\n")
    result_box.insert("end", f"Neutral: {scores['neu']:.2f}\n")
    result_box.insert("end", f"Compound: {scores['compound']:.2f}")

# Create the GUI window
window = tk.Tk()
window.title("Sentiment Analysis")

# Create the text box for input text
text_box = scrolledtext.ScrolledText(window, width=50, height=10)
text_box.pack()

# Create the analyze button
analyze_button = tk.Button(window, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

# Create the text box for displaying the sentiment analysis results
result_box = scrolledtext.ScrolledText(window, width=50, height=10)
result_box.pack()

# Start the GUI event loop
window.mainloop()