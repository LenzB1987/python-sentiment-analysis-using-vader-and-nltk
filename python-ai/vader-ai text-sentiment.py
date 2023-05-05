import tkinter as tk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create a function to perform sentiment analysis on the given text
def analyze_sentiment():
    # Get the text from the text box
    text = text_box.get("1.0", "end-1c")

    # Initialize the sentiment analyzer
    analyzer = SentimentIntensityAnalyzer()

    # Get the sentiment scores for the text
    scores = analyzer.polarity_scores(text)

    # Update the labels with the sentiment scores
    anger_label.config(text="Anger: {:.1%}".format(scores["anger"]))
    happiness_label.config(text="Happiness: {:.1%}".format(scores["happiness"]))
    contempt_label.config(text="Contempt: {:.1%}".format(scores["contempt"]))
    hate_label.config(text="Hate: {:.1%}".format(scores["hate"]))

    # Highlight the text based on the sentiment scores
    for word in text.split():
        word_scores = analyzer.polarity_scores(word)
        if word_scores["anger"] > 0.5:
            text_box.tag_add("anger", "1.0+{}c".format(text.index(word)), "1.0+{}c".format(text.index(word)+len(word)))
        elif word_scores["happiness"] > 0.5:
            text_box.tag_add("happiness", "1.0+{}c".format(text.index(word)), "1.0+{}c".format(text.index(word)+len(word)))
        elif word_scores["contempt"] > 0.5:
            text_box.tag_add("contempt", "1.0+{}c".format(text.index(word)), "1.0+{}c".format(text.index(word)+len(word)))
        elif word_scores["hate"] > 0.5:
            text_box.tag_add("hate", "1.0+{}c".format(text.index(word)), "1.0+{}c".format(text.index(word)+len(word)))

# Create the main window
root = tk.Tk()
root.title("Text Sentiment Analysis")

# Create the text box for input
text_box = tk.Text(root, height=10, width=50)
text_box.pack()

# Create the buttons for analysis
analyze_button = tk.Button(root, text="Analyze", command=analyze_sentiment)
analyze_button.pack()

# Create the labels for sentiment scores
anger_label = tk.Label(root, text="Anger: 0.0%")
anger_label.pack()
happiness_label = tk.Label(root, text="Happiness: 0.0%")
happiness_label.pack()
contempt_label = tk.Label(root, text="Contempt: 0.0%")
contempt_label.pack()
hate_label = tk.Label(root, text="Hate: 0.0%")
hate_label.pack()

# Create the tags for highlighting
text_box.tag_configure("anger", background="red")
text_box.tag_configure("happiness", background="green")
text_box.tag_configure("contempt", background="orange")
text_box.tag_configure("hate", background="purple")

# Start the main event loop
root.mainloop()
