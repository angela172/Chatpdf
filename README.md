# Chatpdf
The application involves a chatbot that reads PDFs and extracts insights.

Chatbot-pdf extractor 
## Goal
This application helps to read a pdf document with the help of a AI-chatbot which helps to extract 
the required information for the pdf. This  helps us to understand the document to the point but 
also helps to summarise the document as a whole.
The application uses python libraries and is hosted using Streamlit.

### Before hosting the application:
Setting up the Chatbot:
This application uses the LLamma chatbot 3 for better results. After the contents of the pdf are extracted, it 
is fed to the chatbot. The chatbot accordingly fine-tunes the input fed to it and displays the output.
To run it using Ollama:
- Run Command Prompt as Administrator

- Update pip and install these dependencies:
```
pip install --upgrade pip
pip install ollama
```

The below steps are displayed on how the application is hosted:
# Installation
1. Clone the repository: `git clone https://github.com/angela172/Chatpdf.git`
2. Navigate to the project directory: `cd project-name`
3. Create a virtual Environment
3. Install dependencies:`pip install -r requirements.txt`
4. Start the project: `streamlit run app.py`

 -Libraries
  1. PyPDF2 3.0.1:- Used to manupilate, extract and read PDFs. Its useful in tasks such as merging
     pdfs, splitting etc.
  2. sentence-transformers:- Used to manupilate sentences into numeric vectors called embeddings. This helps 
     to capture the meaning of the sentence. This is useful for tasks such as to find similar sentences, clustering etc.
     for this application we have used the sentence-tranformer-'all-MiniLM-L6-v2' due to its lightweight and efficiency making ideal for cases
     where computational resources are limited.
  3. faiss-cpu-1.9.0:-  Used for efficient similarity search and clustering of dense vectors. It is mostly 
     used in finding similar items in large datasets such as texts, images, etc.
  5. streamlit 1.41.1 :- Open-source python library that is used to create interactive web applications for data analysis
     and machine learning.
  6. NLTK:- it is used for processing and analyzing human language data. It is mostly used for tasks such as sentiment analysis,
     tokenization, etc.
And your ChatPDF is ready to Go!

# Try out a sample conversation!
Test the application by typing a sample question like this:
Q: what is Go Fish?




