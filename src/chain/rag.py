from langchain_anthropic import ChatAnthropic
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class RagChain:
    def create_chain(self):
        llm = ChatAnthropic(
            model="claude-3-haiku-20240307",
            temperature=0.7,
            max_tokens=200
        )
        
        chat_prompt = ChatPromptTemplate.from_template(
        """
            You are an assistent for question-answering tasks.
            
            Question: {question}
        """
        )
        
        chain = (
            {
                "question": lambda x: x["question"]
            }
            | chat_prompt
            | llm
            | StrOutputParser()            
        )

        return chain
                