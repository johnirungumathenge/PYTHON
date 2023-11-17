import PyPDF2

file = open("book.pdf","rb")
reader = PyPDF2.PdfFileReader(file)

page1 = reader.getPage(1)
a = page1.extractText()
print(reader.numPages)
print(a)