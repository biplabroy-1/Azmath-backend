from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.agents import load_tools, initialize_agent
import os

def execute_query(option: str, user_input: str):
    os.environ["SERPAPI_API_KEY"] = "c03124527bf03e21aae7b483106d31f39b02029e627e1288906b623061471125"
    API = "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"
    llm = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key=API)
    tool_names = ["serpapi"]
    tool = load_tools(tool_names)

    def base_llm(user_input):
        chat = llm
        prompt = ChatPromptTemplate.from_messages(
            [("system", "You are an intelligent assistant. You are supposed to answer any question the human asks."),
            ("human", "{input}")])
        chain = prompt | chat
        result = chain.invoke({"input": user_input})
        return result.content

    def search(to_search):
        agent = initialize_agent(tool, llm, agent="zero-shot-react-description", verbose=True)
        search_result = agent.run(to_search)
        return search_result

    def execute(option, user_input):
        if option == "core":
            return base_llm(user_input)
        elif option == "internet":
            return search(user_input)
        else:
            return "Invalid option selected."
    
    result = execute(option, user_input)
    print('hello from azmath core')
    return result