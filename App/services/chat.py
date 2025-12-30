from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import PromptTemplate
from langchain_classic.memory import ConversationSummaryMemory
from langchain_classic.chains.llm import LLMChain

# LLM (API key read automatically from env)
chatbot = ChatMistralAI(temperature=0.3)

# Memory
memory = ConversationSummaryMemory(
    llm=chatbot,
    memory_key="summary",
    input_key="user_message"
)

# Prompt (NO f-string)
prompt = PromptTemplate(
    input_variables=["summary", "user_message"],
    template="""
You are a helpful assistant.

If the conversation summary is empty, answer the user normally
and establish the initial topic.

Stay on the same topic as the conversation summary unless the user explicitly changes it.

Conversation summary:
{summary}

User message:
{user_message}
"""
)

# Chain (memory is ATTACHED, not piped)
chain = LLMChain(
    llm=chatbot,
    prompt=prompt,
    memory=memory
)

def chatresponse(user_message: str) -> str:
    result = chain.invoke({"user_message": user_message})
    return result["text"]
