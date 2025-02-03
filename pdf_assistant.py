import typer
from typing import Optional,List
from phi.assistant import Assistant
from phi.storage.assistant.postgres import PgAssistantStorage

from phi.knowledge.pdf import PDFUrlKnowledgeBase

from phi.vectordb.pgvector import PgVector2

from groq_embedder import GroqEmbedder

import os
from dotenv import load_dotenv

#os.environ.pop("OPENAI_API_KEY", None)
load_dotenv(dotenv_path='/Users/madmax_jos/Documents/.env') # specify the full path if it's not recoginzed- dotenv_path='fullpath/.env'

print(os.getenv("GROQ_API_KEY"))  # if you think it's not loaded
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

db_url = "postgresql+psycopg://ai:ai@localhost:5532/ai"

groq_api_key=os.getenv("GROQ_API_KEY")
# add this line only if you want to bypass embedding from openai i.e. phi.embedder.openai
#groq_embedder = GroqEmbedder(api_key=groq_api_key)

#https://wwwcdn.imo.org/localresources/en/OurWork/Security/Documents/MSC.4-Circ.268_Annual%202023%20(1).pdf
knowledge_base=PDFUrlKnowledgeBase(
    urls=["https://wwwcdn.imo.org/localresources/en/OurWork/Security/Documents/Piracy%20monthly%20report%20November%202024.pdf"],
    vector_db=PgVector2( collection="imo_marineattacksreport",db_url=db_url
    ), ) # To bypass openai embedder  - pass custom embedder parameter embedder=groq_embedder

knowledge_base.load()

storage=PgAssistantStorage(table_name="IMO_Marine_Attacks_pdf_assistant", db_url=db_url)

def IMO_Marine_Attacks_pdf_assistant(new: bool = False, user: str ="user"):
    run_id: Optional[str] = None

    if not new:
        existing_runids: List[str]= storage.get_all_run_ids(user)
        if len(existing_runids) >0:
           run_id=existing_runids[0]

    assis=Assistant( run_id=run_id, 
                        user_id=user,
                        knowledge_base=knowledge_base,
                        storage=storage,
                        # display tool calls in response
                        show_tool_calls=True,
                        # To let the assistant to see the chat history- enable true
                        read_chat_history= True, 
                        # Enable for assistant to parse through Knowledge base
                        search_knowledge=True,)
    
    if run_id is None:
        run_id=assis.run_id
        print(f"Started Run:  {run_id} \n")
    else:
        print(f"ongoing Run:  {run_id} \n")
    assis.cli_app(markdown=True)

if __name__=="__main__":
    typer.run(IMO_Marine_Attacks_pdf_assistant)
              



