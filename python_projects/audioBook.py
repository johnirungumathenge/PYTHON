import pyttsx3

Book= open(r"book.pdf")
book_text = Book.readline()
engine = pyttsx3.init()

for i in book_text:
    engine.say(i)
    engine.runAndWait()