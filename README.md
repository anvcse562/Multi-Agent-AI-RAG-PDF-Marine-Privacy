# Multi-Agent-AI-RAG-PDF-Marine-Privacy
Leveraging Multi-Agent AI with Vector Databases for Marine Piracy Analysis: A PDF-based Retrieval-Augmented Generation Approach

The multi-agent architecture primarily refers to the use of multiple AI agents working together to carry out specific tasks and enhance the overall functionality of the system. These agents interact with the knowledge base, process the PDF content, and assist the user in querying and analyzing marine piracy data. 


Here sharing the research study that's been used to demonstrate the Agen AI RAG - https://www.researchgate.net/publication/279530488_Analyzing_Marine_Piracy_from_Structured_and_Unstructured_Data_Using_SASR_Text_Miner_by_Raghavender_Reddy_Byreddy_Nitish_Byri_Tejeshwar_Gurram_Anvesh_Reddy_Minukuri_and_Goutam_Chakraborty![image](https://github.com/user-attachments/assets/3d32e793-48bf-4c44-bb68-41fdec5ecda2)


Here is a breakdown of agents being used:
1. Knowledge Base Agent
   -  Role: Manages the loading, parsing, and storage of the PDF documents (piracy reports) into a vector database.
   -  Component: PDFUrlKnowledgeBase

2. Vector Database and Embedding Agent
   -  Role: Manages the storage and retrieval of embeddings for the PDF content.
   -  Component: PgVector2

3. Assistant Agent
   -  Role: The core conversational agent that interacts with the user, processes the query, and responds with the most relevant information.
   -  Component: Assistant

4. Storage Management Agent
   -  Role: Handles session management and stores assistant state, including historical interactions and user context.
   -  Component: PgAssistantStorage


Example Interaction Flow

1.	User Input: The user can now interact with the assistant by typing queries like:
o	"How many attack types are captured in the knowledge base?"
o	"Give me a frequency table of attack types."
o	"What are the most common pirate behaviors in the Gulf of Aden?"

2.	AI Processing:
o	The assistant searches the vector database for relevant information.
o	It can classify the attack data based on types, weapons used, and other factors.
o	It generates responses by retrieving data from the knowledge base.
3.	Assistant Response: The assistant returns the answer in a conversational format, displaying results such as frequency tables, attack descriptions, and more.



<img width="353" alt="Screenshot 2025-02-02 at 11 39 00 PM" src="https://github.com/user-attachments/assets/d9d381a9-ca05-4bfb-9882-1cbbd1418ac6" />


![image](https://github.com/user-attachments/assets/1eca6f6f-087d-43a3-bed0-c20450a2d395)


Below are CLI-based assistant outputs( Ask queries and type queries and receive responses from the assistant):

![image](https://github.com/user-attachments/assets/42990efc-1606-40da-828d-18ea0045bf20)


![image](https://github.com/user-attachments/assets/fb11d7a5-8543-4271-bc29-bb339851b171)

![image](https://github.com/user-attachments/assets/1ffae629-41d1-44e1-a052-a5c4c25ea486)


![image](https://github.com/user-attachments/assets/f42de070-2f49-4a82-acae-7f86b00b7a0d)

![image](https://github.com/user-attachments/assets/b45bb181-e1b2-4371-a5b4-786c7be76586)

![image](https://github.com/user-attachments/assets/b26cbff8-ebbc-4884-b709-bb6a2e33ca57)
![image](https://github.com/user-attachments/assets/88fc9044-3eac-4a81-a67a-76033a568a6a)




