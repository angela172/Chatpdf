# Conclusion

This chatbot successfully extracts text from PDF documents, processes it, generates embeddings, and performs vector search to find the best match for a user's query. 
This method allows for highly efficient and relevant search results based on the content of a PDF file.
For this task, I was able to devise a strategised approach on how I could go about building the chatbot and the logic behind it. I was able to learn alot of new things from this project. 
The challenges I had faced was when application was not able to retrieve matched output from the pdf based on the entered query. Moreover, at times though the chatbot 
would respond, it not only displays the required information but also ends up displaying the information of the next game in the pdf. Hence so as to fix these issues
I integrated the llama3 chatbot. The workflow mechansim is when we enter the query, the relevant information on the code is checked with the help of faiss to get the matching
data and is then embedded into chunks and is fed to the chatbot. The chatbot then displayes the top 3 similar data in the application.
