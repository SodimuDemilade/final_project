import PyPDF2
import textract
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


filename = 'C:\\Users\\Demilade Sodimu\\Documents\\400 Level notes\\ALPHA\\CSC 415\\new\\LECTURE-2- Intelligent Agents.pdf'
pdfFileObj = open(filename, 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)
num_pages = len(pdfReader.pages)
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.pages[count]
    count +=1
    text += pageObj.extract_text()
# This if statement exists to check if the above library returned words.
# It's done because PyPDF2 cannot read scanned files.
if text != "":
    text = text
else:
    text = textract.process(filename, method='tesseract', language='eng')

# The word_tokenize() function will break our text phrases into
# individual words.
tokens = word_tokenize(text)
punctuations = ['(',')',';',':','[',']',',']
# We initialize the stopwords variable, which is a list of words like
# "The," "I," "and," etc. that don't hold much value as keywords.
stop_words = stopwords.words('english')
keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
# print(keywords)



# for i in range(0, len(keywords)):
#     comb = keywords[i] + keywords[i+1]
#     if comb in ontology:





mydict = {}
for word in keywords:
    if word in mydict:
        mydict[word] += 1
    else:
        mydict[word] = 1
sorted_list = sorted(mydict.items(), key=lambda x:x[1], reverse=True)
print(dict(sorted_list))

