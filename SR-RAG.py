import os
import pinecone
from langchain.llms import OpenAI
from operator import itemgetter
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnablePassthrough
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyMuPDFLoader

os.environ["OPENAI_API_KEY"] = "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"
os.environ["PC_API_KEY"] = "286f7f16-6ea7-4cd9-9e22-65419c03aca3"
embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY']) 
pinecone.init(
            api_key= os.environ['PC_API_KEY'], 
            environment= 'gcp-starter'
)

#loader = PyMuPDFLoader("./docs/example.pdf")
#documents = loader.load()

vectorstore = FAISS.from_texts(
    ["Our Values: To achieve our mission of connecting people to jobs they love, we hire people who believe in and embody our values. We win and lose as a team, act as the CEO of our jobs and strive for continuous improvement with an emphasis on making an impact. As a new team member, these four areas will be critical to your success at SmartRecruiters.", 
     "Our benefits: We’ve got you covered with a competitive benefits package. Take time when you need it with unlimited PTO. Recharge during our twice annual Company Shutdown. Grow with us and enjoy our generous equity program. Invest in your wellness and receive a wellness stipend. Prepare for the future with robust retirement options by region. Give back to your community using paid time off to volunteer. Grow your career through our leadership development programs"
    ], 
    embedding=OpenAIEmbeddings()
)
retriever = vectorstore.as_retriever()

model = ChatOpenAI()
context = "You are a recruiter at Recruiting & HR SaaS platform SmartRecruiters.com. You help candidates get the information they need about open roles."

template = """Answer the question using following context:
{context}

Question: {question}

Answer in the following language: {language}
"""
prompt = ChatPromptTemplate.from_template(template)

chain = (
    {
        "context": itemgetter("question") | retriever,
        "question": itemgetter("question"),
        "language": itemgetter("language"),
    }
    | prompt
    | model
    | StrOutputParser()
)

chain.invoke({"question": "Summarize the benefits at SmartRecruiters", "language": "german"})
