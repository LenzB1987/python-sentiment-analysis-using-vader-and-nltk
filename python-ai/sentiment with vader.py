import tkinter as tk
from tkinter import ttk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# GUI setup
root = tk.Tk()
root.title("Text Sentiment Analysis")

# Function to analyze text sentiment
def analyze_sentiment():
    text = text_box.get("1.0", "end-1c")
    vs = analyzer.polarity_scores(text)

    # Calculate sentiment score as percentage and display in label
    positive_score = vs['pos'] * 100
    negative_score = vs['neg'] * 100
    neutral_score = vs['neu'] * 100
    sentiment_percentages.config(text=f"Positive: {positive_score:.2f}%\nNegative: {negative_score:.2f}%\nNeutral: {neutral_score:.2f}%")

    # Set label text based on sentiment score and highlight color
    if vs['compound'] >= 0.05:
        sentiment_label.config(text="Positive")
        sentiment_label.config(bg="green")
        sentiment_percentages.config(fg="green")
    elif vs['compound'] <= -0.05:
        sentiment_label.config(text="Negative")
        sentiment_label.config(bg="red")
        sentiment_percentages.config(fg="red")
    else:
        sentiment_label.config(text="Neutral")
        sentiment_label.config(bg="gray")
        sentiment_percentages.config(fg="black")

# Text box for input
text_box = tk.Text(root, height=10, width=50)
text_box.grid(row=0, column=0, padx=10, pady=10)

# Button to analyze text sentiment
analyze_button = ttk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.grid(row=1, column=0, padx=10, pady=10)

# Label to display text sentiment
sentiment_label = tk.Label(root, text="", font=("Arial Bold", 14), pady=10)
sentiment_label.grid(row=2, column=0, padx=10)

# Label to display sentiment scores as percentages
sentiment_percentages = tk.Label(root, text="", font=("Arial", 12), pady=10)
sentiment_percentages.grid(row=3, column=0, padx=10, pady=10)

root.mainloop()