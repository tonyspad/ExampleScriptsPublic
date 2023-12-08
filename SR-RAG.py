Last login: Thu Dec  7 22:17:08 on ttys002
anthonyspadafino@anthonys-mbp-2 ~ % mkdir Python1
mkdir: Python1: File exists
anthonyspadafino@anthonys-mbp-2 ~ % mkdir Python2
anthonyspadafino@anthonys-mbp-2 ~ % cd Python2
anthonyspadafino@anthonys-mbp-2 Python2 % vim SR-RAG.py
anthonyspadafino@anthonys-mbp-2 Python2 % vim SR-RAG.py
































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

os.environ["OPENAI_API_KEY"] = ("open-ai-api-key-here")
os.environ["PC_API_KEY"] = ("pc-api-key-here")
embeddings = OpenAIEmbeddings(openai_api_key=os.environ['OPENAI_API_KEY'])
pinecone.init(
            api_key= os.environ['PC_API_KEY'],
            environment= ("pc-env-here")
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
"SR-RAG.py" 56L, 2511B
