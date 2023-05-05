import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# GUI setup
root = tk.Tk()
root.title("Text Sentiment Analysis")

# Function to analyze text sentiment
def analyze_sentiment():
    text = text_box.get("1.0", "end-1c")
    vs = analyzer.polarity_scores(text)

    # Set label text based on sentiment score
    if vs['compound'] >= 0.05:
        sentiment_label.config(text="Positive")
        sentiment_label.config(fg="green")
        image = Image.open("positive.png")
    elif vs['compound'] <= -0.05:
        sentiment_label.config(text="Negative")
        sentiment_label.config(fg="red")
        image = Image.open("negative.png")
    else:
        sentiment_label.config(text="Neutral")
        sentiment_label.config(fg="black")
        image = Image.open("neutral.png")

    # Resize image and display it in the GUI
    image = image.resize((150, 150), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(image)
    image_label.config(image=photo)
    image_label.image = photo

    # Calculate sentiment score as percentage and display in label
    positive_score = vs['pos'] * 100
    negative_score = vs['neg'] * 100
    neutral_score = vs['neu'] * 100
    sentiment_percentages.config(text=f"Positive: {positive_score:.2f}%\nNegative: {negative_score:.2f}%\nNeutral: {neutral_score:.2f}%")

# Function to open a file dialog and select an image
def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = Image.open(file_path)
        image = image.resize((150, 150), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        image_label.config(image=photo)
        image_label.image = photo

# Text box for input
text_box = tk.Text(root, height=10, width=50)
text_box.grid(row=0, column=0, padx=10, pady=10)

# Button to analyze text sentiment
analyze_button = ttk.Button(root, text="Analyze Sentiment", command=analyze_sentiment)
analyze_button.grid(row=1, column=0, padx=10, pady=10)

# Label to display text sentiment
sentiment_label = tk.Label(root, text="")
sentiment_label.grid(row=2, column=0, padx=10, pady=10)

# Label to display image based on sentiment
image_label = tk.Label(root)
image_label.grid(row=0, column=1, rowspan=3, padx=10, pady=10)

# Button to select an image
select_image_button = ttk.Button(root, text="Select Image", command=select_image)
select_image_button.grid(row=3, column=1, padx=10, pady=10)

# Label to display sentiment scores as percentages
sentiment_percentages = tk.Label(root, text="")
sentiment_percentages.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()