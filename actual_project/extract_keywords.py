import PyPDF2
import os
import comtypes.client
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# # input_file = "C:\\Users\\Demilade Sodimu\\Documents\\400 Level notes\\OMEGA\\CIS421\\NEW\\Lecture 8 - Auditing.pdf"
# input_file = "C:\\Users\\Demilade Sodimu\\Documents\\400 Level notes\\OMEGA\\CSC424\\NEW\\Interconnecting Devices.pptx"
# output_file = "C:\\Users\\Demilade Sodimu\\Documents\\400 Level notes\\OMEGA\\CSC424\\NEW\\Interconnecting Devices.pdf"
#
#
# # FUNCTION TO COVERT PPTX TO pdf
# def ppt_to_pdf(inputfilename, outputfilename, formattype = 32):
#     powerpoint = comtypes.client.CreateObject("Powerpoint.Application")
#     powerpoint.Visible = 1
#
#     if outputfilename[-3:] != 'pdf':
#         outputfilename = outputfilename + ".pdf"
#     deck = powerpoint.Presentations.Open(inputfilename)
#     deck.SaveAs(outputfilename, formattype) # formatType = 32 for ppt to pdf
#     deck.Close()
#     powerpoint.Quit()
#
#
# # CHECK THE FILE EXTENSION
# file_path = "C:\\Users\\Demilade Sodimu\\Documents\\400 Level notes\\OMEGA\\CIS421\\NEW\\Lecture 8 - Auditing.pdf"
# file_extension = os.path.splitext(file_path)[1]
# file_extension = file_extension.lstrip(".")
# if file_extension != "pdf":
#     ppt_to_pdf(input_file, output_file)
#     actual_file = output_file
# else:
#     actual_file = input_file
#
# # CONVERT PDF TO TEXT
# actual_file = "C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\NEW\\CSC424\\CSC424_Modulation, Demodulation  Multiplexing_2023_Part1.pdf"
# mytext = ''
# reader = PyPDF2.PdfReader(actual_file)
# for page_num in range(len(reader.pages)):
#     page = reader.pages[page_num]
#     text = page.extract_text()
#     mytext += text

# txt_path = os.path.splitext(actual_file)[0] + ".txt"
#
# with open(actual_file, 'rb') as pdf_file:
#     reader = PyPDF2.PdfReader(pdf_file)
#     text = ''
#     for page_num in range(len(reader.pages)):
#         page = reader.pages[page_num]
#         text += page.extract_text()
#
# with open(txt_path, 'w', encoding='utf-8') as txt_file:
#     txt_file.write(text)


# EXTRACT KEYWORDS FROM TEXT
def extract_keywords(note):
    # Tokenize the note into words
    tokens = word_tokenize(note)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
    punctuations = ['(', ')', ';', ':', '[', ']', ',', '.', '=']
    main_tokens = [token for token in filtered_tokens if token.lower() not in punctuations]

    # Calculate word frequencies
    fdist = FreqDist(main_tokens)

    # Get the most common keywords
    keyword_count = 3  # Number of keywords to extract
    keywords = [word for word, _ in fdist.most_common(keyword_count)]

    return keywords


# GET THE FINAL KEYWORD
def get_keyword(mytext):
    keyword = extract_keywords(mytext)
    new_keyword = []
    for word in keyword:
        if word.lower() not in new_keyword:
            new_keyword.append(word.lower())
    if new_keyword[0] != "computer":
        final_word = "computer " + new_keyword[0] + " " + new_keyword[1]
    else:
        final_word = new_keyword[0] + " " + new_keyword[1]
    print("Keyword:", final_word)
    return(final_word)


# import PyPDF2
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.stem import PorterStemmer
# from nltk.probability import FreqDist
# from nltk import sent_tokenize
# from nltk.corpus import brown
# from gensim.models import LdaModel
# from gensim.corpora import Dictionary
#
# def extract_text_from_pdf(pdf_path):
#     with open(pdf_path, 'rb') as file:
#         pdf = PyPDF2.PdfReader(file)
#         text = ''
#         for page in range(len(pdf.pages)):
#             text += reader.pages[page].extract_text()
#         return text
#
# def preprocess_text(text):
#     # Tokenize the text
#     tokens = word_tokenize(text.lower())
#
#     # Remove stop words
#     stop_words = set(stopwords.words('english'))
#     tokens = [token for token in tokens if token.isalnum() and token not in stop_words]
#
#     # Stemming
#     stemmer = PorterStemmer()
#     tokens = [stemmer.stem(token) for token in tokens]
#
#     return tokens
#
# def generate_topic(text):
#     # Preprocess the text
#     tokens = preprocess_text(text)
#
#     # Create a dictionary and corpus
#     dictionary = Dictionary([tokens])
#     corpus = [dictionary.doc2bow(tokens)]
#
#     # Train an LDA model
#     model = LdaModel(corpus, num_topics=1, id2word=dictionary)
#
#     # Get the topic words
#     topic_words = model.print_topics(num_words=5)[0][1]
#     topic_words = [word.split('*')[1].strip().strip('"') for word in topic_words.split('+')]
#
#     return topic_words
#
#
# pdf_file = 'C:\\Users\\Demilade Sodimu\\Documents\\my_notes\\courses\\CSC421\\Lecture 8 - Auditing-.pdf'
# text = extract_text_from_pdf(pdf_file)
# topic = generate_topic(text)
# print("The topic of the PDF is:", topic)
