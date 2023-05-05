import nltk
nltk.download('vader_lexicon')

from tkinter import *
from tkinter import messagebox
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Define a function to perform sentiment analysis
def analyze_sentiment():
    # Get the input text from the text box
    text = input_text.get("1.0", END)
    
    # Create a sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()
    
    # Perform sentiment analysis
    scores = analyzer.polarity_scores(text)
    
    # Display the sentiment scores in the labels
    anger_label.config(text=f"Anger: {scores['anger']*100:.2f}%")
    happiness_label.config(text=f"Happiness: {scores['joy']*100:.2f}%")
    contempt_label.config(text=f"Contempt: {scores['contempt']*100:.2f}%")
    hate_label.config(text=f"Hate: {scores['hate']*100:.2f}%")
    
    # Highlight the input text based on sentiment
    for sentence in nltk.sent_tokenize(text):
        sentence_scores = analyzer.polarity_scores(sentence)
        if sentence_scores['compound'] > 0.5:
            input_text.tag_add("positive", f"{input_text.index('1.0')}+{len(sentence)}c")
        elif sentence_scores['compound'] < -0.5:
            input_text.tag_add("negative", f"{input_text.index('1.0')}+{len(sentence)}c")
        else:
            input_text.tag_add("neutral", f"{input_text.index('1.0')}+{len(sentence)}c")
    
    # Display a message box with the overall sentiment
    if scores['compound'] > 0.5:
        messagebox.showinfo("Sentiment Analysis", "Overall sentiment: Positive")
    elif scores['compound'] < -0.5:
        messagebox.showinfo("Sentiment Analysis", "Overall sentiment: Negative")
    else:
        messagebox.showinfo("Sentiment Analysis", "Overall sentiment: Neutral")

# Create a GUI window
root = Tk()
root.title("Sentiment Analysis")

# Create a text box for input text
input_text = Text(root, height=10)
input_text.pack()

# Create buttons for performing sentiment analysis and clearing input text
analyze_button = Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.pack()

clear_button = Button(root, text="Clear Text", command=lambda: input_text.delete("1.0", END))
clear_button.pack()

# Create labels for displaying sentiment scores
anger_label = Label(root, text="Anger: 0.00%")
anger_label.pack()

happiness_label = Label(root, text="Happiness: 0.00%")
happiness_label.pack()

contempt_label = Label(root, text="Contempt: 0.00%")
contempt_label.pack()

hate_label = Label(root, text="Hate: 0.00%")
hate_label.pack()

# Create tags for highlighting input text
input_text.tag_configure("positive", background="#b3ffb3")
input_text.tag_configure("negative", background="#ff9999")
input_text.tag_configure("neutral", background="#e6e6e6")

# Start the GUI event loop
root.mainloop()