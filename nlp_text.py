import nltk

text = """
Name: vaibhavi devare
Roll No: 35
Year: B.Tech
Branch: Information Technology.
Mobile no: 0987654321
Email: vaibhavi@gmail.com
"""

tokens = nltk.word_tokenize(text)
print(tokens)


#(venv) PS C:\Users\Shree\Desktop\NLP> python Assigenment1.py

# ['Name', ':', 'Gawali', 'Tejshree', 'Tulshidas', '.', 'Roll', 'No', ':', '47', 'Year', ':', 'B.Tech', 'Branch', ':', 'Information', 'Technology', '.', 'Mobile', 'no', ':', '0872392648716', 'Email', ':', 'tej', '@', 'gmail.com']
