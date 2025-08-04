from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

model=ChatGoogleGenerativeAI(
    model="gemini-2.0-flash")

prompt=PromptTemplate(
    template="Summarize the following text: {text}",
    input_variables=["text"],
)

parser=StrOutputParser()

loader=TextLoader(
    'cricket.txt',
    encoding='utf-8',
)
documents = loader.load()


chain= prompt | model | parser
result=chain.invoke({'text': documents[0].page_content})
print(documents[0].page_content)
print("Summary of the text: \n")
print(result)